#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list
    mep = my_list.copy()
    for index, value in enumerate(mep):
        if value == search:
            mep[index] = replace
    return mep
