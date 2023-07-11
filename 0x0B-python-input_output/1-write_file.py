#!/usr/bin/python3
""" this module for wrinting into a file and retuning the number wrtten """


def write_file(filename="", text=""):
    """ This function returns number of char written """

    with open(filename, "w", encoding="UTF8") as f:
        f.write(text)
        return f.tell()
