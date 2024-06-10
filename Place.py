#!/usr/bin/python3
import uuid
import datetime


Amneties = __import__('Amneties').Amneties
City = __import__('City').City
class Place(Amneties, City):


    def __init__(self, name="", description="", adress="", latitude=0, longitude=0, host=None, rooms=0,
                 bathrooms=0, price_night=0, guest_capacity=0, city_name="", country_name=""):
        super().__init__(city_name=city_name, country_name=country_name)
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