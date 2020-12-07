#!/usr/bin/env python3
"""
session expiration for session id auth system
"""
from datetime import datetime, timedelta

from api.v1.auth.session_auth import SessionAuth
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    session expiration for session id auth system
    """

    def __init__(self):
        """
        init
        """
        self.session_duration = getenv('SESSION_DURATION', 0)
        try:
            self.session_duration = int(self.session_duration)
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        overloads father create_session
        :param user_id: user's id
        :return: session id or None
        """
        session_id = super().create_session(user_id=user_id)
        if session_id:
            self.user_id_by_session_id[session_id] = {}
            self.user_id_by_session_id[session_id]['user_id'] = user_id
            self.user_id_by_session_id[session_id][
                'created_at'] = datetime.now()

            return session_id

        return None

    def user_id_for_session_id(self, session_id=None):
        """
        overloads: get user id from session id
        :param session_id:
        :return: user_id or None
        """
        if session_id:
            if session_id in self.user_id_by_session_id:
                if 'created_at' not in \
                        self.user_id_by_session_id[session_id]:
                    return None
                else:
                    current = datetime.now()
                    if self.user_id_by_session_id[
                        session_id]['created_at'] \
                            + timedelta(seconds=self.session_duration) < \
                            current:
                        return None
            if session_id in self.user_id_by_session_id:
                if self.session_duration >= 0:
                    return self.user_id_by_session_id[session_id]['user_id']

        return None
