#!/usr/bin/python3
"""This module contains the Country class."""
import uuid
import datetime
import json


class Country:
    """Country class
    Attributes:
        country_count (int) = number of Country object
        country_object_list (int) = ist of every object's __dict__
    """
    country_object_list = []
    country_count = 0

    def __init__(self, country_name=""):
        self.country_name = country_name
        self.created_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))
        self.__id = str(uuid.uuid1())
        Country.country_count += 1

    @property
    def get(self):
        """Retrieves id"""
        return self.__id

    @get.setter
    def get(self, value):
        """Modified Id"""
        self.__id = value
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))

    def update(self, new_country=""):
        """Update country name"""
        self.country_name = new_country
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))

    def delete(self):
        """"Deletes an object in country_object_list
        by retrieving its Id"""
        for dictionary in Country.country_object_list:
            if dictionary['_Country__id'] == self.__id:
                Country.country_object_list.remove(dictionary)
        with open("Saving_files/Country.json", 'w') as myFile:
            json.dump(Country.country_object_list, myFile, indent=4)

    def save(self):
        """Saves object into list and save
        updated list in json file"""
        Country.country_object_list.append(self.__dict__)
        with open("Saving_files/Country.json", 'w') as myFile:
            json.dump(Country.country_object_list, myFile, indent=4)
