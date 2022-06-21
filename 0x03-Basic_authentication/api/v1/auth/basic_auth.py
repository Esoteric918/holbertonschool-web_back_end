#!/usr/bin/env python3
'''Create a class BasicAuth that inherits from Auth'''

from api.v1.auth.auth import Auth


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
        if base64_authorization_header:
            if type(base64_authorization_header) is str:
                return base64_authorization_header.decode("utf-8")
        return None
