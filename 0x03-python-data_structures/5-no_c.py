#!/usr/bin/env python3
def no_c(my_string):
    string=''
    for char in my_string:
        if char in ['c','C']:
            char = ''
            string += char
        string += char

    return string

