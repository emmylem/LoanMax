#!/usr/bin/python3
"""This module starts the flask app fo LoanMax."""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def display_homepage():
    """Handles Homepage of LoanMax."""
    return render_template('loan.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
