#!/usr/bin/python3
import uuid
Place = __import__('Place').Place

class Amenities(Place):
    amneties = ["couch", "dishwasher", "fridge", "microwave", "wifi", "TV", "Balcony"]
    my_dict = {}
    def __init__(self, id_feature, name):
        self.id_place = uuid.uuid4()
        self.name = name
        self.created_at = datetime.datetime.today()
        self.update_at = datetime.datetime.today()

    def save_amenities(self, name):
        pass

    def update_amenities(self, name):
        j = 0
        self.update_at = datetime.datetime.today()
        for key in amneties:
            if name == amneties[i]:
                my_dict[j] = self.name
                j += 1

    def get_amenities(self, name):
        pass

    def delete_amenities(self, name):
        pass
