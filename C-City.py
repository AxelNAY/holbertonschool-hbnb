#!/usr/bin/python3
import uuid
import datetime
import json


Country = __import__('C-Country').Country
class City(Country):
    city_object_list = []
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
        for dictionary in City.city_object_list:
            if dictionary['_City__id'] == self.__id:
                 City.city_object_list.remove(dictionary)
        with open("Saving_files/City.json", 'w') as myFile:
            json.dump(City.city_object_list, myFile, indent=4)
    
    def save(self):
        City.city_object_list.append(self.__dict__)
        with open("Saving_files/City.json", 'w') as myFile:
            json.dump(City.city_object_list, myFile, indent=4)

my_city = City("Bordeaux")
my_city2 = City("Paris")
my_city3 = City("Nice")

my_city.save()
my_city2.save()
my_city3.save()
my_city3.delete()
with open("Saving_files/City.json", 'r') as myFile:
    my_objects = json.load(myFile)
    for dictionary in my_objects:
        print(dictionary, end="\n\n")
#my_city.delete()
#my_city2.delete()





#print(my_city.__dict__)
#my_city.delete()