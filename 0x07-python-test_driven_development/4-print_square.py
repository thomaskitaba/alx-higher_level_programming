#!/usr/bin/python3
def print_square(size):
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
