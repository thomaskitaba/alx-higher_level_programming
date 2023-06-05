#!/usr/bin/python3
import sys

def valid_VHD(ans, row, col):

    for row_ans in ans:
        # check horizontal
        if row_ans[0] == row or row_ans[1] == col:

            return False
        # check if diagornal
        if abs(row - row_ans[0]) == abs(col - row_ans[1]):
            return False

    return True
def set_queen(N):
    col = 1
    ans = []
    for y in range (1, N):
        location = [[0, y]]
        ans = []
        for row in range(0, N): # we can start checking from 1
            if row == 0:
                ans.append(location[0])
                continue
            for col in range(0, N):
                # check if Vertical

                if valid_VHD(ans, row, col):
                    ans.append([row, col])
                    break


        print(ans)

                # check if Horizontal
                # check if diagonal

                #if not dieagonal H  or V append to answer

if __name__ == "__main__":
    """ check number of arguments """
    N = 1
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    """ check number of queens """
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    set_queen(N)
