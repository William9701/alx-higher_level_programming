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

    def __str__(self):
        return f'[Rectangle] {self.__width}/{self.__height}'

    def area(self):
        """ This function returns the area of the rectangle """

        result = self.__width * self.__height
        return result


class Square(Rectangle):
    """ This is a Square class that has also inherited\
            the rectangular class too """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
