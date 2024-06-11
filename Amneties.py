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
        self.__amneties.append(new_amnetie)
        self.__updated_at = datetime.datetime.today()
    def save(self):
        my_dict_save = {}
        for key, values in self.__dict__.items():
            if key == "_Amneties__created_at" or key == "_Amneties__updated_at" or key == "_Amneties__id":
                my_dict_save.update({key: str(values)})
            else:
                my_dict_save.update({key: values})

        with open("Saving_files/Amneties.json", 'w') as myFile:
            json.dump(my_dict_save, myFile)

        
    


my_amneties = Amneties()
print(my_amneties.__dict__)
print(my_amneties.get)
my_amneties.update("Nintendo switch")
print(my_amneties.get)

my_amneties.save()