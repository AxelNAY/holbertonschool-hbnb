import uuid
import City from city
import Country from country
import Amenities from amenities
import Reviews from reviews

class Place:
    def __init__(self, id_place, name, description, address, id_city, id_country, latitude, longitude, id_user, rooms_number, bathrooms, price_night, max_guest, id_feature, id_reviews):
        self.id_place = uuid.uuid4()
        self.name = name
        self.description = description
        self.address = address
        self.id_city = id_city
        self.id_country = id_country
        self.latitude = latitude
        self.longitude = longitude
        self.id_user = id_user
        self.rooms_number = rooms_number
        self.bathrooms = bathrooms
        self.price_night = price_night
        self.max_guest = max_guest
        self.id_feature = id_feature
        self.id_reviews = id_reviews

    def add_place(self, name, description, address, id_city, id_country, latitude, longitude, id_user, rooms_number, bathrooms, price_night, max_guest, id_feature, id_reviews):
        pass

    def update_place(self, name, description, address, id_city, id_country, latitude, longitude, id_user, rooms_number, bathrooms, price_night, max_guest, id_feature, id_reviews):
        pass

    def get_place(self, name, description, address, id_city, id_country, latitude, longitude, id_user, rooms_number, bathrooms, price_night, max_guest, id_feature, id_reviews):
        pass

    def delete_place(self, name, description, address, id_city, id_country, latitude, longitude, id_user, rooms_number, bathrooms, price_night, max_guest, id_feature, id_reviews):
        pass
