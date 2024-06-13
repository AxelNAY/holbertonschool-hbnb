#!/usr/bin/python3
import uuid
import datetime
import json


class Place:
    place_count = 0
    place_object_list = []
    def __init__(self, name="", description="", adress="", latitude=0, longitude=0, rooms=0,
                 bathrooms=0, price_night=0, guest_capacity=0, city_name=""):
        self.name = name
        self.description = description
        self.adress = adress
        self.latitude = latitude
        self.longitude = longitude
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price_night = price_night
        self.guest_capacity = guest_capacity
        self.city_name = city_name
        self.created_at = str(datetime.datetime.today())
        self.updated_at = str(datetime.datetime.today())
        self.__id = str(uuid.uuid1())
        Place.place_count += 1



    def save(self):
        Place.place_object_list.append(self.__dict__)
        with open("Saving_files/Place.json", 'w') as myFile:
            json.dump(Place.place_object_list, myFile, indent=4)
        
    def update(self, dictionary):
        for key, value in dictionary.items():
            for keys, values in self.__dict__.items():
                if key == keys:
                    self.__dict__[key] = value
        self.__updated_at = str(datetime.datetime.today())
    
    def delete(self):
        for dictionary in Place.place_object_list:
            if dictionary['_Place__id'] == self.__id:
                 Place.place_object_list.remove(dictionary)
        with open("Saving_files/Place.json", 'w') as myFile:
            json.dump(Place.place_object_list, myFile, indent=4)

        Place.place_count -= 1
    

my_place = Place("HBNB", "Small apartment", "Holberton street", 0, 0, 5, 2, 150, 10, "Bordeaux")
my_place2 = Place("BX_HOTEL", "Hotel situated near Garonne", "A random street in Bordeaux", 0, 0, 5, 2, 150, 10, "Bordeaux")
my_place3 = Place("FRANCE_HOTEL", "Hotel built next to Eiffel Tower", "A random street in France", 0, 0, 5, 2, 150, 10, "Paris")
print(my_place.__dict__)
my_place.save()
my_place2.save()
my_place3.save()

my_place2.delete()