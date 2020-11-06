#!/usr/bin/env python3
"""
hash a password
"""

import bcrypt
from typing import ByteString


def hash_password(password: str) -> ByteString:
    """
    hash a password and returned byte string hashed password
    :param password: password
    :return: byte string hashed password
    """
    byte_pass = password.encode('utf-8')
    hashed = bcrypt.hashpw(byte_pass, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validate that the provided password matches the hashed password
    :param hashed_password: hashed_password
    :param password: password
    :return: True if is match, False otherwise
    """
    password = password.encode('utf-8')
    if bcrypt.checkpw(password, hashed_password):
        return True
    else:
        return False
