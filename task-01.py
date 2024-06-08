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

        

class Amneties:
    amneties_list = ["couch", "dishwasher", "fridge",
                     "microwave", "wifi", "TV", "Balcony"]
    def __init__(self):
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.perso_amneties_list = Amneties.amneties_list
        self.id = uuid.uuid1()
    
    def update_amneties(self, my_list=[]):
         self.updated_at = datetime.datetime.today()
         for amneties in my_list:
             self.perso_amneties_list.append(amneties) 
            


class Review:
    feedback_count = 0
    def __init__(self, rating=0.0, feedback=""):
        self.id = uuid.uuid1()
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        Review.feedback_count += 1

    def __del__(self):
        Review.feedback_count -= 1
    
    def new_feedback(self, rating=0.0, feedback="" ):
        my_dict = {}
        my_dict.update({'rating': rating})
        my_dict.update({'feedback': feedback })
        return my_dict

    def update_feedback(self, rating=0.0, feedback="" ):
        self.updated_at = datetime.datetime.today()
        my_dict = {}
        my_dict.update({'rating': rating})
        my_dict.update({'feedback': feedback })
        return my_dict



class Place(City, Review):


    def __init__(self, name="", description="", adress="", latitude=0, longitude=0, host=[None], rooms=0,
                 bathrooms=0, price_night=0, guest_capacity=0):
        self.name = name
        self.description = description
        self.adress = adress
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price_night = price_night
        self.guest_capacity = guest_capacity
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id = uuid.uuid1()




    











class User(Review, Place, Amneties):
    user_count = 0
    def __init__(self, email="", password="",
                first_name="", last_name=""):

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


class Host(User, Place):
    def __init__(self, email="", password="", first_name="", last_name="", places_owned=[]):
        super().__init__(email, password, first_name, last_name)
        self.places_owned = places_owned
class Commenter(Host):
    pass




    
















# Testing objects

my_host = Host(email="my_mail@mail.mail", password="ABCD", first_name="Sofiane", last_name="Slimane")
my_user.