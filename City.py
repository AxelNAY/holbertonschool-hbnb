#!/usr/bin/python3
import uuid
import datetime
import json


Country = __import__('Country').Country
class City(Country):
    city_list = []
    city_count = 0
    def __init__(self, city_name=""):
        self.city_name = city_name
        self.created_at = str(datetime.datetime.today())
        self.updated_at = str(datetime.datetime.today())
        self.__id = str(uuid.uuid1())
        City.city_count += 1
    




    @property
    def get(self):
        return self.__id
    @get.setter
    def get(self, value):
        self.__id = value
    

    
























    def update(self, new_city):
        self.city_name = new_city 
        self.updated_at = str(uuid.uuid1())

    def delete(self):
        with open("Saving_files/City.json", 'r+') as myFile:
            for line in myFile:
                print(line)
                for dictionary in json.loads(line):
                    for key in dictionary:
                        if key == "_City__city_name":
                            pass
                            

        #City.city_count -= 1
    
    def save(self):
        with open("Saving_files/City.json", 'a') as myFile:
            json.dump(self.__dict__, myFile)

my_city = City("Bordeaux")
print(my_city.__dict__)
my_city.save()
#my_city.delete()