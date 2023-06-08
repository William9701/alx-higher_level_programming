#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv) - 1
    if a == 1:
        print("{} argument:".format(a))
        print("{}: {}".format(a, argv[1]))
    elif a == 0:
        print("{} arguments.".format(a))
    else:
        print("{} arguments:".format(a))
        for c in range(1, a + 1):
            print("{}: {}".format(c, argv[c]))
