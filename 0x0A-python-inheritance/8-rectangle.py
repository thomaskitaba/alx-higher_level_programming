#!/usr/bin/python3
""" Create an empty class called BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        this class inherits from BaseGeometry class
    """

    def __init__(self, width, height):
        """ instantiate with width adn height """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
