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


if __name__ == "__main__":
    app.run()
