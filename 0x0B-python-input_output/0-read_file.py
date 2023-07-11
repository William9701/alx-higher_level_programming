#!/usr/bin/python3
""" This module contains how to open files in python """


def read_file(filename=""):
    """ this function defines opening of a fike and priting it """
    
    with open(filename, encoding="UTF8") as f:
        r_read = f.read()
        print(r_read, end='')
