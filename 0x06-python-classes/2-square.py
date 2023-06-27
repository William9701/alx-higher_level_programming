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
    size (int): int

    Attribute:
    size (int): integer

    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer.")
        if size < 0:
            raise ValueError("Size must be >= 0.")
        self._Square__size = size
