#!/usr/bin/python3

import uuid
import datetime

class User:
    user_count = 0
    def __init__(self, status="", email="", password="",
                first_name="", last_name=""):
        self.status = status
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.id = uuid.uuid1()
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        User.user_count += 1
    
    def get_user(self):
            return self.status
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
    def __init__(self, status="", email="", password="",
                first_name="", last_name=""):
        self.status = status
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.id = uuid.uuid1()
        Review.feedback_count += 1




    def __del__(self):
        Review.feedback_count -= 1
    
    def new_feedback(self, ratings=0.0, feedback="" ):
        my_dict = {}
        my_dict.update({'rating': ratings})
        my_dict.update({'feedback': feedback })
        return my_dict

# Testing objects

my_user = User(status="reviewer", email="my_email@mail.com", password="1234", first_name="Sofiane", last_name="Slimane")
print(my_user.get_user())
print(my_user.user_count)
print("My user attributes before:", my_user.__dict__)
print("My user object creation date", my_user.created_at)
print("----------------------------")
print("my user object updated date", my_user.updated_at)
print("Changing object attribute:")
my_user_attributes = my_user.update_user({'status': 'host', 'email': 'my_other_email@mail.com', 'password': 'ABCD', 'first_name': 'Optimus', 'last_name': 'Prime'})

print("My user attributes:", my_user_attributes)

print("----------------------")
print("Creating my review:")
my_review = Review(status="host", email="another_email@mail.com", password="...", first_name="Bradd", last_name="Pitt")
print("Review from {}:".format(my_review.first_name), my_review.new_feedback(5.2, "The place had no wifi."))
print(my_review.first_name)
print(my_review.id)