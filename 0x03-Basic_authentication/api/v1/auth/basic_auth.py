#!/usr/bin/env python3
'''Create a class BasicAuth that inherits from Auth'''

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''Create a class BasicAuth that inherits from Auth'''

    def __init__(self):
        '''Initialize the class'''
        super().__init__()
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''Extract the base64 encoded authorization header'''
        if authorization_header:
            if type(authorization_header) is str:
                if authorization_header.startswith("Basic "):
                    return authorization_header[6:]
        return None
