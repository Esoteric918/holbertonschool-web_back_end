#!/usr/bin/env python3
'''Create a class BasicAuth that inherits from Auth'''


from base64 import b64decode
from collections import UserDict, UserList
from re import search
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    '''Create a class BasicAuth that inherits from Auth'''

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''Extract the base64 encoded authorization header'''
        if authorization_header:
            if type(authorization_header) is str:
                if authorization_header.startswith("Basic "):
                    return authorization_header[6:]
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        '''Decode the base64 encoded authorization header'''
        try:
            return b64decode(base64_authorization_header).decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
                                self,
                                decoded_base64_authorization_header: str
                                ) -> Tuple[str, str]:
        '''Extract the user credentials'''
        if decoded_base64_authorization_header:
            if type(decoded_base64_authorization_header) is str:
                if decoded_base64_authorization_header.find(":") > 0:
                    return decoded_base64_authorization_header.split(":")
        return None, None

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        '''Create a user object from the credentials'''
        if user_email and user_pwd:
            if type(user_email) is str and type(user_pwd) is str:
                res = User.search({'email': user_email})
                if res:
                    if res[0].is_valid_password(user_pwd):
                        return res[0]
        return None
