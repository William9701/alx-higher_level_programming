#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c = c if ord(c) < 97 or ord(c) > 122 else chr(ord(c) - 32)
        print("{}".format(c), end='')
    print()
