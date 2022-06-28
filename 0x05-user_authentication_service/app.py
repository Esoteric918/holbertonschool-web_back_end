#!/usr/bin/env python3
''' init flask app '''

from flask import Flask, jsonify, request, abort, make_response
from auth import Auth
from user import User

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
