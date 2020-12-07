#!/usr/bin/env python3
"""
model for user sessions
"""
from models.base import Base


class UserSession(Base):
    """
    model for user sessions
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        initialize
        :param args: args without keywords
        :param kwargs: keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.user_id: str = kwargs.get('user_id')
        self.session_id: str = kwargs.get('session_id')

