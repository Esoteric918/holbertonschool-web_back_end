#!/usr/bin/env python3
'''Basic flask app for i18n'''

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

class Config(object):
    '''
    Config class for flask-babel
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


@babel.localeselector
def get_local(self):
    '''get local'''
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
