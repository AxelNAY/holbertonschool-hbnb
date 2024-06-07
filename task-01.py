#!/usr/bin/python3

import uuid

class User:
    user_count = 0
    def __init__(self, host=False, reviewer=False, email="", password="",
                first_name="", last_name=""):
        self.host = host
        self.reviewer = reviewer
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
    
    def get_user(self):
        if self.host == True:
            return self.host
        elif self.reviewer == True:
            return self.reviewer
    def add_user(self):
        User.user_count += 1

    def __del__(self):
        User.user_count -= 1



