#!/usr/bin/python3
import uuid
import datetime
import json

class Country:
    country_list = []
    country_count = 0
    def __init__(self, country_name=""):
        self.country_name = country_name
        self.created_at = str(datetime.datetime.today())
        self.updated_at = str(datetime.datetime.today())
        self.__id = str(uuid.uuid1())
        Country.country_count += 1
    

    @property
    def get(self):
        return self.__id
    @get.setter
    def get(self, value):
        self.__id = value
        self.updated_at = str(datetime.datetime.today())
    
    def update(self, new_country=""):
        self.country_name = new_country
        self.__updated_at = str(datetime.datetime.today())
    
    def __del__(self):
        Country.country_count -= 1

    def save(self):
        with open("Saving_files/Country.json", 'w') as myFile:
            json.dump(self.__dict__, myFile)

my_country = Country("France")
print(my_country.__dict__)
my_country.save()