#!/usr/bin/python3
import uuid
import datetime
import json

class Amneties:
    amneties_list = ["couch", "dishwasher", "fridge", "microwave", "wifi", "TV", "Balcony"]
    amnetie_count = 0
    def __init__(self):
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id = uuid.uuid1()
        Amneties.amnetie_count += 1
    
    def __del__(self):
        Amneties.amnetie_count -= 1
    
    def get(self):
        return Amneties.amneties_list
    

    def update(self, new_amnetie=""):
        Amneties.amneties_list.append(new_amnetie)
        self.updated_at = datetime.datetime.today()
    def save(self, object):
        with open("Amneties.json", 'w') as myFile:
            json.dump(object, myFile)