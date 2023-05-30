#!/usr/bin/python3
"""create square class"""


class Square:
    """attributes go here."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        for row in range(self.__size):
            for col in range(self.__size):
                print("#", end='')
            print()
        print()
