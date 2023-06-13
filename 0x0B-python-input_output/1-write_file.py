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
    with open(filename, 'r', encoding='utf-8') as fr:
        with open(text, 'w', encoding='utf-8') as fw:
            fr_read = fr.read()
            fw.write(fr_read)
            return (len(fr_read))
