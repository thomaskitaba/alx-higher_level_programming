#!/usr/bin/python3
"""create square class"""


class Square:
    """attributes go here."""
    def __init__(self, size=0):
        self.size = size

    def size(self):
        return (self.__size)

    def size(self, value):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)
