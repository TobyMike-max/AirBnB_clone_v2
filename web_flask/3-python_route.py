#!/usr/bin/python3
"""Script that starts a web application."""

from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Return Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Return C followed by value of text variable."""
    return ("C {}".format(escape(text)))


@app.route('/python/<text>', strict_slashes=False)
def python_str(text='is cool'):
    """Return Python foolowed by value of text"""
    return ("Python {}".format(escape(text)))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
