#!/usr/bin/python3
"""
    Write a function that writes
    a string to a text file
"""
import json


def to_json_string(my_obj):
    """
    convert object to json string
    """
    return json.dumps(my_obj)
