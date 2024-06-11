#!/usr/bin/python3
import uuid
import datetime
from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    def __init__(self, entity_id, entity_type, entity):
        self.entity_id = uuid4()
        self.entity_type = entity_type
        self.entity = entity

    @abstractmethod
    def save(self, entity):
        with open("entity.json", 'w') as my_file:
            json.dump(entity, my_file)

    @abstractmethod
    def get(self, entity_id, entity_type):
        pass

    @abstractmethod
    def update(self, entity):
        return self.entity

    @abstractmethod
    def delete(self, entity_id, entity_type):
        self.entity_id -= 1
