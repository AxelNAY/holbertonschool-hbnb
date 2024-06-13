#!/usr/bin/python3
import uuid
import datetime
import json

class Review:
    review_count = 0
    review_object_list = []
    
    def __init__(self, rating=0.0, feedback=""):
        self.__id = str(uuid.uuid1())
        self.created_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
        self.feedback = {rating: feedback}
        self.__id = str(uuid.uuid1())
        Review.review_count += 1

    @property
    def get(self):
        return self.__id
    @get.setter
    def get(self, value):
        self.__id = value
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))











    def delete(self):
        for dictionary in Review.review_object_list:
            if dictionary['_Review__id'] == self.__id:
                 Review.review_object_list.remove(dictionary)
        with open("Saving_files/Review.json", 'w') as myFile:
            json.dump(Review.review_object_list, myFile, indent=4)
        Review.review_count -= 1
    
    def update(self, rating=0.0, feedback="" ):
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
        self.feedback = {rating: feedback}

    def save(self):
        Review.review_object_list.append(self.__dict__)
        with open("Saving_files/Review.json", 'w') as myFile:
            json.dump(Review.review_object_list, myFile, indent=4)


my_review = Review(10.0, "Best place ever")
my_review2 = Review(5.0, "Not bad")
my_review3 = Review(0.0, "Never coming back")
print(my_review.__dict__)
my_review.save()
my_review2.save()
my_review3.save()

my_review2.delete()
my_review.delete()
my_review3.delete()