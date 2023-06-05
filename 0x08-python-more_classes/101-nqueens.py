#!/usr/bin/python3
import sys

def valid_VHD(ans, row, col):
    return True
def set_queen(N):
    row = 0
    col = 1
    ans = []
    for y in range (1, N - 1):
        location = [[0, y]]
        ans.clear()
        for row in range(0, N): # we can start checking from 1
            if row == 0:
                ans.append(location[0])
                continue
            for col in range(0, N - 1):

                # check if Vertical
                if valid_VHD(ans, row, col):
                    ans.append([row, col])
                    break
        print(ans)

                # check if Horizontal
                # check if diagonal

                #if not dieagonal H  or V append to answer





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
    answer = set_queen(N)
