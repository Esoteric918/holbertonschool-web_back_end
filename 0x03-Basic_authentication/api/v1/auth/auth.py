#!/usr/bin/env python3
''' Class to handle API authentication'''
from typing import TypeVar, List, Dict, Any
from flask import  request


class Auth():
    '''template for all authentication systems'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' Return True if path not in list of excluded paths
            Args:
                path: path to check
                excluded_paths: list of paths to exclude
        '''
        if path is None and excluded_paths is None:
            return True
        # loop through excluded paths and check if path is in list
        if path in excluded_paths or f'{path}/' in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header
        """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user
        """
        if request is None:
            auth_header = self.authorization_header(request)
        if auth_header:
            return self.decode_token(auth_header)
        return None