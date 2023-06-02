#!/usr/bin/python3
def matrix_divided(matrix, div):
    length = 0
    new_matrix = []
    col = []
    if not isinstance(matrix, list) and \
      [not isinstance(row, list) for row in matrix]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if matrix is not None:
        length = len(matrix[0])
    else:
        return matrix
    for row in matrix:
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        col = []
        for val in row:

            col.append(round(val/2, 2))
        if not None:
            new_matrix.append(col)
    print(new_matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix_divided(matrix, 2)