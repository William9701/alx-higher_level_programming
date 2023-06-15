#!/usr/bin/python3
def common_elements(set_1, set_2):
    if len(set_1) != 0 and len(set_2) != 0:
        return (set_1 & set_2)
    else:
        return ()
