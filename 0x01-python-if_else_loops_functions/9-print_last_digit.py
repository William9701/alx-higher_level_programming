#!/usr/bin/python3
def print_last_digit(number):
    c = abs(number) % 10
    print(c, end='')
    return c
