#!/usr/bin/python3
import uuid
import datetime
import IPersistenceManager from IPersistenceManager
from city import City
from amenity import Amenities
from review import Review
from country import Country
from place import Place
from user import User

class DataManager(IPersistenceManager):
    def __init__(self, entity_id, entity_type, entity):
        self.entity_id = uuid4()
        self.entity_type = entity_type
        self.entity = entity

    def save(self, entity):
        if isinstance(entity, Place):
            self.save_place(entity)
        elif isinstance(entity, User):
            self.save_user(entity)
        elif isinstance(entity, City):
            self.save_city(entity)
        elif isinstance(entity, Amenities):
            self.save_amenities(entity)
        elif isinstance(entity, Review):
            self.save_review(entity)
        elif isinstance(entity, Country):
            self.save_country(entity)
        else:
            raise TypeError("Type d'entité non pris en charge")

    def get(self, entity_id, entity_type):
        if entity_type == Place:
            return self.get_place(entity_id)
        elif entity_type == User:
            return self.get_user(entity_id)
        elif entity_type == City:
            return self.get_city(entity_id)
        elif entity_type == Amenities:
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
        elif isinstance(entity, Amenities):
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
        elif entity_type == Amenities:
            self.delete_amenities(entity_id)
        elif entity_type == Review:
            self.delete_review(entity_id)
        elif entity_type == Country:
            self.delete_country(entity_id)
        else:
            raise TypeError("Type d'entité non pris en charge")
