#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for col in matrix:
        result.append(list(map(lambda x: x ** 2, col)))
    return (result)
    # result = list(map(lambda row : list(map(lambda x : x **x, row)), matrix))
