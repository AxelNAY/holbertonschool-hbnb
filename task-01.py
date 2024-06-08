#!/usr/bin/python3

import uuid
import datetime



class Country:
    def __init__(self, country_name=""):
        self.country_name = country_name

class City(Country):
    def __init__(self, city_name="", country_name=""):
        super().__init__(country_name=country_name)
        self.city_name = city_name
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id = uuid.uuid1()

        

class Amneties:
    amneties = ["couch", "dishwasher", "fridge", "microwave", "wifi", "TV", "Balcony"]
    def __init__(self):
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id = uuid.uuid1()   
    
             
             
             
              
            


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



class Place(Amneties, City):


    def __init__(self, name="", description="", adress="", latitude=0, longitude=0, host=None, rooms=0,
                 bathrooms=0, price_night=0, guest_capacity=0):
        #super().__init__(amneties=["couch", "dishwasher", "fridge", "microwave", "wifi", "TV", "Balcony"])
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
             

class Host(User, Place):
    def __init__(self, email="", password="", first_name="", last_name=""):
        super().__init__(email, password, first_name, last_name)
        self.places_owned = []
    def add_places(self, host):
        self.places_owned.append(host)


class Commenter(Host):
    def __init__(self, email="", password="", first_name="", last_name=""):
        super().__init__(email, password, first_name, last_name)




    
















# Testing objects
#1. Testing assignement of places to host
my_host = Host(email="my_mail@mail.mail", password="ABCD", first_name="Sofiane", last_name="Slimane")
my_place = Place("HBNB", "Appartment", "5 random street", 0.0, 0.0, my_host, 5, 2, 150, 10)
my_host.add_places(my_place.name)
print(my_host.places_owned)
print(my_place.host)

#2. Testing user adding new amneties
print("My host amneties before: ", my_host.amneties)
my_host.update_amneties(["Phone", "Parking"])
print("My host amneties after: ", my_host.amneties)

#3 Testing user writing reviews
print("My host's review: ", my_host.new_feedback(5.5, "The place has no wifi"))

#4 Testing if created_at/updated_at attributes are created
new_user = User(first_name="Sofiane")
print(new_user.created_at)
print(new_user.first_name)
new_user.update_user({'first_name': 'Joel'})
print(new_user.first_name)
print(new_user.updated_at)

#5 testing relationships between classes
Bordeaux = City("Bordeaux", "France")

print(Bordeaux.country_name)
