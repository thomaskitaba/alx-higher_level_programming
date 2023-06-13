#!/usr/bin/python3
""" append text """


def append_after(filename="", search_string="", new_string=""):
    """ search and replace with new string """
    my_str = ""
    with open(filename, 'r') as fr:
        # add loop heare
        for line_r in fr:
            my_str += line_r
            if search_string != '' and search_string in line_r:
                my_str += new_string

    with open(filename, 'w') as fw:
        fw.write(my_str)
