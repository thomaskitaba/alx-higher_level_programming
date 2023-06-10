#!/usr/bin/python3
""" Divide matrix
Parameters:
- matrix (list): The 2D list
- div (int): The The divisor must be greater than 0.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """

    length = 0
    new_matrix = []
    col = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    for row in matrix:
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("matrix must be a "
                                "matrix (list of lists) "
                                "of integers/floats")

    if matrix is not None:
        length = len(matrix[0])
    else:
        return matrix

    for row in matrix:
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        col = []
        for val in row:
            col.append(round(val / div, 2))
        new_matrix.append(col)

    return new_matrix
