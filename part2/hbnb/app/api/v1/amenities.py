from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):

    @api.expect(amenity_model, validate=True)
    @api.response(201, 'Amenity created')
    def post(self):
        data = api.payload

        amenity = facade.create_amenity(data)

        return {
            "id": amenity.id,
            "name": amenity.name
        }, 201

    @api.response(200, 'List of amenities')
    def get(self):
        amenities = facade.get_all_amenities()

        return [
            {
                "id": a.id,
                "name": a.name
            }
            for a in amenities
        ], 200
    

@api.route('/<amenity_id>')
class AmenityResource(Resource):

    @api.response(200, 'Amenity found')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        amenity = facade.get_amenity(amenity_id)

        if not amenity:
            return {"error": "Amenity not found"}, 404

        return {
            "id": amenity.id,
            "name": amenity.name
        }, 200

    @api.expect(amenity_model, validate=True)
    @api.response(200, 'Amenity updated')
    @api.response(404, 'Amenity not found')
    def put(self, amenity_id):
        data = api.payload

        amenity = facade.update_amenity(amenity_id, data)

        if not amenity:
            return {"error": "Amenity not found"}, 404

        return {
            "id": amenity.id,
            "name": amenity.name
        }, 200