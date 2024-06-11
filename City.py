#!/usr/bin/python3
import uuid
import datetime
import json


Country = __import__('Country').Country
class City(Country):
    city_list = []
    city_count = 0
    def __init__(self, city_name=""):
        self.__city_name = city_name
        self.__created_at = datetime.datetime.today()
        self.__updated_at = datetime.datetime.today()
        self.__id = uuid.uuid1()
        City.city_count += 1
    @property
    def get(self):
        return self.__city_name
    @get.setter
    def get(self, city_name=""):
        self.__city_name = city_name
    


    @property
    def get_update_date(self):
        return self.__updated_at
    
    @property
    def get_creation_date(self):
        return self.__created_at
    
    @property
    def get_id(self):
        return self.__id
    
    def update(self, new_city):
        self.city_name = new_city 
        self.updated_at = uuid.uuid1()

    def __del__(self):
        City.city_count -= 1
    
    def save(self):
        my_dict_save = {}
        for key, values in self.__dict__.items():
            if key == "_City__created_at" or key == "_City__updated_at" or key == "_City__id":
                my_dict_save.update({key: str(values)})
            else:
                my_dict_save.update({key: values})

        with open("Saving_files/City.json", 'w') as myFile:
            json.dump(my_dict_save, myFile)

my_city = City("Bordeaux")
my_city.save()