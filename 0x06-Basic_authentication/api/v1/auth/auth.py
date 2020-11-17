#!/usr/bin/env python3
"""
class to manage the API authentication
"""

from flask import request
from typing import List, TypeVar, Union


class Auth:
    """
    class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """

        :param path:
        :param excluded_paths:
        :return:
        """
        if path is None:
            return True
        else:
            if path[-1] != '/':
                path += '/'
        if not excluded_paths:
            return True
        if path not in excluded_paths:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> Union[None, str]:
        """

        :param request:
        :return:
        """
        if request is None:
            return None
        if request.headers:
            if 'Authorization' not in request.headers:
                return None

        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """

        :param request:
        :return:
        """
        return None
