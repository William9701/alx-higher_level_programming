#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        c = sorted(my_list)
        c = c[-1]
        return c
