#!/usr/bin/python3
""" matrix_mul
Parameters:
- m_a (list): 2D list matrix.
- m_b (list): 2D list matrix.

"""


def matrix_mul(m_a, m_b):
    """ matrix multiplication """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if len(m_a) == 0 or m_a == [] or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or m_b == [] or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    # Check if m_a and m_b contain only integers or floats
    for rows in m_a:
        if not all(isinstance(val, (int, float)) for val in rows):
            raise TypeError("m_a should contain only integers or floats")
    for rows in m_b:
        if not all(isinstance(val, (int, float)) for val in rows):
            raise TypeError("m_b should contain only integers or floats")

    # Check if m_a and m_b are rectangular
    len_ma_row = len(m_a[0])
    for rows in m_a:
        if len_ma_row != len(rows):
            raise TypeError("each row of m_a must be of the same size")
    len_mb_row = len(m_b[0])
    for rows in m_b:
        if len_mb_row != len(rows):
            raise TypeError("each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    m_c = []
    for i in range(len(m_a)):
        c_row = []
        for k in range(len(m_b[0])):
            result = 0
            for j in range(len(m_b)):
                result += m_a[i][j] * m_b[j][k]
            c_row.append(result)
        m_c.append(c_row)

    return m_c
