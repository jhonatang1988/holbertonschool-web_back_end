#!/usr/bin/env python3
"""
session authentication that's being save in a database
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """
    session authentication that's being save in a database
    """

    def create_session(self, user_id=None):
        """
        overloads parents create_session. Creates a UserSession Object and
        saves it in the database
        :param user_id:
        :return:
        """
        session_id = super().create_session(user_id=user_id)
        if session_id:
            user_session = UserSession(user_id=user_id, session_id=session_id)
            user_session.save()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        overloads from parent. looks for user_id in the database and returns it
        :param session_id: session id
        :return: user id.
        """
        if session_id:

            UserSession.load_from_file()
            user_session_list = UserSession.search(
                {'session_id': session_id})

            if user_session_list:
                session = user_session_list[0]
                user_id = session.user_id
                if hasattr(session, 'created_at'):
                    current = datetime.utcnow()
                    if user_id:
                        if self.session_duration <= 0 or not self.session_duration:
                            return user_id
                        if (session.created_at + timedelta(
                                seconds=self.session_duration)) < current:
                            return None

                        return user_id

        return None

    def destroy_session(self, request=None):
        """
        destroy the session saved in the database
        :param request: request
        :return:
        """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                UserSession.load_from_file()
                user_session_list = UserSession.search(
                    {'session_id': session_id})

                if user_session_list:
                    user_session = user_session_list[0]
                    if user_session:
                        user_session.remove()
                        return True

        return False
