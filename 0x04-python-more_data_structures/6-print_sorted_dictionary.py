#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary, key=None, reverse=False)
    for data in new_dict:
        print("{}: {}".format(data, a_dictionary.get(data)))
