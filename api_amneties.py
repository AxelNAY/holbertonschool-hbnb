# app.py
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from amneties import Amneties  # Importing the provided model

app = Flask(__name__)
api = Api(app, doc='/docs', title='Amenities API', description='API for managing amenities')

# Define the model for API documentation
amenity_model = api.model('Amenity', {
    'id': fields.String(readonly=True, description='The unique identifier of the amenity'),
    'name': fields.String(required=True, description='The name of the amenity'),
    'created_at': fields.String(readonly=True, description='Creation date of the amenity'),
    'updated_at': fields.String(readonly=True, description='Last update date of the amenity')
})

# Utility function to get an amenity by id
def get_amenity_by_id(amenity_id):
    for amenity in Amneties.amneties_object_list:
        if amenity['_Amneties__id'] == amenity_id:
            return amenity
    return None

@api.route('/amenities')
class AmenityList(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        """Retrieve a list of all amenities"""
        return Amneties.amneties_object_list

    @api.expect(amenity_model, validate=True)
    @api.response(201, 'Amenity successfully created.')
    @api.response(409, 'Amenity name already exists.')
    def post(self):
        """Create a new amenity"""
        data = request.json
        if any(amenity['name'] == data['name'] for amenity in Amneties.amneties_object_list):
            api.abort(409, 'Amenity name already exists.')
        new_amenity = Amneties()
        new_amenity.name = data['name']
        new_amenity.save()
        return new_amenity.__dict__, 201

@api.route('/amenities/<string:amenity_id>')
@api.response(404, 'Amenity not found.')
class Amenity(Resource):
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Retrieve detailed information about a specific amenity"""
        amenity = get_amenity_by_id(amenity_id)
        if not amenity:
            api.abort(404, 'Amenity not found.')
        return amenity

    @api.expect(amenity_model, validate=True)
    @api.response(200, 'Amenity successfully updated.')
    @api.response(404, 'Amenity not found.')
    @api.response(409, 'Amenity name already exists.')
    def put(self, amenity_id):
        """Update an existing amenity’s information"""
        amenity = get_amenity_by_id(amenity_id)
        if not amenity:
            api.abort(404, 'Amenity not found.')
        data = request.json
        if any(a['name'] == data['name'] for a in Amneties.amneties_object_list if a['_Amneties__id'] != amenity_id):
            api.abort(409, 'Amenity name already exists.')
        amenity['name'] = data['name']
        amenity['updated_at'] = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
        Amneties.save_to_file()
        return amenity, 200

    @api.response(204, 'Amenity successfully deleted.')
    def delete(self, amenity_id):
        """Delete a specific amenity"""
        amenity = get_amenity_by_id(amenity_id)
        if not amenity:
            api.abort(404, 'Amenity not found.')
        Amneties.amneties_object_list.remove(amenity)
        Amneties.save_to_file()
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)

