#!/usr/bin/python3
""" This i s a module that flips the "==" and the "!=" operators """


class MyInt(int):
    """ This is the class that holds them both """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
