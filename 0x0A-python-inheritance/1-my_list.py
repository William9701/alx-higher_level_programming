#!/usr/bin/python3
""" This module contains my_list class """


class MyList(list):
    """ This class takes a list and returns a sorted list instead"""

    def __init__(self, num=[]):
        if all(isinstance(x, int) for x in num):
            super().__init__(num)
        else:
            raise TypeError("All elements of the list must be integers.")

    def print_sorted(self):
        """ this function prints the sorted list to the output """

        sorted_list = sorted(self)
        print(sorted_list)
