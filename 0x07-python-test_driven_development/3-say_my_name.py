#!/usr/bin/python3
""" This is a say my name module """


def say_my_name(first_name, last_name=""):
    """
    Print the given first and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If `first_name` is not a string.
        TypeError: If `last_name` is not a string.

    Prints:
        The message "My name is <first_name> <last_name>". If `last_name` is not provided,
        the message will only contain the first name.

    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is', first_name, last_name)

