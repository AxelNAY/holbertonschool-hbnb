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
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id = uuid.uuid1()
        City.city_count += 1
    
    def get_city(self):
        return self.city_name
    
    def update(self, new_city):
        self.city_name = new_city 
        self.updated_at = uuid.uuid1()

    def __del__(self):
        City.city_count -= 1
    
    def save_city(self, object):
        with open("City.json", 'w') as myFile:
            json.dump(object, myFile)