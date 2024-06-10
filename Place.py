#!/usr/bin/python3
import uuid
import datetime
import json


class Place:
    place_count = 0

    def __init__(self, name="", description="", adress="", latitude=0, longitude=0, rooms=0,
                 bathrooms=0, price_night=0, guest_capacity=0, city_name=""):
        self.name = name
        self.description = description
        self.adress = adress
        self.latitude = latitude
        self.longitude = longitude
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price_night = price_night
        self.guest_capacity = guest_capacity
        self.city_name = city_name
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id = uuid.uuid1()
        Place.place_count += 1


    def get_place(self):
            return self.name
    


    def save_place(self, object):
        with open("objects.json", 'w') as myFile:
            json.dump(object, myFile)
        
    def update_place(self, dictionary):
        for key, value in dictionary.items():
            for keys, values in self.__dict__.items():
                if key == keys:
                    self.__dict__[key] = value
        self.updated_at = datetime.datetime.today()
    
    def __del__(self):
        Place.place_count -= 1