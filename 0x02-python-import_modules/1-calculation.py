#!/usr/bin/python3
from calculator_1 import add, subtruct, multiply,divid
if __name__ == "__main__":
    a = 10
    b = 5
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, subtruct(a, b)))
print("{:d} * {:d} = {:d}".format(a, b, multiply(a, b)))
print("{:d} / {:d} = {:d}".format(a, b, divid(a, b)))
