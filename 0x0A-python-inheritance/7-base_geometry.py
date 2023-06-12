#!/usr/bin/python3
""" Create an empty class called BaseGeometry """


class BaseGeometry:
    """ this is an empty class """
    def area(self):

        e = Exception("area() is not implemented")
        raise e

    def integer_validator(self, name, value):
        """ validate value """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
