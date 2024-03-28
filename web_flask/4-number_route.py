#!/usr/bin/python3
"""Hello Flask"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Method that returns Welcome message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    "Method that returns HBNB"
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Method that returns a text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/')
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Method that returns a text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Method that checks if a given input is a number"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run()
