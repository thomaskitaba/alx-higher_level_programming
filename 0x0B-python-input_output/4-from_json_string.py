#!/usr/bin/python3
"""
    Write a function that writes
    a string to a text file
"""
import json


def from_json_string(my_str):
    """
    convert object to json string
    """
    return json.parce(my_str)
