#!/usr/bin/env python3


from lib2to3.pgen2 import token
from bcrypt import checkpw, gensalt, hashpw
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''Register a new user.

        Args:
            email: email address of the user
            password: hashed password of the user
        '''
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        '''Validate a user login'''
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'), user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        '''Create a new session for a user'''
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        '''Get a user by session id'''
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''Destroy a session with a user id'''
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        '''get a reset password token'''
        try:
            email = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(email.id, reset_token=token)
        except Exception:
            return None


def _hash_password(password: str) -> bytes:
    """Hash a password

    Args:
        password: password to hash
    """
    pwd = password.encode()
    return hashpw(pwd, gensalt())


def _generate_uuid() -> str:
    '''Generate a new UUID'''
    return str(uuid.uuid4())
