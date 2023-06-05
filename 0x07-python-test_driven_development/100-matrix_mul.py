#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) == 0 or m_a == [] or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or m_b == [] or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    len_ma_row = len(m_a[0])
    for rows in m_a:
        if not all(isinstance(val, (int, float)) for val in rows):
            raise TypeError("m_a should contain only integers or floats")
        if len_ma_row != len(rows):
            raise TypeError("each row of m_a must be of the same size")
    len_mb_row = len(m_b[0])
    for rows in m_b:
        if not all(isinstance(val, (int, float)) for val in rows):
            raise TypeError("m_b should contain only integers or floats")
        if len_mb_row != len(rows):
            raise TypeError("each row of m_b must be of the same size")

    #TODO: If m_a and m_b can’t be multiplied: raise a ValueError exception with the message m_a and m_b can't be multiplied

    result = 0
    m_c = []
    c_value = []
    for i in range (len(m_a)):
        c_value = []
        for k in range(len(m_a[i])):
            result = 0
            for j in range(len(m_b)):
                result += m_a[i][j] * m_b[j][k]
            c_value.append(result)
        m_c.append(c_value)
    return (m_c)