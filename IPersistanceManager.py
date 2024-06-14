#!/usr/bin/python3
import uuid
import datetime
from abc import ABC, abstractmethod
from City_class import City
from Amneties_class import Amneties
from Review_class import Review
from Country_class import Country
from Place_class import Place
from User_class import User

class IPersistenceManager(ABC):
    #def __init__(self, entity_id, entity_type, entity):
        #self.entity_id = uuid.uuid4()
        #self.entity_type = entity_type
        #self.entity = entity

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
