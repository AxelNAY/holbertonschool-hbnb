#!/usr/bin/python3
import uuid
import datetime
import json
DataManager = __import__('DataManager').DataManager
import User from user.py
import City from City
import Amneties from amneties
import Reviews from reviews

class Place(DataManager):
    place_count = 0
    def __init__(self, name="", description="", adress="", latitude=0, longitude=0, host=None, rooms=0,
                 bathrooms=0, price_night=0, guest_capacity=0, city_name="", country_name="", first_name="", last_name=""):
        super().__init__(city_name=city_name, country_name=country_name, first_name=first_name, last_name=last_name)
        self.name = name
        self.description = description
        self.adress = adress
        self.latitude = latitude
        self.longitude = longitude
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price_night = price_night
        self.guest_capacity = guest_capacity
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id_place = uuid.uuid1()
        Place.place_count += 1

    def save_place(self, object):
        with open("objects.json", 'w') as myFile:
            json.dump(object, myFile)

    def update_place(self, name, description, address, latitude, longitude, rooms, bathrooms,
            price_night, guest_capacity, city_name, country_name, first_name, last_name):
        my_dict = {}
        self.updated_at = datetime.datetime.today()
        my_dict.update({'name': name})
        my_dict.update({'description': description})
        my_dict.update({'address': address})
        my_dict.update({'latitude': latitude})
        my_dict.update({'longitude': longitude})
        my_dict.update({'rooms': rooms})
        my_dict.update({'price_night': price_night})
        my_dict.update({'guest_capacity': guest_capacity})
        my_dict.update({'city_name': city_name})
        my_dict.update({'country_name': country_name})
        my_dict.update({'first_name': first_name})
        my_dict.update({'last_name': last_name})
        return my_dict

    def get_place(self):
        return self.name

    def __del__(self):
        Place.place_count -= 1
