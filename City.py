#!/usr/bin/python3
import uuid
import datetime


Country = __import__('Country').Country
class City(Country):
    def __init__(self, city_name="", country_name=""):
        super().__init__(country_name=country_name)
        self.city_name = city_name
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.id = uuid.uuid1()
