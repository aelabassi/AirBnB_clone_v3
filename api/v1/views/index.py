#!/usr/bin/python3
"""Index module"""
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
    return jsonify({key: storage.count(value) for key,
                    value in classes.items()})
