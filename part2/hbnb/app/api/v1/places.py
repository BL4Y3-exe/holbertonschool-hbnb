from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

amenity_model = api.model('PlaceAmenity', {
    'id': fields.String,
    'name': fields.String
})

user_model = api.model('PlaceUser', {
    'id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String
})

place_model = api.model('Place', {
    'title': fields.String(required=True),
    'description': fields.String,
    'price': fields.Float(required=True),
    'latitude': fields.Float(required=True),
    'longitude': fields.Float(required=True),
    'owner_id': fields.String(required=True),
    'amenities': fields.List(fields.String)
})

@api.route('/')
class PlaceList(Resource):

    @api.expect(place_model, validate=True)
    @api.response(201, 'Place created')
    def post(self):
        data = api.payload

        try:
            place = facade.create_place(data)

            return {
                "id": place.id,
                "title": place.title,
                "description": place.description,
                "price": place.price,
                "latitude": place.latitude,
                "longitude": place.longitude,
                "owner_id": place.owner.id
            }, 201

        except ValueError as e:
            return {"error": str(e)}, 400


    @api.response(200, 'List of places')
    def get(self):
        places = facade.get_all_places()

        return [
            {
                "id": p.id,
                "title": p.title,
                "latitude": p.latitude,
                "longitude": p.longitude
            }
            for p in places
        ], 200
    
@api.route('/<place_id>')
class PlaceResource(Resource):

    @api.response(200, 'Place found')
    @api.response(404, 'Not found')
    def get(self, place_id):
        place = facade.get_place(place_id)

        if not place:
            return {"error": "Place not found"}, 404

        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": place.owner.id,
                "first_name": place.owner.first_name,
                "last_name": place.owner.last_name,
                "email": place.owner.email
            },
            "amenities": [
                {"id": a.id, "name": a.name}
                for a in place.amenities
            ]
        }, 200


    @api.expect(place_model, validate=True)
    @api.response(200, 'Updated')
    def put(self, place_id):
        data = api.payload

        try:
            place = facade.update_place(place_id, data)

            if not place:
                return {"error": "Place not found"}, 404

            return {
                "message": "Place updated successfully"
            }, 200

        except ValueError as e:
            return {"error": str(e)}, 400
        
@api.route('/<place_id>/reviews')
class PlaceReviewList(Resource):

    def get(self, place_id):
        reviews = facade.get_reviews_by_place(place_id)

        if reviews is None:
            return {"error": "Place not found"}, 404

        return [
            {
                "id": r.id,
                "text": r.text,
                "rating": r.rating
            }
            for r in reviews
        ], 200