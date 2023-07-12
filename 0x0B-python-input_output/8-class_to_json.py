#!/usr/bin/python3
""" This module retuns a dict representation """


import json


def class_to_json(obj):
    """ This retuns any type of file passed to it """

    if isinstance(obj, (str, int, bool)):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {class_to_json(key): class_to_json(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        return {class_to_json(key): class_to_json(value) for key, value in obj.__dict__.items()}
    else:
        raise TypeError("Object type not supported for JSON serialization.")
