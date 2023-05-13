#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list = my_list[::-1]
        for value in my_list:
            print("{}".format(value))
