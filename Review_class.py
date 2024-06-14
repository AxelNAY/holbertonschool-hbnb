#!/usr/bin/python3
"""This module contains the Review Class"""
import uuid
import datetime
import json


class Review:
    """Review class"""
    review_count = 0
    review_object_list = []

    def __init__(self, rating=0.0, feedback=""):
        """Initializes Review object"""
        self.__id = str(uuid.uuid1())
        self.created_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))
        self.feedback = {rating: feedback}
        self.__id = str(uuid.uuid1())
        Review.review_count += 1

    @property
    def get(self):
        """Retrieves Id"""
        return self.__id

    @get.setter
    def get(self, value):
        """Modified Id"""
        self.__id = value
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))

    def delete(self):
        """Deletes object"""
        for dictionary in Review.review_object_list:
            if dictionary['_Review__id'] == self.__id:
                Review.review_object_list.remove(dictionary)
        with open("Saving_files/Review.json", 'w') as myFile:
            json.dump(Review.review_object_list, myFile, indent=4)
        Review.review_count -= 1

    def update(self, rating=0.0, feedback=""):
        """Update object"""
        self.updated_at = str(datetime.datetime.today().
                              replace(microsecond=0, second=0, minute=0))
        self.feedback = {rating: feedback}

    def save(self):
        """Save object into json file"""
        Review.review_object_list.append(self.__dict__)
        with open("Saving_files/Review.json", 'w') as myFile:
            json.dump(Review.review_object_list, myFile, indent=4)
