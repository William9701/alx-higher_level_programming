#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return None
    elif idx > (len(my_list)):
        return my_list
    else:
        b_list = my_list.copy()
        b_list[idx] = element
        return b_list
