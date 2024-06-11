#!/usr/bin/python3
import uuid
import datetime
import json


class Place:
    place_count = 0

    def __init__(self, name="", description="", adress="", latitude=0, longitude=0, rooms=0,
                 bathrooms=0, price_night=0, guest_capacity=0, city_name=""):
        self.__name = name
        self.__description = description
        self.__adress = adress
        self.__latitude = latitude
        self.__longitude = longitude
        self.__rooms = rooms
        self.__bathrooms = bathrooms
        self.__price_night = price_night
        self.__guest_capacity = guest_capacity
        self.__city_name = city_name
        self.__created_at = datetime.datetime.today()
        self.__updated_at = datetime.datetime.today()
        self.__id = uuid.uuid1()
        Place.place_count += 1

    @property
    def get(self):
            return self.__name
    


    def save(self):
        my_dict_save = {}
        for key, values in self.__dict__.items():
            if key == "_Place__created_at" or key == "_Place__updated_at" or key == "_Place__id":
                my_dict_save.update({key: str(values)})
            else:
                my_dict_save.update({key: values})

        with open("Saving_files/Place.json", 'w') as myFile:
            json.dump(my_dict_save, myFile)
        
    def update(self, dictionary):
        for key, value in dictionary.items():
            for keys, values in self.__dict__.items():
                if key == keys:
                    self.__dict__[key] = value
        self.__updated_at = datetime.datetime.today()
    
    def __del__(self):
        Place.place_count -= 1
    

my_place = Place("HBNB", "No Wifi", "Holberton street", 0, 0, 5, 2, 150, 10, "Bordeaux")
print(my_place.__dict__)
my_place.save()