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
        if type(value) != int and type(value) != float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def __eq__(self, other):
        """ equal to method """
        return self.area() == other.area()

    def __ne__(self, other):
        """ not equal to"""
        return self.area() != other.area()

    def __lt__(self, other):
        """ less than """
        return self.area() < other.area()

    def __le__(self, other):
        """ less or equal to """
        return self.area() <= other.area()

    def __gt__(self, other):
        """ greater or equal to"""
        return self.area() > other.area()

    def __ge__(self, other):
        """ greater or equal to"""
        return self.area() >= other.area()