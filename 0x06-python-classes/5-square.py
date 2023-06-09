#!/usr/bin/python3

"""
Square module
This module defines the Square class.
"""


class Square:
    """
    Square class
    This class represents a square shape.

    Attributes:
        _Square__size (int): The size of the square.

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
        self._Square__size = 0  # Initialize with default value
        self.size = size  # Use property setter for validation

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.

        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        if value < 0:
            raise ValueError("Size must be >= 0.")
        self._Square__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self._Square__size ** 2

    def my_print(self):
        """
        Print a square pattern based on the size attribute.

        """
        if self._Square__size == 0:
            print()
        else:
            for i in range(self._Square__size):
                for x in range(self._Square__size):
                    print("#", end='')
                print()
