#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    can = list(a_dictionary.keys())
    can.sort()
    for i in can:
        print("{}: {}".format(i, a_dictionary.get(i)))
