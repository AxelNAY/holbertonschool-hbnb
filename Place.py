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
        self.created_at = str(datetime.datetime.today())
        self.updated_at = str(datetime.datetime.today())
        self.__id = str(uuid.uuid1())
        Place.place_count += 1



    def save(self):
        with open("Saving_files/Place.json", 'a') as myFile:
            json.dump(self.__dict__, myFile)
        
    def update(self, dictionary):
        for key, value in dictionary.items():
            for keys, values in self.__dict__.items():
                if key == keys:
                    self.__dict__[key] = value
        self.__updated_at = str(datetime.datetime.today())
    
    def __del__(self):
        Place.place_count -= 1
    

my_place = Place("HBNB", "No Wifi", "Holberton street", 0, 0, 5, 2, 150, 10, "Bordeaux")
print(my_place.__dict__)
my_place.save()