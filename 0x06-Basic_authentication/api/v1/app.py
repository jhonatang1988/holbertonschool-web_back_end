#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)

from api.v1.auth.auth import Auth

import os
from werkzeug.exceptions import Unauthorized, Forbidden

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = getenv('AUTH_TYPE')
if auth:
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


# @app.errorhandler(401)
# def unauthorized(error: Unauthorized) -> str:
#     """
#     unauthorized
#     :param error: error
#     :return: json error and code
#     """
#     return jsonify({"error": "Unauthorized"}), 401

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def test_unathourized() -> str:
    """ GET /api/v1/unauthorized
    Return:
      - Raise error
    """
    return abort(401)


@app.errorhandler(403)
def forbidden(error: Forbidden) -> str:
    """
    forbidden
    :param error: error
    :return: json error and code
    """
    return jsonify({"error": "Forbidden"}), 403


def auth_needed():
    """
    checks if endpoints need auth
    :return: None if forbidden without auth
    """
    if auth:
        excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                          '/api/v1/forbidden/']
        if auth.require_auth(request.path, excluded_paths):
            if auth.authorization_header(request) is None:
                abort(401)
            if auth.current_user(request) is None:
                abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.before_request(auth_needed)
    app.run(host=host, port=port)
