#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul#import the functions (add,sub,div,mul) from a file calculator_1
    a = 10#define a variable 'a' and give him a value 10
    b = 5#define a variable 'b' and give him a value 5
    print('{} + {} = {}'.format(a, b, add(a, b)))
    print('{} - {} = {}'.format(a, b, sub(a, b)))
    print('{} * {} = {}'.format(a, b, mul(a, b)))
    print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
