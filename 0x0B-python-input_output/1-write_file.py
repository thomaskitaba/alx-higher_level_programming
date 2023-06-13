#!/usr/bin/python3
"""
    Write a function that writes
    a string to a text file
"""


def write_file(filename="", text=""):
    """
    step-1 open the file in read mode
    step-2 Read from the opend file
    step-3 print it on the stdout
    """

    with open(filename, 'w') as f:
        return f.write(text)
