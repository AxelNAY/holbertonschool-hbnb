#!/usr/bin/python3
"""This module contains the Amneties class"""
import uuid
import datetime
import json


class Amneties:
    """Amneties class
    Attrutes:
        amnetie_count (int): number of Amneties object
        amnies_object_list (list): list of every object's __dict__
    """
    amnetie_count = 0
    amneties_object_list = []

    def __init__(self):
        """Intializes Amneties object with a common amneties list"""
        self.amneties = ["couch", "dishwasher", "fridge",
                         "microwave", "wifi", "TV", "Balcony"]
        self.created_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))
        self.__id = str(uuid.uuid1())
        Amneties.amnetie_count += 1

    @property
    def get(self):
        """Retrieves id"""
        return self.__id

    @get.setter
    def get(self, value):
        """Changes Id"""
        self.__id = value
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))

    def delete(self):
        """Deletes an object from amneties_object_list and
        updates the json file with the newly updated
        list."""
        for dictionary in Amneties.amneties_object_list:
            if dictionary['_Amneties__id'] == self.__id:
                Amneties.amneties_object_list.remove(dictionary)
        with open("Saving_files/Amneties.json", 'w') as myFile:
            json.dump(Amneties.amneties_object_list, myFile, indent=4)

    def update(self, new_amnetie=""):
        """Updates an object amneties list.
        Raises:
            ValueError: if amnetie is already in list
        """
        if new_amnetie in self.amneties:
            raise ValueError(f"{new_amnetie} is already in your list")
        self.amneties.append(new_amnetie)
        self.__updated_at = str(datetime.datetime.today().
                                replace(microsecond=0, second=0, minute=0))

    def save(self, entity):
        """Saves the current amneties_object_list
        to the json file"""
        Amneties.amneties_object_list.append(self.__dict__)
        with open("Saving_files/Amneties.json", 'w') as myFile:
            json.dump(Amneties.amneties_object_list, myFile, indent=4)
    
    def get(self):
        return self.__dict__
