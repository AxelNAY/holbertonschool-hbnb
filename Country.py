#!/usr/bin/python3
import uuid
import datetime
import json

class Country:
    country_list = []
    country_count = 0
    def __init__(self, country_name=""):
        self.country_name = country_name
        Country.country_count += 1
    

    
    def get_country(self):
        return self.country_name
    
    def update_country(self, new_country=""):
        self.country_name = new_country
    
    def __del__(self):
        Country.country_count -= 1

    def save_country(self, object):
        with open("objects.json", 'w') as myFile:
            json.dump(object, myFile)