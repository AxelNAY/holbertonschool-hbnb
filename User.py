#!/usr/bin/python3
import uuid
import datetime
import json

class User:
    user_count = 0
    user_list = []
    def __init__(self, email="", password="",
                first_name="", last_name="", status=""):
        self.__email = email
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name
        self.status = status
        self.__places_owned = []
        self.__id = str(uuid.uuid1())
        self.created_at = str(datetime.datetime.today())
        self.updated_at = str(datetime.datetime.today())
        User.user_count += 1   


    @property
    def get(self):
        return self.__email
    @get.setter
    def get(self, value):
        self.__email = value
    
    @property
    def get(self):
        return self.__password
    @get.setter
    def get(self, value):
        self.__password = value
        self.updated_at = str(datetime.datetime.today())


    @property
    def get(self):
        return self.__first_name
    @get.setter
    def get(self, value):
        self.__first_name = value
        self.updated_at = str(datetime.datetime.today())

    @property
    def get(self):
        return self.__last_name
    @get.setter
    def get(self, value):
        self.__last_name = value
        self.updated_at = str(datetime.datetime.today())

    @property
    def get(self):
        return self.__places_owned
    @get.setter
    def get(self, value):
        self.__places_owned = value
        self.updated_at = str(datetime.datetime.today())
    @property
    def get(self):
        return self.__id
    @get.setter
    def get(self, value):
        self.__id = value
        self.updated_at = str(datetime.datetime.today())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def delete(self):
        User.user_count -= 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def update(self, dictionary):
        for key, value in dictionary.items():
            for keys, values in self.__dict__.items():
                if key == keys:
                    self.__dict__[key] = value
        self.updated_at = datetime.datetime.today()
        return self.__dict__
    

    def save(self):
        with open("Saving_files/User.json", 'a') as myFile:
            json.dump(self.__dict__, myFile)


my_user = User("Random@", "ABCD", "Ronald", "Slimane", "host")
print(my_user.__dict__)
my_user.save()