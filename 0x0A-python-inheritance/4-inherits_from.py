#!/usr/bin/python3
"""
return True or False based on the object instance
"""


def inherits_from(obj, a_class):
    """ check instance of obj """
    if issubclass(obj, a_class):
        return (True)
    return (False)
