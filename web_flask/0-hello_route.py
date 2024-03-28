#!/usr/bin/python3
"""Hello Flask"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Method that returns Welcome message"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
