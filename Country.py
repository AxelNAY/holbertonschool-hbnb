#!/usr/bin/python3
import uuid
import datetime
import json

class Country:
    country_list = []
    country_count = 0
    def __init__(self, country_name=""):
        self.__country_name = country_name
        self.__created_at = datetime.datetime.today()
        self.__updated_at = datetime.datetime.today()
        self.__id = uuid.uuid1()
        Country.country_count += 1
    

    @property
    def get(self):
        return self.country_name
    @get.setter
    def get(self, new_country_name=""):
        self.__country_name = new_country_name
        self.__updated_at = datetime.datetime.today()
    
    def update(self, new_country=""):
        self.country_name = new_country
        self.__updated_at = datetime.datetime.today()
    
    def __del__(self):
        Country.country_count -= 1

    def save(self):

        my_dict_save = {}
        for key, values in self.__dict__.items():
            if key == "_Country__created_at" or key == "_Country__updated_at" or key == "_Country__id":
                my_dict_save.update({key: str(values)})
            else:
                my_dict_save.update({key: values})

        with open("Saving_files/Country.json", 'w') as myFile:
            json.dump(my_dict_save, myFile)

my_country = Country("France")
print(my_country.__dict__)
my_country.save()