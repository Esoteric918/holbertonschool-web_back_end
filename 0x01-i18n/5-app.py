#!/usr/bin/env python3
'''Basic flask app for i18n'''

from gettext import gettext
from flask import Flask, g, render_template, request
from flask_babel import Babel
from flask_babel import gettext as _


app = Flask(__name__)
babel = Babel(app)

# mock database for task 5
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    '''get local

        Detects if the incoming request contains locale argument and
        ifs value is a supported locale, return it. If not or if the
        parameter is not present, resort to the previous default behavior.
    '''
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
            return locale
    return request.accept_languages.best_match(Config.LANGUAGES)

def get_user() -> dict:
    '''get user

        Returns a user dict from the users dict based on the id
        passed in the url.
    '''
    user_id = request.args.get('login_as')
    if not user_id:
        return None
    try:
        user_id = int(user_id)
        if user_id < 1 or user_id > 4:
            raise Exception
    except Exception:
        return None
    return

@app.before_request
def before_request():
    '''before request

        Sets the user dict in the request context.
    '''
    data = get_user()
    if data:
        g.user = data
    else:
        g.user = None



@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    ''' Return the index page '''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
