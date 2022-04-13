#!/usr/bin/python3
"""module hello route of flask"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Print first message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Print route hbnb message"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_ctext(text):
    """Print a variable rule <text>"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_pythontext(text='is cool'):
    """print python default or not text"""
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)