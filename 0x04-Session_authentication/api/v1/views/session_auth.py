#!/usr/bin/env python3
'''Module for session_auth'''

from api.v1.views import app_views
from api.v1.auth.session_auth import SessionAuth
from flask import jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login',
                 methods=['POST'], strict_slashes=False)
def login():
    '''Login user'''
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not pwd:
        return jsonify({"error": "password missing"}), 400

    userEmail = User.search({'email': email})

    if not userEmail or len(userEmail) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    if not userEmail[0].is_valid_password(pwd):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    auth.create_session(userEmail.id)
    # set SESSION_ID in cookie to userEmail.id
    res = jsonify(userEmail.to_json())
    res.set_cookie(getenv('SESSION_NAME'), userEmail.id)
    return res
