#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        self.size = size

    def size(self):
        return (self.__size)

    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__ size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        for row in range(size()):
            for col in range(size()):
                print("#", end='')
            print()
        print()
