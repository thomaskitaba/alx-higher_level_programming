#!/usr/bin/python3
"""
    save command line arguments
    to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

""" load json file convert
    json string to python object
"""

loaded_string = load_from_json_file("add_item.json")

""" add arguments to the loaded
    python object
"""

if len(loaded_string) > 0:
    args += loaded_string

"""
    save the python object to
    a json file
"""

json_string = save_to_json_file(args, "add_item.json")
# print(type(json_string))
