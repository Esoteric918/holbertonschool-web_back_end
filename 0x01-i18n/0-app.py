#!/usr/bin/env python3
'''Basic flask app for i18n'''
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_babel import Babel, gettext, lazy_gettext

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
