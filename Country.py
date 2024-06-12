#!/usr/bin/python3
import uuid
import datetime
import json

class Country:
    country_object_list = []
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

my_country = Country("France")
my_country2 = Country("Spain")
my_country3 = Country("Germany")
print(my_country.__dict__)
my_country.save()
my_country2.save()
my_country3.save()

my_country.delete()
my_country2.delete()
my_country3.delete()