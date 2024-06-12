#!/usr/bin/python3
import uuid
import datetime
import json

class Amneties:
    
    amnetie_count = 0
    amneties_object_list = []
    def __init__(self):
        self.amneties = ["couch", "dishwasher", "fridge", "microwave", "wifi", "TV", "Balcony"]
        self.created_at = str(datetime.datetime.today())
        self.updated_at = str(datetime.datetime.today())
        self.__id = str(uuid.uuid1())
        Amneties.amnetie_count += 1
    
    @property
    def get(self):
        return self.__id
    @get.setter
    def get(self, value):
        self.__id = value
        self.updated_at = str(datetime.datetime.today())
    
    def delete(self):
        for dictionary in Amneties.amneties_object_list:
            if dictionary['_Amneties__id'] == self.__id:
                 Amneties.amneties_object_list.remove(dictionary)
        with open("Saving_files/Amneties.json", 'w') as myFile:
            json.dump(Amneties.amneties_object_list, myFile, indent=4)

    def update(self, new_amnetie=""):
        self.amneties.append(new_amnetie)
        self.__updated_at = str(datetime.datetime.today())
    
    
    def save(self):
        Amneties.amneties_object_list.append(self.__dict__)
        with open("Saving_files/Amneties.json", 'w') as myFile:
            json.dump(Amneties.amneties_object_list, myFile, indent=4)

        
    


my_amneties = Amneties()
my_amneties2 = Amneties()
my_amneties2.update("Playstation 4")
my_amneties3 = Amneties()
my_amneties3.update("Home Cinema")
print(my_amneties.__dict__)

my_amneties.save()
my_amneties2.save()
my_amneties3.save()


my_amneties.delete()
my_amneties2.delete()
my_amneties3.delete()