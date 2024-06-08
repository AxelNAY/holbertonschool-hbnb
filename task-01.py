#!/usr/bin/python3

import uuid
import datetime

class User:
    user_count = 0
    def __init__(self, name="", host=False, reviewer=False, email="", password="",
                first_name="", last_name=""):
        self.host = host
        self.reviewer = reviewer
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.id = uuid.uuid1()
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        User.user_count += 1
    
    def get_user(self):
        if self.host == True:
            return self.host
        elif self.reviewer == True:
            return self.reviewer
    #@classmethod
    #def add_user(self):

        #User.user_count += 1

    def __del__(self):
        User.user_count -= 1
    
    def update_user(self, dictionary):
        for key, value in dictionary.items():
            for keys, values in self.__dict__.items():
                if key == keys:
                    self.__dict__[key] = value
        self.updated_at = datetime.datetime.today()
        return self.__dict__



class Review:
    feedback_count = 0
    def __init__(self, feedback="", rating=0):
        self.feedback = feeback
        self.rating = rating
        self.id = uuid.uuid1()


    def new_feedback(self):
        feedback_count += 1

    def __del__(self):
        feedback_count -= 1

# Testing objects

my_user = User(name="Sofiane", host=True, reviewer=False, email="my_email@mail.com", password="1234")
print(my_user.get_user())
print(my_user.user_count)
print("My user attributes before:", my_user.__dict__)
print("My user object creation date", my_user.created_at)
print("----------------------------")
print("my user object updated date", my_user.updated_at)
print("Changing object attribute:")
my_user_attributes = my_user.update_user({'name': 'Axel', 'host': False, 'reviewer': True, 'email': 'my_other_email@mail.com', 'password': 'ABCD'})

print("My user attributes:", my_user_attributes)
