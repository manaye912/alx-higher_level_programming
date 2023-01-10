#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argvlength = len(sys.argv) - 1
    if argvlength == 0:
        print("0 arguments.")
    elif argvlength == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argvlength))
    for i in range(argvlength):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
