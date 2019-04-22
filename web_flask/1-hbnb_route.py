#!/usr/bin/python3
"""Starts a flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Defines the index page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Defines the hbnb page"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
