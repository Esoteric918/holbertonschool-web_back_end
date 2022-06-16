#!/usr/bin/env python3
'''Write a function called hash_password'''
import bcrypt


def hash_password(password: str) -> str:
    '''
    Args:
        password: string representing the password to be hashed
    Return:
        string representing the hashed password'''
    return bcrypt.hashpw(password, bcrypt.gensalt())
