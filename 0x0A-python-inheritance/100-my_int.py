#!/usr/bin/python3
""" A class that inherits form int """


class MyInt(int):
    """ class inheriting from int """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
