#!/usr/bin/python3
"""
return list of available attributes and methods of an object
"""


def lookup(obj):
    if (isinstance(obj, type) and hasattr(obj, "__dict__")):
        return (dir(obj))