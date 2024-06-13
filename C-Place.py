#!/usr/bin/python3
"""This module contains the Place class"""
import uuid
import datetime
import json


class Place:
    """Place class
    Attributes:
        place_count (int) = number of Place object
        place_object_list (int) = ist of every object's __dict__
    """
    place_count = 0
    place_object_list = []

    def __init__(self, name="", description="", adress="", latitude=0,
                 longitude=0, rooms=0, bathrooms=0, price_night=0,
                 guest_capacity=0, city_name=""):
        """Initializes Place object"""
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
        self.created_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))
        self.__id = str(uuid.uuid1())
        Place.place_count += 1

    def save(self):
        """Saves the current place_object_list
        to the json file"""
        Place.place_object_list.append(self.__dict__)
        with open("Saving_files/Place.json", 'w') as myFile:
            json.dump(Place.place_object_list, myFile, indent=4)

    def update(self, dictionary):
        """Updates an object's attributes"""
        for key, value in dictionary.items():
            for keys, values in self.__dict__.items():
                if key == keys:
                    self.__dict__[key] = value
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))

    def delete(self):
        """Deletes an object from place_object_list and
        updates the json file with the newly updated
        list."""
        for dictionary in Place.place_object_list:
            if dictionary['_Place__id'] == self.__id:
                Place.place_object_list.remove(dictionary)
        with open("Saving_files/Place.json", 'w') as myFile:
            json.dump(Place.place_object_list, myFile, indent=4)

        Place.place_count -= 1
