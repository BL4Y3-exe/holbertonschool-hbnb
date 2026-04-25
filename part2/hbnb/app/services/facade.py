from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.user import User
from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            return None
        if "email" in user_data:
            existing_user = self.get_user_by_email(user_data["email"])
            if existing_user and existing_user.id != user_id:
                raise ValueError("Email already registered")

        self.user_repo.update(user_id, user_data)
        return user

    def get_place(self, place_id):
        pass


    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None

        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity
    
    def create_place(self, place_data):
        owner = self.user_repo.get(place_data["owner_id"])
        if not owner:
            raise ValueError("Owner not found")

        amenities = []
        for amenity_id in place_data.get("amenities", []):
            amenity = self.amenity_repo.get(amenity_id)
            if amenity:
                amenities.append(amenity)

        place_data["owner"] = owner
        place_data["amenities"] = amenities

        place = Place(**place_data)
        self.place_repo.add(place)
        return place


    def get_place(self, place_id):
        return self.place_repo.get(place_id)


    def get_all_places(self):
        return self.place_repo.get_all()


    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if not place:
            return None

        if "owner_id" in place_data:
            owner = self.user_repo.get(place_data["owner_id"])
            if not owner:
                raise ValueError("Owner not found")
            place_data["owner"] = owner

        if "amenities" in place_data:
            amenities = []
            for a_id in place_data["amenities"]:
                a = self.amenity_repo.get(a_id)
                if a:
                    amenities.append(a)
            place_data["amenities"] = amenities

        self.place_repo.update(place_id, place_data)
        return place