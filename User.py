#!/usr/bin/python3
import uuid
import datetime


Review = __import__('Review').Review
Review = __import__('Review').Review
class User(Review, Amneties):
    user_count = 0 
    def __init__(self, email="", password="",
                first_name="", last_name=""):
        self.amneties = Amneties.amneties
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.id = uuid.uuid1()
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        User.user_count += 1   

    def __del__(self):
        User.user_count -= 1
    
    def update_user(self, dictionary):
        for key, value in dictionary.items():
            for keys, values in self.__dict__.items():
                if key == keys:
                    self.__dict__[key] = value
        self.updated_at = datetime.datetime.today()
        return self.__dict__
    
    def update_amneties(self, my_new_amneties=[]):
         self.updated_at = datetime.datetime.today()
         for comfort in my_new_amneties:
             self.amneties.append(comfort)
