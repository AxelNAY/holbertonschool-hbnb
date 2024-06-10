#!/usr/bin/python3
import uuid
import datetime


class Amneties:
    amneties = ["couch", "dishwasher", "fridge", "microwave", "wifi", "TV", "Balcony"]
    def __init__(self):
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id = uuid.uuid1()   