#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    a = list(map(lambda r: list(map(lambda c: c ** 2, r)), matrix))
    return (a)
