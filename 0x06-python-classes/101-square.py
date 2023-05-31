#!/usr/bin/python3
"""create square class"""


class Square:
    """attributes go here."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.__position = position

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

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
          not all(isinstance(num, int) for num in value) or \
          not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for row in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end='')
            for col in range(self.__size):
                print("#", end='')
            print()

    def __str__(self):
        """ print instance of a class """
        if self.__size == 0:
            return ""
        temp_str = ""
        for j in range(0, self.__position[1]):
            temp_str += "\n"
        for row in range(self.__size):
            for k in range(self.__position[0]):
                temp_str += " "
            for col in range(self.__size):
                temp_str += "#"
            temp_str += "\n"
        return (temp_str)
