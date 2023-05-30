#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        self.size = size

    def size(self):
        return (self.__size)

    def size(self, value):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__ size = value

    def area(self):
        return (self.__size ** 2)
