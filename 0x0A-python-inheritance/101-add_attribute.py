#!/usr/bin/python3
""" add attribute to an object """


def add_attribute(obj, att, value):
    """ add attribute """
    if not obj.__dict__  and obj is not None:
        setattr(obj, att, value)
    else:
        print("can't add new attribute")
