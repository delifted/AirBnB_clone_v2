#!/usr/bin/python3
"""Script that starts a Flask web app"""

from flask import Flask


app = Flask(__name__)


# Reroute to display "Hello HBNB!" with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<name>', strict_slashes=False)
def c(name):
    return 'C ' + name.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return f"{n } is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
