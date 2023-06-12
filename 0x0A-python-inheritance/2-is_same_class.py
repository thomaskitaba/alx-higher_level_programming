#!/usr/bin/python3
"""
return True or False based on the object type
"""


def is_same_class(obj, a_class):
    """ check instance of object """
    if type(obj) == a_class:
        return (True)
    return (False)
