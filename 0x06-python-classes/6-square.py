#!/usr/bin/python3
"""create square class"""


class Square:
    """attributes go here."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def position(self, value):
        if not isinstance(value, tuple) || len(value) != 2 || type(value[0]) != int || type(value[1]) != int || value[0] < 0 or value[1] < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print("")
        for row in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end='')
            for col in range(self.__size):
                print("#", end='')
            print()
