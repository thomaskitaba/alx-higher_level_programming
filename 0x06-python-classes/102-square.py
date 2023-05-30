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

    def equal_to(self, second):
        return self.area() == second.area()
    def less_than(self, second):
        return self.area() == second.area()
    def less_than_equal_to(self, second):
        return self.area() == second.area()
    def grater_than(self, second):
        return self.area() == second.area()
    def grater_than_equal(self, second):
        return self.area() == second.area()
    def equal(self, second):
        return self.area() == second.area()
    def equal(self, second):
        return self.area() == second.area()