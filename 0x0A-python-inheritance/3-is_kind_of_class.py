#!/usr/bin/python3
""" This is a is_kinda_class module """


def is_kind_of_class(obj, a_class):
    """ This fuction chks if the obj is same as the class """

    if isinstance(obj, a_class):
        return True
    return False
