#!/usr/bin/python3
""" append text """


def append_after(filename="", search_string="", new_string=""):
    """ search and replace with new string """
    with open(filename, 'w') as fw:
        line_read = fw.readline()
        print(line_read)
append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")