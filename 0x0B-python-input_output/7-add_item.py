#!/usr/bin/python3
"""
    save command line arguments
    to a file
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

""" load json file convert
    json string to python object
"""
loaded_string = []

try:
    loaded_string = load_from_json_file("add_item.json")
except Exception:
    save_to_json_file(args, "add_item.json")
""" add arguments to the loaded
    python object
"""

for item in args:
    loaded_string.append(item)

"""
    save the python object to
    a json file
"""

json_string = save_to_json_file(loaded_string, "add_item.json")
print(json_string)
