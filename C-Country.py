#!/usr/bin/python3
import uuid
import datetime
import json

class Country:
    country_object_list = []
    country_count = 0
    def __init__(self, country_name=""):
        self.country_name = country_name
        self.created_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
        self.__id = str(uuid.uuid1())
        Country.country_count += 1
    

    @property
    def get(self):
        return self.__id
    @get.setter
    def get(self, value):
        self.__id = value
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
    
    def update(self, new_country=""):
        self.country_name = new_country
        self.__updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
    
    def delete(self):
        for dictionary in Country.country_object_list:
            if dictionary['_Country__id'] == self.__id:
                 Country.country_object_list.remove(dictionary)
        with open("Saving_files/Country.json", 'w') as myFile:
            json.dump(Country.country_object_list, myFile, indent=4)

    def save(self):
        Country.country_object_list.append(self.__dict__)
        with open("Saving_files/Country.json", 'w') as myFile:
            json.dump(Country.country_object_list, myFile, indent=4)

