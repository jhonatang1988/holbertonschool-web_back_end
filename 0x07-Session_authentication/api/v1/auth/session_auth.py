#!/usr/bin/env python3
"""
Session authentication class
"""

from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    Session authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        :param user_id: user's id
        :return:
        """
        if isinstance(user_id, str):
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID
        :param session_id: session id
        :return:user Id or None
        """
        if isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """
        returns a User instance based on a cookie value
        :param request: request
        :return: User instance or None
        """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                user_id = self.user_id_for_session_id(session_id)
                if user_id:
                    User.load_from_file()
                    user = User.get(user_id)
                    if user:
                        return user
        return None

    def destroy_session(self, request=None):
        """
        destroy a session
        :param request: request
        :return:
        """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                user_id = self.user_id_for_session_id(session_id)
                if user_id:
                    del self.user_id_by_session_id[session_id]
                    return True
        return False
