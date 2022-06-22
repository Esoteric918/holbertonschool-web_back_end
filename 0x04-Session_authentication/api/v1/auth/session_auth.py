#!/usr/bin/env python3
'''Initailize class session_auth'''


import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    '''Class session_auth'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''Create session'''
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str((uuid.uuid4()))
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''Get user_id for session_id'''
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)
