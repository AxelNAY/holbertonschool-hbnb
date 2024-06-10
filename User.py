#!/usr/bin/python3
import uuid
import datetime
import json

class User:
    user_count = 0
    user_list = []
    def __init__(self, email="", password="",
                first_name="", last_name="", status=""):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.places_owned = []
        self.id = uuid.uuid1()
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        User.user_count += 1   

    def __del__(self):
        User.user_count -= 1
    
    def update(self, dictionary):
        for key, value in dictionary.items():
            for keys, values in self.__dict__.items():
                if key == keys:
                    self.__dict__[key] = value
        self.updated_at = datetime.datetime.today()
        return self.__dict__
    
    def get(self):
        user = f"{self.first_name}, {self.last_name}"
        return user

    def save(self, object):
        with open("User.json", 'w') as myFile:
            json.dump(object, myFile)