#!/usr/bin/env python3
"""
basic authentication for auth
"""
import binascii
import json

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
from models.base import Base, DATA


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        decodes string from the authorization header
        :param base64_authorization_header: auth header
        :return: None of decoded string
        """

        try:
            return base64.b64decode(base64_authorization_header).decode(
                'utf-8')
        except TypeError:
            return None
        except binascii.Error:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """
        extract user credentials
        :param decoded_base64_authorization_header:
        :return: None, None or email and pasword
        """
        if isinstance(decoded_base64_authorization_header, str):
            splitted = decoded_base64_authorization_header.split(':')
            if len(splitted) != 2:
                return None, None
            return splitted[0], splitted[1]
        return None, None

    def user_object_from_credentials(
            self,
            user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password
        :param user_email: email
        :param user_pwd: password
        :return: None or User instance
        """
        if isinstance(user_email, str) and isinstance(user_pwd, str):
            User.load_from_file()
            users_with_email = User.search(
                {'email': user_email})

            if users_with_email:
                for user in users_with_email:
                    if user.is_valid_password(pwd=user_pwd):
                        return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        retrieves the User instance for a request
        :param request: the request
        :return:
        """

        if request:
            auth_credentials = self.authorization_header(request)

            if auth_credentials:
                encoded_str = self.extract_base64_authorization_header(
                    auth_credentials)

                if encoded_str:
                    decoded_str = self.decode_base64_authorization_header(
                        encoded_str)
                    print(decoded_str)

                    if decoded_str:
                        user_credentials = self.extract_user_credentials(
                            decoded_str)

                        if not any(map(lambda x: x is None, user_credentials)):
                            user = self.user_object_from_credentials(
                                user_email=user_credentials[0],
                                user_pwd=user_credentials[1]
                            )

                            if user:
                                return user

        return None
