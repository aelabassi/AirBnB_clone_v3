#!/usr/bin/python3
"""Places amenities view """
from api.v1.views import app_views
from flask import abort
from models.amenity import Amenity
from flask import jsonify
import os
from models.place import Place
from flask import request
from models import storage

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    @app_views.route('/places/<place_id>/amenities',
                     methods=['GET'], strict_slashes=False)
    @app_views.route('/places/<place_id>/amenities/',
                     methods=['GET'], strict_slashes=False)
    def get_amenities(place_id):
        """Return all amenities"""
        all_places = storage.all(Place).values()
        place = [place for place in all_places if place.id == place_id]
        if not place:
            abort(404)
        return jsonify([amenity.to_dict() for amenity in place[0].amenities])

    @app_views.route('/places/<place_id>/amenities/<amenity_id>',
                     methods=['DELETE'],
                     strict_slashes=False)
    def delete_amenity(place_id, amenity_id):
        """Delete a amenity"""
        all_places = storage.all(Place).values()
        place = [place for place in all_places if place.id == place_id]
        if not place:
            abort(404)
        all_amenities = storage.all(Amenity).values()
        amenity = [amenity for amenity in all_amenities
                   if amenity.id == amenity_id]
        if not amenity:
            abort(404)
        if amenity[0] not in place[0].amenities:
            abort(404)
        place[0].amenities.remove(amenity[0])
        storage.save()
        return jsonify({}), 200

    @app_views.route('/places/<place_id>/amenities/<amenity_id>',
                     methods=['POST'],
                     strict_slashes=False)
    def post_amenity(place_id, amenity_id):
        """Create a amenity"""
        all_places = storage.all(Place).values()
        place = [place for place in all_places if place.id == place_id]
        if not place:
            abort(404)
        all_amenities = storage.all(Amenity).values()
        amenity = [amenity for amenity in all_amenities
                   if amenity.id == amenity_id]
        if not amenity:
            abort(404)
        if amenity[0] in place[0].amenities:
            return jsonify(amenity[0].to_dict()), 200
        place[0].amenities.append(amenity[0])
        storage.save()
        return jsonify(amenity[0].to_dict()), 201


else:
    @app_views.route('/places/<place_id>/amenities',
                     methods=['GET'], strict_slashes=False)
    @app_views.route('/places/<place_id>/amenities/',
                     methods=['GET'], strict_slashes=False)
    def get_amenities(place_id):
        """Return all amenities"""
        all_places = storage.all(Place).values()
        place = [place for place in all_places if place.id == place_id]
        if not place:
            abort(404)
        return jsonify([amenity.to_dict() for amenity in place[0].amenities])

    @app_views.route('/places/<place_id>/amenities/<amenity_id>',
                     methods=['DELETE'],
                     strict_slashes=False)
    def delete_amenity(place_id, amenity_id):
        """Delete a amenity"""
        all_places = storage.all(Place).values()
        place = [place for place in all_places if place.id == place_id]
        if not place:
            abort(404)
        all_amenities = storage.all(Amenity).values()
        amenity = [amenity for amenity in all_amenities
                   if amenity.id == amenity_id]
        if not amenity:
            abort(404)
        if amenity[0] not in place[0].amenities:
            abort(404)
        place[0].amenities.remove(amenity[0])
        storage.save()
        return jsonify({}), 200

    @app_views.route('/places/<place_id>/amenities/<amenity_id>',
                     methods=['POST'], strict_slashes=False)
    def post_amenity(place_id, amenity_id):
        """Create a amenity"""
        all_places = storage.all(Place).values()
        place = [place for place in all_places if place.id == place_id]
        if not place:
            abort(404)
        all_amenities = storage.all(Amenity).values()
        amenity = [amenity for amenity in all_amenities
                   if amenity.id == amenity_id]
        if not amenity:
            abort(404)
        if amenity[0] in place[0].amenities:
            return jsonify(amenity[0].to_dict()), 200
        place[0].amenities.append(amenity[0])
        storage.save()
        return jsonify(amenity[0].to_dict()), 201
