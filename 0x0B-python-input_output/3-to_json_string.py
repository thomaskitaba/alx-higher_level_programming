#!/usr/bin/python3
import json
"""
    Write a function that writes
    a string to a text file
"""


def to_json_string(my_obj):
    """
    convert object to json string
    """
    return json.dumps(my_obj)