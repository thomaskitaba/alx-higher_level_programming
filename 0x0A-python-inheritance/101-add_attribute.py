#!/usr/bin/python3
""" add attribute to an object """


def add_attribute(obj, att, value):
    """ add attribute """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    raise TypeError: "can't add new attribute"
