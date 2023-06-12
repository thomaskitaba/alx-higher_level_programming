#!/usr/bin/python3
""" Create an squate class that inherits
    from the Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """ create square instances """

    def __init__(self, size):
        """ instantiate size """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ calculate area """
        retrun (self.__size * self.__size)
