#!/usr/bin/python3
"""
return True or False if obj is subclass of a_class
"""


def inherits_from(obj, a_class):
    """ check for subclass """
    if issubclass(obj, a_class):
        return (True)
    return (False)
