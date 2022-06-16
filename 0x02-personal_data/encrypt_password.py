#!/usr/bin/env python3
'''Write a function called hash_password'''

from bcrypt import hashpw, gensalt


def hash_password(password: str) -> bytes:
    '''
    Args:
        password: string representing the password to be hashed
    Return:
        string representing the hashed password'''
    hashed = hashpw(password.encode('utf-8'), gensalt())
    return hashed
