#!/usr/bin/python3
""" This is a class module that defines a student """


class Student:
    """ This class defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ This function retuns dict rep of the class Student """

        return self.__dict__
