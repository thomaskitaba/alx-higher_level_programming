#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if isinstance(my_list, list):
        result = list(map(lambda x: x * number, my_list))
    return (result)
