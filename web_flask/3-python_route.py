#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns a string at the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns a string at the route /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """Display C followed by the value of <text>"""
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Display Python followed by the value of <text>
    The default value of text is “is cool” if it is not provided in the URL
    """
    formatted_text = text.replace('_', ' ')
    return "Python {}".format(formatted_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
