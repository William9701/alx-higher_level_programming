#!/usr/bin/python3
""" This is an inherit from module """


def inherits_from(obj, a_class):
    """ This fuctions returns True if the object \
            is an instance of a class that inherited \
            (directly or indirectly) from the \
            specified class ; otherwise False. """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
