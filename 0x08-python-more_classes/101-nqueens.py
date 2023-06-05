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

    def backtrack(row):
        if row == N:
            print_solution(ans)
            return
        for col in range(N):
            if valid_VHD(ans, row, col):
                ans.append([row, col])
                backtrack(row + 1)
                ans.pop()

    backtrack(0)


def print_solution(ans):
    for queen in ans:
        print(f"[{queen[0]}, {queen[1]}]", end=" ")
    print()


if __name__ == "__main__":
    """ check number of arguments """
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
