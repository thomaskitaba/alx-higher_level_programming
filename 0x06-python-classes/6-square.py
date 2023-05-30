#!/usr/bin/python3
class square:

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def size(self):
        return (self.__size)

    def size(self, value):
        if type(size) not int:
            raise TypeError("size must be an integer")
        if type(size) is int and size < 0:
            raise ValueError("size must be >= 0")
        self.__ size = value

    def area(self):
        return (self.__size ** 2)

    def position(self):
        return (self.__position)

    def position(self, position):
        if isinstance(position, tuple):
            if postion[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple of 
                2 positive integers")
        raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = tuple

    def my_print(self):
        for row in range(size()):
            for k in range(position()):
                print(" ")
            for col in range(size()):
                print("#", end='')
            print()
        print()
