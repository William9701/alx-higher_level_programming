#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    can = dict(sorted(a_dictionary.items(), key=lambda x: x[0]))
    for i, v in can.items():
        print(i, ":", v)
