#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv) - 1
    if a == 1:
        print("{} argument".format(a))
        print("{}: {}".format(a, argv[1]))
    else:
        print("{} arguments".format(a))
        if a > 0:
            for c in range(a):
                print("{}: {}".format(c + 1, argv[c + 1]))
