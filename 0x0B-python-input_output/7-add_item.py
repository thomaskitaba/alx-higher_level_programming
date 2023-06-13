#!/usr/bin/python3
"""
    save command line arguments
    to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def load():
    pass

def add():
    pass

def save():
    pass
# if __name__ == "__main__":
args = sys.argv[1:]
file_name = "add_item.json"
json_string = save_to_json_file(args, "add_item.json")
print(type(json_string))