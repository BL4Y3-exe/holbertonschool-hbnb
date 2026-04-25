from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

# User
user = User("John", "Doe", "john@mail.com")

# Place
place = Place("Nice house", "Cool place", 100, 40.0, 50.0, user)

# Amenity
wifi = Amenity("Wi-Fi")
place.add_amenity(wifi)

# Review
review = Review("Great!", 5, place, user)
place.add_review(review)

print(place.title)
print(place.owner.first_name)
print(place.amenities[0].name)
print(place.reviews[0].text)