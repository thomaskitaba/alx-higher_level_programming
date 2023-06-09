#!/usr/bin/python3
""" add integers
Parameters:
- a (int or float): The first number.
- b (int or float, optional): The second number. Defaults to 98.
"""


def add_integer(a, b=98):
    """ function that adds two numbers """
    result = 0
    if a is None:
        raise Exception("a must be an integer")
    if a is None and b is None:
        raise TypeError("a must be an integer")
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    else:
        try:
            a = int(a)
        except Exception as e:
            raise OverflowError("float Overflow") from e
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        try:
            b = int(b)
        except Exception as e:
            raise OverflowError("float Overflow") from e
    result = a + b
    return (result)
