#!/usr/bin/python3
""" add attribute to an object """


def add_attribute(obj, att, value):
    """ add attribute """
    if len(obj.__dict__) > 0:
        setattr(obj, att, value)
    else:
        print("can't add new attribute")
