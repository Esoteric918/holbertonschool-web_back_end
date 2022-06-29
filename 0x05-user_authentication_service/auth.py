#!/usr/bin/env python3


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

def _hash_password(password: str) -> bytes:
    """Hash a password

    Args:
        password: password to hash
    """
    pwd = password.encode()
    return hashpw(pwd, gensalt())

def _generate_uuid(self) -> str:
        '''Generate a new UUID'''
        return str(uuid.uuid4())
