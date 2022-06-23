#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS)


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv("AUTH_TYPE")
if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    # create an instance of BasicAuth and assign it to the variable auth
    auth = BasicAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    # create an instance of SessionAuth and assign it to the variable auth
    auth = SessionAuth()
else:
    auth_type == 'auth'
    from api.v1.auth.auth import Auth
    # create an instance of Auth and assign it to the variable auth
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """
    This function is called before the request is processed.
    """
    auth_list = ["/api/v1/status/",
                 "/api/v1/unauthorized/",
                 "/api/v1/forbidden/"]

    if auth and auth.require_auth(request.path, auth_list):
        if auth.authorization_header(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)

        request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
