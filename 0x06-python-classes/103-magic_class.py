#!/usr/bin/python3
""" do area and circumfrance operations"""
import math


class MagicClass:
    """ do the initialization and calcutlation"""

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) != int or type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (math.pi * self.__radius * self.__radius)

    def circumference(self):
        return (2 * math.pi * self.__radius)
