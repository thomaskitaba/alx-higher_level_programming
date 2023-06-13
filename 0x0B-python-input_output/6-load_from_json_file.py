#!/usr/bin/python3
"""
    convert json file to python object
"""
import json


def load_from_json_file(filename):
    """ json file to object """

    with open(filename, 'r', encoding="utf-8") as fr:
        return (json.loads(fr.read()))
