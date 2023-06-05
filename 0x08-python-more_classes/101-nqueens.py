#!/usr/bin/python3
import sys

def valid_VHD(ans, row, col):
    for row_ans in ans:
        # check horizontal
        if row_ans[0] == row or row_ans[1] == col:
            return False
        # check if diagonal
        if abs(row - row_ans[0]) == abs(col - row_ans[1]):
            return False
    return True

def set_queen(N):
    ans = []
    for y in range(N):
        location = [[0, y]]
        ans = [location[0]]
        for row in range(1, N):
            for col_inner in range(N):
                if valid_VHD(ans, row, col_inner):
                    ans.append([row, col_inner])
                    break
        print(ans)

if __name__ == "__main__":
    N = 1
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    set_queen(N)
