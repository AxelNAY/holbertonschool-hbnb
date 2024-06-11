#!/usr/bin/python3
import uuid
import datetime
import json

class Amneties:
    
    amnetie_count = 0
    def __init__(self):
        self.amneties = ["couch", "dishwasher", "fridge", "microwave", "wifi", "TV", "Balcony"]
        self.created_at = str(datetime.datetime.today())
        self.updated_at = str(datetime.datetime.today())
        self.__id = str(uuid.uuid1())
        Amneties.amnetie_count += 1
    
    def __del__(self):
        Amneties.amnetie_count -= 1
    
    @property
    def get(self):
        return self.__id
    @get.setter
    def get(self, value):
        self.__id = value
        self.updated_at = str(datetime.datetime.today())
    
    

    def update(self, new_amnetie=""):
        self.amneties.append(new_amnetie)
        self.__updated_at = str(datetime.datetime.today())
    
    
    def save(self):
         with open("Saving_files/Amneties.json", 'a') as myFile:
            json.dump(self.__dict__, myFile)

        
    


my_amneties = Amneties()
print(my_amneties.__dict__)
my_amneties.update('Ninento Switch')
print(my_amneties.__dict__)
my_amneties.save()