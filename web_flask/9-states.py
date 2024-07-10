#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects sorted by name"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=sorted_states)

@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Display a HTML page with a list of City objects for a given State id"""
    state = storage.get(State, id)
    if state is None:
        return render_template('state_not_found.html')
    cities = state.cities
    sorted_cities = sorted(cities, key=lambda x: x.name)
    return render_template('state_cities.html', state=state, cities=sorted_cities)

@app.teardown_appcontext
def teardown_db(exception=None):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
