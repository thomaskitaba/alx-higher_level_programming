#!/usr/bin/python3
""" text_indentation
Parameters:
- text (string): text to be manuplated.

"""


def text_indentation(text):
    """ indent text when . : or ? is found """

    all_text = []
    line_text = []

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """ iterate and create list of strings"""
    for i in range(len(text)):

        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            all_text.append([''.join(line_text)])
            line_text.clear()
        else:
            line_text.append(text[i])
        if i == len(text) - 1:
            all_text.append([''.join(line_text)])
    """ strip inital space for a string """
    for row in all_text:
        print(row[0].lstrip())
        print('')
