#!/usr/bin/python3
import uuid
import datetime
import json

class User:
    user_count = 0
    user_object_list = []
    def __init__(self, email="", password="",
                first_name="", last_name="", status=""):
        for dictionary in User.user_object_list:
            if email in dictionary['_User__email'] and email != "":
                raise ValueError(f'{email} is already used')
        if len(email) == 0:
            raise ValueError('Valid email is recquired')
        elif type(password) is not str:
            raise ValueError("Password must be a string")
        elif len(password) < 8:
            raise ValueError('Password should contain at least 8 characters')
        elif len(password) > 128:
            raise ValueError('Passsword must not exceed 128 characters')
        elif first_name == "" or last_name == "":
            raise ValueError("First name or last name must be a valid string")
        elif status != "host" and status != "commenter":
            raise ValueError('Choose a valid status (host or commenter)') 
        self.__email = email
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name
        self.status = status
        self.__places_owned = []
        self.__id = str(uuid.uuid1())
        self.created_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
        User.user_count += 1   
        User.user_object_list.append(self.__dict__)

    @property
    def get(self):
        return self.__email
    @get.setter
    def get(self, value):
        self.__email = value
    
    @property
    def get(self):
        return self.__password
    @get.setter
    def get(self, value):
        self.__password = value
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))


    @property
    def get(self):
        return self.__first_name
    @get.setter
    def get(self, value):
        self.__first_name = value
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))

    @property
    def get(self):
        return self.__last_name
    @get.setter
    def get(self, value):
        self.__last_name = value
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))

    @property
    def get(self):
        return self.__places_owned
    @get.setter
    def get(self, value):
        self.__places_owned = value
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
    @property
    def get(self):
        return self.__id
    @get.setter
    def get(self, value):
        self.__id = value
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def delete(self):
        for dictionary in User.user_object_list:
            if dictionary['_User__id'] == self.__id:
                 User.user_object_list.remove(dictionary)
        with open("Saving_files/User.json", 'w') as myFile:
            json.dump(User.user_object_list, myFile, indent=4)

        User.user_count -= 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def update(self, dictionary):
        for key, value in dictionary.items():
            for keys, values in self.__dict__.items():
                if key == keys:
                    self.__dict__[key] = value
        self.updated_at = str(datetime.datetime.today().replace(microsecond=0, second=0, minute=0))
        return self.__dict__
    

    def save(self):
        User.user_object_list.append(self.__dict__)
        with open("Saving_files/User.json", 'w') as myFile:
            json.dump(User.user_object_list, myFile, indent=4)


my_user = User("my_mail@mail.com", "ABCDeesgege", "Ronald", "Slimane", "host")
my_user2 = User("m_mail@mail.com", "1234gezgezgege", "Luffy", "Monkey.D", "host")
my_user6 = User("Bruno@mail.com", "Uptownfunk2014", "Bruno", "Mars", "singer")
#print(User.user_b
#my_user2.save()
#my_user3.save()

#with open("Saving_files/User.json", 'r') as myFile:
    #my_dict = json.load(myFile)
    #print(my_dict)
    #rint(type(my_dict))
#with open("Saving_files/User.json", 'r') as myFile:
    #for objects in myFile:
        #print(objects)
        #print(type(objects))

#my_user2.delete()
#my_user3.delete()
#my_user.delete()