#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


    class Rectangle:
    """ def Rectangel with width and height """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return (self.height)

    @height.setter
    def width(self, value):
        self.__height = value
