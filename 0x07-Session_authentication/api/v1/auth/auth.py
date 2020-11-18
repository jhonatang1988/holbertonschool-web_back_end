#!/usr/bin/env python3
"""
class to manage the API authentication
"""

from flask import request
from typing import List, TypeVar, Union
from os import getenv


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
        if not excluded_paths:
            return True

        split_exc_paths = []

        for exc_path in excluded_paths:
            reg_exp = exc_path.split('*', 1)
            split_exc_paths.append(reg_exp[0])

        for exc_path in split_exc_paths:
            len_exc_path = len(exc_path)
            sub_str_path = path[:len_exc_path]
            if sub_str_path == exc_path:
                return False

        if path[-1] != '/':
            path += '/'
            if path not in excluded_paths:
                return True

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
        base class for current_user, must be create in childs
        :param request:
        :return:
        """
        return None

    def session_cookie(self, request=None):
        """
        returns a cookie value from a request
        :param request: request
        :return: cookie or None
        """
        if request:
            session_name = getenv('SESSION_NAME')

            if session_name == '_my_session_id':
                return request.cookies.get('_my_session_id', None)
