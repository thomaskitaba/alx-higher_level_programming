#!/usr/bin/python3
""" print_square
Parameters:
- size (int): Size of square.

"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ use numpy to multiply two metrixs """
    result = np.matmul(m_a, m_b)
    return (result)
