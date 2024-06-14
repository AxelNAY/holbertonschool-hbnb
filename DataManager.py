#!/usr/bin/python3
import uuid
import datetime
from IPersistanceManager import IPersistenceManager
from City_class import City
from Amneties_class import Amneties
from Review_class import Review
from Country_class import Country
from Place_class import Place
from User_class import User

class DataManager(IPersistenceManager):
    #def __init__(self, entity_id, entity_type, entity):
        #self.entity_id = uuid.uuid4()
        #self.entity_type = type(entity)
        #self.entity = entity

    def save(self, entity):
        if isinstance(entity, Place):
             Place.save(entity)
        elif isinstance(entity, User):
            User.save(entity)
        elif isinstance(entity, City):
            City.save(entity)
        elif isinstance(entity, Amneties):
            Amneties.save(entity)
        elif isinstance(entity, Review):
            Review.save(entity)
        elif isinstance(entity, Country):
            Country.save(entity)
        else:
            raise TypeError("Type d'entité non pris en charge")

    def get(self, entity_id, entity_type):
        if entity_type == Place:
            Place.get(self)
        elif entity_type == User:
            return self.get_user(entity_id)
        elif entity_type == City:
            return self.get_city(entity_id)
        elif entity_type == Amneties:
            return self.get_amenities(entity_id)
        elif entity_type == Review:
            return self.get_review(entity_id)
        elif entity_type == Country:
            return self.get_country(entity_id)
        else:
            raise TypeError("Type d'entité non pris en charge")

    def update(self, entity):
        if isinstance(entity, Place):
            self.update_place(entity)
        elif isinstance(entity, User):
            self.update_user(entity)
        elif isinstance(entity, City):
            self.update_city(entity)
        elif isinstance(entity, Amneties):
            self.update_amenities(entity)
        elif isinstance(entity, Review):
            self.update_review(entity)
        elif isinstance(entity, Country):
            self.update_country(entity)
        else:
            raise TypeError("Type d'entité non pris en charge")

    def delete(self, entity_id, entity_type):
        if entity_type == Place:
            self.delete_place(entity_id)
        elif entity_type == User:
            self.delete_user(entity_id)
        elif entity_type == City:
            self.delete_city(entity_id)
        elif entity_type == Amneties:
            self.delete_amenities(entity_id)
        elif entity_type == Review:
            self.delete_review(entity_id)
        elif entity_type == Country:
            self.delete_country(entity_id)
        else:
            raise TypeError("Type d'entité non pris en charge")

my_place = Place("HBNB", "Too small", "Random street", 0, 0, 5, 5, 100, 10, "Bordeaux")
data_manager = DataManager()

data = data_manager.save(my_place)
print(data)