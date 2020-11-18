#!/usr/bin/env python3
"""
module of session authentication
"""

from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models.user import User
from typing import Union, Dict
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Dict[str, str]:
    """
    view for login form
    :return: dict representation of User instance
    """
    if request:
        email = request.form.get('email', None)
        if not email:
            return jsonify({"error": "email missing"}), 400
        password = request.form.get('password', None)
        if not password:
            return jsonify({"error": "password missing"}), 400
        users_with_email: list[Union[User, None]] = User.search({'email':
                                                                     email})
        if not users_with_email:
            return jsonify({"error": "no user found for this email"}), 404
        if not users_with_email[0].is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        user = users_with_email[0]
        from api.v1.app import auth
        cookie_value = auth.create_session(user.id)
        if cookie_value:
            cookie_name = getenv('SESSION_NAME')
            response = make_response(jsonify(user.to_json()), 200)
            response.headers['Content-Type'] = 'application/json'
            response.set_cookie(cookie_name, value=cookie_value)
            return response
