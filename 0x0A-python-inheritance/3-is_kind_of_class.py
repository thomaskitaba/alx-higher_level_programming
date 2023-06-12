#!/usr/bin/python3
"""
return True or False based on the object instance
"""


def is_kind_of_class(obj, a_class):
    """ check instance of obj """
    if isinstance(obj, a_class):
        return (True)
    return (False)
