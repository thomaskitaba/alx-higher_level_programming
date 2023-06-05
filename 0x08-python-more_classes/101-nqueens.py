#!/usr/bin/python3
import sys

def set_queen(N):
    print(N ** N)

if __name__ == "__main__":
    print(sys.argv)
    """ check number of arguments """
    N = 1
    if len(sys.argv) != 2:
        print("Usage: nqueens N")

    """ check number of queens """
    try:
        N = int(sys.argv[1])
        if int(sys.argv[1]) < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    print('Create {} by {} board'.format(N, N))
    # answer = set_queen(n)