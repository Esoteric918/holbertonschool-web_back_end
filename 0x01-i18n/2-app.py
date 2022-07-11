#!/usr/bin/env python3
'''Basic flask app for i18n'''

from email.policy import strict
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    ''' Config class for flask-babel '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale(self):
    '''get local'''
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    ''' Index page '''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
