#!/usr/bin/python3
""" pascals triangle """


def pascal_triangle(n):
    """ return numbers based on n """
    if n > 0:
        answer = []
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(answer[i - 1][j - 1] + answer[i - 1][j])
            answer.append(row)
        return (answer)
    return ([])
