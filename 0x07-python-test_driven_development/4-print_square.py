#!/usr/bin/python3
""" This is a square building module """


def print_square(size):
    """
    Print a square pattern of '#' characters with the given size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
        TypeError: If `size` is a float and less than 0.

    Prints:
        The square pattern of '#' characters with the given size.

    Example:
        >>> print_square(3)
        ###
        ###
        ###

    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for _ in range(size):
        for _ in range(size):
            print('#', end='')
        print()
