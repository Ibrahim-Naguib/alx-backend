#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Configuration for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale():
    """Select and return best language match based on supported languages"""
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def home() -> str:
    """Basic Flask app"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
