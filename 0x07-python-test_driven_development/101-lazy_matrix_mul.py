#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ use numpy to multiply two metrixs """
    result = np.matmul(m_a, m_b)
    return(result)
