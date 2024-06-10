#!/usr/bin/python3
import uuid
import datetime


class Review:
    feedback_count = 0
    def __init__(self, rating=0.0, feedback=""):
        self.id = uuid.uuid1()
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        Review.feedback_count += 1

    def __del__(self):
        Review.feedback_count -= 1
    
    def new_feedback(self, rating=0.0, feedback="" ):
        my_dict = {}
        my_dict.update({'rating': rating})
        my_dict.update({'feedback': feedback })
        return my_dict

    def update_feedback(self, rating=0.0, feedback="" ):
        self.updated_at = datetime.datetime.today()
        my_dict = {}
        my_dict.update({'rating': rating})
        my_dict.update({'feedback': feedback })
        return my_dict
