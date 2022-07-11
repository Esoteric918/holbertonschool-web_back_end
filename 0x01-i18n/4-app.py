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
def get_locale():
    '''get locale

        Detects if the incoming request contains locale argument and
        ifs value is a supported locale, return it. If not or if the
        parameter is not present, resort to the previous default behavior.
    '''
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    ''' Return the index page '''
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
