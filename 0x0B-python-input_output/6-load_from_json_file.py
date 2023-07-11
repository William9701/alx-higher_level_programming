#!/usr/bin/python3
""" this module contains json module """


import json


def load_from_json_file(filename):
    """Loads JSON data from a file and returns the corresponding object"""

    with open(filename, "r") as f:
        json_data = f.read()
        obj = json.loads(json_data)
        return obj
