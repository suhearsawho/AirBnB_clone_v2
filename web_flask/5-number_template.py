#!/usr/bin/python3
"""This starts a Flask web application"""
from flask import Flask, render_template


def create_app(test_config=None):
    """Configures and creates an application"""
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        """Index page"""
        return 'Hello HBNB!'

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """Hbnb page"""
        return 'HBNB'

    @app.route('/c/<text>', strict_slashes=False)
    def c_page(text):
        """c page"""
        return 'C {}'.format(text.replace('_', ' '))

    @app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
    @app.route('/python/<text>', strict_slashes=False)
    def python_page(text):
        """Python page"""
        return 'Python {}'.format(text.replace('_', ' '))

    @app.route('/number/<int:n>', strict_slashes=False)
    def number(n):
        """number page"""
        return str(n)

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n):
        """number template page"""
        return render_template('5-number.html', n=n)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
