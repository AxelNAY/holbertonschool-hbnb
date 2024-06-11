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
        self.__status = status
        self.__places_owned = []
        self.__id = uuid.uuid1()
        self.__created_at = datetime.datetime.today()
        self.__updated_at = datetime.datetime.today()
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

    def save(self):
        my_dict_save = {}
        for key, values in self.__dict__.items():
            if key == "_User__created_at" or key == "_User__updated_at" or key == "_User__id":
                my_dict_save.update({key: str(values)})
            else:
                my_dict_save.update({key: values})
        with open("Saving_files/User.json", 'w') as myFile:
            json.dump(my_dict_save, myFile)


my_user = User("Random@", "ABCD", "Sofiane", "Slimane", "host")
print(my_user.__dict__)
my_user.save()