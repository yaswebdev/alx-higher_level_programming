#!/usr/bin/python3
def uppercase(s):
    result = ''
    for c in s:
        if 'a' <= c <= 'z':  # Check if the character is lowercase
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
