#!/usr/bin/python3
"""
return list of available attributes and methods of an object
"""


def lookup(obj):
    """
    check for obj and return desired result

    """
    if (isinstance(obj, type) and hasattr(obj, "__dict__")):
        return (dir(obj))
