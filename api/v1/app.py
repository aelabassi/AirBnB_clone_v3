#!/usr/bin/python3
"""App module"""
from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """Return a 404 error"""
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = 5000
    app.run(host=host, port=port, threaded=True)
