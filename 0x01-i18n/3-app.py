#!/usr/bin/env python3
'''Basic flask app for i18n'''

from gettext import gettext
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
gettext(u'home_title')
gettext(u'home_header')

@babel.localeselector
def get_local():
    '''get local'''
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    ''' Return the index page '''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)