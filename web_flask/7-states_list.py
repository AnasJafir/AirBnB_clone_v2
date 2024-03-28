#!/usr/bin/python3
"""Flask Framework"""

from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_lst():
    """Methods that returns an html page with list of states"""
    states = sorted(
            list(
                storage.all("States").values()
                ), key=lambda x: x.name
            )
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Method that close the storage"""
    storage.close()


if __name__ == "__main__":
    app.run()
