#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for num in my_list:
        if num == search:
            num = replace
        result.append(num)
    reutrn (result)
