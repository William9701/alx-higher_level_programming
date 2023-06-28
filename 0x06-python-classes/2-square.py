#!/usr/bin/python3

"""
Square module
This module defines the Square class.
"""


class Square:
    """
    Square class
    This class represents a square shape.

    Args:
        size (int): The size of the square.

    Attributes:
        __size (int): The size of the square.

    """

    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer.")
        elif size < 0:
            raise ValueError("size must be >= 0.")
        self.__size = size
