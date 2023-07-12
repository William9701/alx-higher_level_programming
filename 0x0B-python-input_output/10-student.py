#!/usr/bin/python3
""" This is a class module that defines a student """


class Student:
    """ This class defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ This function retuns dict rep of the class Student """

        if attrs is None:
            return self.__dict__
        else :
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
