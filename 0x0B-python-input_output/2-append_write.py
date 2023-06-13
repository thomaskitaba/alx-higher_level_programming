#!/usr/bin/python3
"""
    Write a function that writes
    a string to a text file
"""


def append_write(filename="", text=""):
    """
    step-1 open the file in read mode
    step-2 Read from the opend file
    step-3 return number of appended char
    """

    with open(filename, 'a') as f:
        return f.write(text)
