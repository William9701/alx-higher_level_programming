#!/usr/bin/python3
import sys
a = len(sys.argv) - 1
if a == 1:
    print("{} argument".format(a))
    print("{}: {}".format(a, sys.argv[1]))
else:
    print("{} arguments".format(a))
    if a > 0:
        for c in range(a):
            print("{}: {}".format(c + 1, sys.argv[c + 1]))
