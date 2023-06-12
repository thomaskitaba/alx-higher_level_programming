#!/usr/bin/python3
""" Create an squate class that inherits
    from the Rectangle class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ create square instances """

    def __init__(self, size):
        """ instantiate size """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
