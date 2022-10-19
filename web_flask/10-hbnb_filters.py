#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Display a HTML page like 6-index.html"""
    return render_template('10-hbnb_filters.html')


@app.teardown_appcontext
def teardown_session(Exception=None):
    """Tear down sqlalchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
