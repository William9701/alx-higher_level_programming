#!/usr/bin/python3
""" this module for wrinting into a file and retuning the number wrtten """


def append_write(filename="", text=""):
    """ This function returns number of char written """

    with open(filename, "a", encoding="UTF8") as f:
        return (f.write(text))
