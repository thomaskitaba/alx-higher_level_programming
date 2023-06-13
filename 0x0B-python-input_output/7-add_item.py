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
f = open("add_item.json", 'w')
f.close()

loaded_string = load_from_json_file("add_item.json")

""" add arguments to the loaded
    python object
"""
print(loaded_string)
args += loaded_string

"""
    save the python object to
    a json file
"""

json_string = save_to_json_file(args, "add_item.json")
print(json_string)
