#!/usr/bin/python3
if __name__ == "__main__":
    import sys

     argvlength = len(sys.argv)
     if argvlength == 0:
         print("0 arguments.")
     elif argvlength == 1:
         print("1 argument:")
     else:
         print("{} arguments:".format(argvlength))
     i = 1
     for argument in sys.argv:
         print("{:d}: {}".format(i, argument))
         i += 1
