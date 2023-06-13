#!/usr/bin/python3
"""
    read text file and print to stdout
"""


def read_file(filename=""):
    """
    step-1 open the file in read mode
    step-2 Read from the opend file
    step-3 print it on the stdout
    """
    with open(filename, 'r') as f:
        my_file = f.read()
        print(my_file, end='')
