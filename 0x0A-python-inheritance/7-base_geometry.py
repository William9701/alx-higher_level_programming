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
