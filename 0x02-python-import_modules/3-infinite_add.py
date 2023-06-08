#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv) - 1
    if a > 0:
        numbers = [int(arg) for arg in argv[1:]]
        result = sum(numbers)
        print("{}".format(result))
    else:
        print("0")
