#!/usr/bin/python3
"""This module contains the City subclass"""
import uuid
import datetime
import json


Country = __import__('Country_class').Country


class City(Country):
    """City subclass"""
    city_object_list = []
    city_count = 0

    def __init__(self, city_name=""):
        self.city_name = city_name
        self.created_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))
        self.__id = str(uuid.uuid1())
        City.city_count += 1

    @property
    def get(self):
        """Retrieves Id"""
        return self.__id

    @get.setter
    def get(self, value):
        """Modify Id"""
        self.__id = value

    def update(self, new_city):
        """Update object"""
        self.city_name = new_city
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))

    def delete(self):
        """Delete object"""
        for dictionary in City.city_object_list:
            if dictionary['_City__id'] == self.__id:
                City.city_object_list.remove(dictionary)
        with open("Saving_files/City.json", 'w') as myFile:
            json.dump(City.city_object_list, myFile, indent=4)

    def save(self):
        """Save object"""
        City.city_object_list.append(self.__dict__)
        with open("Saving_files/City.json", 'w') as myFile:
            json.dump(City.city_object_list, myFile, indent=4)
