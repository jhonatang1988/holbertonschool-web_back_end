#!/usr/bin/env python3
"""
basic authentication for auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    basic authentication
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        get the auth header after Basic
        :param authorization_header: auth header
        :return: the base64 encoded string or None
        """
        if isinstance(authorization_header, str):
            splitted = authorization_header.split(' ')
            if len(splitted) != 2:
                return None

            if splitted[0] != 'Basic':
                return None

            return splitted[1]

        return None
