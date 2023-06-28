#!/usr/bin/python3
"""
Square module

This module defines the Square class, which represents a square shape.

"""


class Square:
    """
    Square class

    This class represents a square shape.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.

        """
        self._Square__size = 0  # Initialize with default value
        self.size = size
        self._Square__position = (0, 0)
        self.position = position

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.

        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        if value < 0:
            raise ValueError("Size must be >= 0.")
        self._Square__size = value

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns:
            tuple: The position of the square.

        """
        return self._Square__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.

        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("Position must be a tuple of 2 positive integers.")
        self._Square__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self._Square__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#' in stdout.

        """
        if self._Square__size == 0:
            print()
        else:
            for _ in range(self._Square__position[1]):
                print()
            for _ in range(self._Square__size):
                print(" " * self._Square__position[0], end="")
                print("#" * self._Square__size)
