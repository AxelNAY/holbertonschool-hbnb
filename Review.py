#!/usr/bin/python3
import uuid
import datetime
import json

class Review:
    review_count = 0
    review_object_list = []
    
    def __init__(self, rating=0.0, feedback=""):
        self.__id = str(uuid.uuid1())
        self.created_at = str(datetime.datetime.today())
        self.updated_at = str(datetime.datetime.today())
        self.feedback = {rating: feedback}
        self.__id = str(uuid.uuid1())
        Review.review_count += 1

    @property
    def get(self):
        return self.__id
    @get.setter
    def get(self, value):
        self.__id = value











    def delete(self):
        Review.review_count -= 1
    
    def update(self, rating=0.0, feedback="" ):
        self.updated_at = str(datetime.datetime.today())
        self.feedback = {rating: feedback}

    def save(self):
        Review.review_object_list.append(self.__dict__)
        with open("Saving_files/Review.json", 'w') as myFile:
            json.dump(Review.review_object_list, myFile)


my_review = Review(10.0, "Best place ever")
print(my_review.__dict__)
my_review.save()