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

    def area(self):
        """ return area of rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        string = "[Rectangle] "
        string += str(self.__width) + '/' + str(self.__height)
        return string
