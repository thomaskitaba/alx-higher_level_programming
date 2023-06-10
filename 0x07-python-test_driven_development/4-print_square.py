#!/usr/bin/python3
""" print_square
Parameters:
- size (int): Size of square.

"""


def print_square(size):
    """ print square of size size """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for row in range(0, size):
        for brick in range(0, size):
            print("#", end="")
        print("")
