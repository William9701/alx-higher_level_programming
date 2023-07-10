#!/usr/bin/python3
""" This module hold a BaseGeometry class """


class BaseGeometry:
    """ This class holds a Public instance method\
            "area" and "integer_validator" """

    def area(self):
        """ defines the functions area """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ defines the int_validtor """

        if type(value) is int:
            if value <= 0:
                raise ValueError(f'{name} must be greater than 0')
            self.value = value
        else:
            raise TypeError(f'{name} must be an integer')
        if isinstance(name, str):
            self.name = name


class Rectangle(BaseGeometry):
    """ This class inherits attributs and method of the super class """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
