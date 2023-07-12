#!/usr/bin/python3
""" This module retuns a dict representation """


import json


def class_to_json(obj):
    """ This retuns any type of file passed to it """

    return obj.__dict__
