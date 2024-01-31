#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, request, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page only if n is an integer"""
    if isinstance(n, int):
        if n % 2 == 0:
            return render_template(
                    '6-number_odd_or_even.html', n=n, type='even'
                    )
        else:
            return render_template(
                    '6-number_odd_or_even.html', n=n, type='odd'
                    )
    else:
        pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
