#!/usr/bin/python3
""" Description goes here """
Base = __import__('base').Base


class Rectangle(Base):
    """ Description for function goes here """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter for width """
        if not isinstance(value, int):  # TODO: added
            raise TypeError("{} must be an integer".format(self.__width))   # TODO: added
        if self.__width <= 0:   # TODO: added
            raise ValueError("{} must be > 0".format(self.__width)) # TODO: added
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):  # TODO: added
            raise TypeError("{} must be an integer".format(self.__height))  # TODO: added
        if self.__height <= 0:  # TODO: added
            raise ValueError("{} must be > 0".format(self.__height))    # TODO: added
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Setter for x """
        if not isinstance(value, int):  # TODO: added
            raise TypeError("{} must be an integer".format(self.__x))   # TODO: added
        if self.__x <= 0:   # TODO: added
            raise ValueError("{} must be > 0".format(self.__x)) # TODO: added
        self.__x = value

    @property
    def y(self):
        """ Setter for y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Setter for y """
        if not isinstance(value, int):  # TODO: added
            raise TypeError("{} must be an integer".format(self.__y)) # TODO: added
        if self.__y <= 0:   # TODO: added
            raise ValueError("{} must be > 0".format(self.__y)) # TODO: added
        self.__y = value
