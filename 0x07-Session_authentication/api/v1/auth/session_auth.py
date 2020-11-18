#!/usr/bin/env python3
"""
Session authentication class
"""

from api.v1.auth.auth import Auth
import uuid


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
