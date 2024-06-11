#!/usr/bin/python3
import uuid
import datetime
import json

class Review:
    review_count = 0
    feedback = {}
    def __init__(self, rating=0.0, feedback=""):
        self.__id = uuid.uuid1()
        self.__created_at = datetime.datetime.today()
        self.__updated_at = datetime.datetime.today()
        Review.review_count += 1

    def __del__(self):
        Review.review_count -= 1
    
    def update(self, rating=0.0, feedback="" ):
        self.__updated_at = datetime.datetime.today()
        Review.feedback.update({'rating': rating})
        Review.feedback.update({'feedback': feedback })

    def save(self):
        my_dict_save = {}
        for key, values in self.__dict__.items():
            if key == "_Review__created_at" or key == "_Review__updated_at" or key == "_Review__id":
                my_dict_save.update({key: str(values)})
            else:
                my_dict_save.update({key: values})
        with open("Saving_files/Review.json", 'w') as myFile:
            json.dump(my_dict_save, myFile)


my_review = Review(10.0, "Best place ever")
print(my_review.__dict__)
my_review.save()