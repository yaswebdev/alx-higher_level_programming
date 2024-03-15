#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 arguments:")
    else:
        print('{} arguments:'.format(argc))
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
