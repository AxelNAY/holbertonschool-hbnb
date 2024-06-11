#!/usr/bin/python
import uuid
import datetime
import json
DataManager = __import__('DataManager').DataManager

class Amenities(DataManager):
    amenities = ["couch", "dishwasher", "fridge", "microwave", "wifi", "TV", "Balcony"]
    amenitie_count = 0
    my_dict = {}
    def __init__(self, id_feature, name):
        self.id_place = uuid.uuid4()
        self.name = name
        self.created_at = datetime.datetime.today()
        self.update_at = datetime.datetime.today()
        Amenities.amnetie_count += 1

    def save_amenities(self, name):
        with open("Amneties.json", 'w') as my_file:
            json.dump(object, my_file)

    def update_amenities(self, name):
        j = 0
        self.update_at = datetime.datetime.today()
        for key in amneties:
            if name == amenities[i]:
                my_dict[j] = self.name
                j += 1

    def get_amenities(self, name):
        return Amenities.amenities_list

    def __del__(self):
        Amenities.amenitie_count -= 1
