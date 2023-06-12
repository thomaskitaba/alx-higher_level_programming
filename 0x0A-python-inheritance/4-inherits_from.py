#!/usr/bin/python3
"""
return True or False if obj is subclass of a_class
"""


def inherits_from(obj, a_class):
    """ check for subclass
        determine if obj is an instance
        that is inherited from a_class
        but not an instance of a_class itself.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
