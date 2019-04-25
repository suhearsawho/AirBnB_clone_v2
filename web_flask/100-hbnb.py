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

    @app.route('/states', strict_slashes=False)
    @app.route('/states/<id>', strict_slashes=False)
    def states(id=None):
        """Displays a State object with corresponding id"""
        state_obj = storage.all('State')
        match = None
        if id:
            for state in state_obj.values():
                if state.id == id:
                    match = state
                    break
        else:
            match = state_obj
        return render_template('9-states.html', id=id, state=match)

    @app.route('/hbnb_filters', strict_slashes=False)
    def hbnb_filters():
        """Displays the main home page for HBNB"""
        states = storage.all('State')
        cities = storage.all('City')
        amenities = storage.all('Amenity')
        return render_template('10-hbnb_filters.html', states=states,
                               cities=cities, amenities=amenities)

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """Displays the hbnb page"""
        states = storage.all('State')
        cities = storage.all('City')
        amenities = storage.all('Amenity')
        places = storage.all('Place')
        users = storage.all('User')
        return render_template('100-hbnb.html', states=states, cities=cities,
                               amenities=amenities, places=places, users=users)

    @app.teardown_appcontext
    def teardown(app):
        """Teardown context"""
        storage.close()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
