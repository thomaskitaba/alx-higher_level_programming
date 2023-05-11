#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("{} argument.".fromat(length))
    else:
        for i in range(1, length + 1):
            print("{} arguments".format(length))
            print("{}: {}".format(sys.argv[i]))
