#!/usr/bin/python3
"""Create Flask for State objects"""
from models import storage
from models.state import State
from flask import Flask, render_template
STATES = Flask(__name__)
STATES.url_map.strict_slashes = False


@STATES.route('/states_list')
def dispalySates():
    state_list = storage.all(State)
    sorted_list = state_list.sorted()
    return render_template('7-states_list.html', States=sorted_list)

if __name__ == '__main__':
    STATES.run(debug=True, host='0.0.0.0', port=5000)
