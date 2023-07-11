#!/usr/bin/python3
""" this module contains json module """

import json


def save_to_json_file(my_obj, filename):
    """ This function writes to the new module """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
