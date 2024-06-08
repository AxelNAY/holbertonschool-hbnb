#!/usr/bin/python3

import uuid
import datetime



class Country:
    def __init__(self, country_name=""):
        self.country_name = country_name

class City(Country):
    def __init__(self, city_name=""):
        self.city_name = city_name
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id = uuid.uuid1()

        







class Place(City, Country):


    def __init__(self, description="", adress="", latitude=0, longitude=0, rooms=0,
                 bathrooms=0, price_night=0, guest_capacity=0):
        self.description = description
        self.adress = adress
        self.latitude = latitude
        self.longitude = longitude
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price_night = price_night
        self.guest_capacity = guest_capacity
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id = uuid.uuid1()

class Amneties(Place):
    def __init__(self, amneties_dict={}):
        self.dict = amneties_dict
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id = uuid.uuid1()
    
    def add_amneties(self, dict={}):
         for key, value in dict.items(): 
            self.dict.update({key: value})


class Review(Place):
    feedback_count = 0
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
        Review.feedback_count += 1











class User(Review):
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








    def __del__(self):
        Review.feedback_count -= 1
    
    def new_feedback(self, ratings=0.0, feedback="" ):
        my_dict = {}
        my_dict.update({'rating': ratings})
        my_dict.update({'feedback': feedback })
        return my_dict

    def update_feedback(self, ratings=0.0, feedback="" ):
        self.updated_at = datetime.datetime.today()
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