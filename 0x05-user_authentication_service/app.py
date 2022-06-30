#!/usr/bin/env python3
''' init flask app '''

import email
from flask import Flask, abort, jsonify, redirect, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    '''init flask app '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def registerUser():
    '''Register a new user.

    Args:
        email: email address of the user
        password: hashed password of the user
    '''
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})

    except ValueError:
        return jsonify({'message': "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Route for loggin in a user"""
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not (AUTH.valid_login(
            email=email,
            password=pwd)) or not email or not pwd:
        abort(401)

    session_id = AUTH.create_session(email=email)
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Route for logging out a user"""
    session_id = request.cookies.get('session_id')
    if not session_id or not AUTH.get_user_from_session_id(session_id):
        abort(403)

    AUTH.destroy_session(session_id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """Route for getting the profile of a user"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user and session_id:
        return jsonify({'email': user.email}), 200
    else:
        abort(403)

@app.route('/reset-password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """Route for getting a reset password token"""
    email = request.form.get('email')
    if not email:
        abort(403)

    token = AUTH.get_reset_password_token(email)

    return jsonify({"email": "<user email>", "reset_token": token}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
