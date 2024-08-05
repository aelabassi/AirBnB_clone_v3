#!/usr/bin/python3
"""Index module"""
from api.v1.views import app_views
from flask import jsonify
import models
from models.base_model import BaseModel


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Return stats"""
    from models import storage
    classes = {"amenities": Amenity,
               "cities": City,
               "places": Place,
               "reviews": Review,
               "states": State,
               "users": User}
    return jsonify({key: storage.count(value) for key, value in classes.items()})
