#!/usr/bin/python3
import uuid
import datetime
import json

class Review:
    review_count = 0
    feedback = {}
    def __init__(self, rating=0.0, feedback=""):
        self.id = uuid.uuid1()
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        Review.review_count_count += 1

    def __del__(self):
        Review.review_count -= 1
    
    def update(self, rating=0.0, feedback="" ):
        self.updated_at = datetime.datetime.today()
        Review.feedback.update({'rating': rating})
        Review.feedback.update({'feedback': feedback })

    def save(self, object):
        with open("objects.json", 'w') as myFile:
            json.dump(object, myFile)