#!/usr/bin/python3
"""
Create an empty class called BaseGeometry
"""


class BaseGeometry():
    """ This is an empty class """

    def area(self):
        e = Exception("area() is not implemented")
        raise e

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
