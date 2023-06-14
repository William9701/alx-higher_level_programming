#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return 0

    can = set(my_list)
    res = 0
    for i in can:
        res += i
    return res
