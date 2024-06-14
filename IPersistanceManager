#!/usr/bin/python3
import uuid
import datetime
from abc import ABC, abstractmethod
from city import City
from amenity import Amenities
from review import Review
from country import Country
from place import Place
from user import User

class IPersistenceManager(ABC):
    def __init__(self, entity_id, entity_type, entity):
        self.entity_id = uuid4()
        self.entity_type = entity_type
        self.entity = entity

    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        pass
