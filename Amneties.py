#!/usr/bin/python3
import uuid
import datetime
import json

class Amneties:
    
    amnetie_count = 0
    def __init__(self):
        self.__amneties = ["couch", "dishwasher", "fridge", "microwave", "wifi", "TV", "Balcony"]
        self.__created_at = datetime.datetime.today()
        self.__updated_at = datetime.datetime.today()
        self.__id = uuid.uuid1()
        Amneties.amnetie_count += 1
    
    def __del__(self):
        Amneties.amnetie_count -= 1
    @property
    def get(self):
        return self.__amneties
    @get.setter
    def get(self, amnetie=""):
        self.__amneties.append(amnetie)
        self.__updated_at = datetime.datetime.today()

    def update(self, new_amnetie=""):
        Amneties.amneties_list.append(new_amnetie)
        self.updated_at = datetime.datetime.today()
    def save(self, object):
        with open("Amneties.json", 'w') as myFile:
            json.dump(object, myFile)