#!/usr/bin/env python3
'''Write a function called hash_password'''

import bcrypt


def hash_password(password: str) -> bytes:
    '''
    Args:
        password: string representing the password to be hashed
    Return:
        string representing the hashed password'''

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Args:
        hashed_password: string representing the hashed password
        password: string representing the password to be checked
    Return:
        True if the password is valid, False otherwise'''

    return bcrypt.checkpw(password.encode(), hashed_password)
