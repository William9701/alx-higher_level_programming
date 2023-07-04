#!/usr/bin/python3
def magic_string():
    magic_string.static_var = getattr(magic_string, 'static_var', 0) + 1
    return ', '.join(['BestSchool'] * magic_string.static_var)
