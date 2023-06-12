#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        b_list = my_list.copy()
        b_list[idx] = element
        return b_list
    else:
        return my_list
