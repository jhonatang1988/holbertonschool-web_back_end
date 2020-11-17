#!/usr/bin/env python3
"""
Route module for the API GET /api/v1/forbiddenGET /api/v1/forbidden
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)

from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth = getenv('AUTH_TYPE')

if auth == 'basic_auth':
    auth = BasicAuth()
elif auth:
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler GET /api/v1/forbidden
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Handle a unauthorized accessGET /api/v1/forbiddenGET /api/v1/forbidden
        Args:
            error: Error catch
        Return:
            Info of the error
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    forbidden GET /api/v1/forbiddenGET /api/v1/forbidden
    :param error: error
    :return: json error and code
    """
    return jsonify({"error": "Forbidden"}), 403


def auth_needed():
    """
    checks if endpoints need auth GET /api/v1/forbidden
    :return: None if forbidden without auth
    """
    if auth:
        excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                          '/api/v1/forbidden/']
        if auth.require_auth(request.path, excluded_paths):
            if auth.authorization_header(request) is None:
                abort(401)

            request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.before_request(auth_needed)
    app.run(host=host, port=port)
