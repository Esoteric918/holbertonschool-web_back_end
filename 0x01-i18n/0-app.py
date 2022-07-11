#!/usr/bin/env python3
'''Basic flask app for i18n'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    ''' Index page '''
    return render_template('0-index.html')
