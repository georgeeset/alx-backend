#!/usr/bin/env python3
""" Route module for the API """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ configuration class
    for supported languages
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('4-app.Config')


@babel.localeselector
def get_locale() -> str:
    """ Determines best match for supported languages
    check if user spcified language
    """
    locale_data = request.query_string.decode('utf-8').split('&')
    locale_split = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        locale_data,
    ))
    if 'locale' in locale_split:
        if locale_split['locale'] in app.config["LANGUAGES"]:
            return locale_split['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    flask index page
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
