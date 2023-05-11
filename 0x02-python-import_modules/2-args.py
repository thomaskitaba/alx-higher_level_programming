#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("{} argument.".fromat(length))
    else:
        print("{} argument".format(length))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
