#!/usr/bin/python3
"""this module defines and creates a new Flask application"""
from flask import Flask, render_template
from models import storage


def create_app():
    """Creates and sets up a Flask application"""
    app = Flask(__name__)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        """Displays an HTML page with list of states"""
        state_obj = storage.all('State')
        return render_template('7-states_list.html', state_obj=state_obj)

    @app.route('/cities_by_states', strict_slashes=False)
    def cities_by_states():
        """Displays an HTML page"""
        state_obj = storage.all('State')
        return render_template('8-cities_by_states.html', state_obj=state_obj)

    @app.teardown_appcontext
    def teardown(app):
        """Teardown context"""
        storage.close()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
