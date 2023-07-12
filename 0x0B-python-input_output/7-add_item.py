#!/usr/bin/python3
""" This mosule is to load and add files """


import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_list_and_save(args):
    """ this fuction creates a script that adds all\
            arguments to a Python list, and then\
            save them to a file: """

    file_name = 'add_item.json'

    if path.exists(file_name):
        # Load existing data from file
        items = load_from_json_file(file_name)
    else:
        # Create a new list if file doesn't exist
        items = []

    # Add arguments to the list
    items.extend(args)

    # Save the updated list to the file
    save_to_json_file(items, file_name)


# Get the arguments excluding the script name
arguments = sys.argv[1:]


# Add the arguments to the list and save to JSON file
add_items_to_list_and_save(arguments)
