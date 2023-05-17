#!/usr/bin/python3
def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        return sum(list(set(my_list)))
