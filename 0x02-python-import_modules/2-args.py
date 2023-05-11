#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    if length == 0:
        print("{} argument.".fromat(length))
    else:
        for i in range(1, length):
            print("{} arguments".format(length))
            print("{}: {}".format(sys.argv[i]))
