#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    list_key = list(a_dictionary.keys())
    list_value = list(a_dictionary.values())

    # try:
    #     value_of_index = list_value.index(value)
    # except ValueError:
    #     return (a_dictionary)
    found = 0
    for i in range(len(list_value)):
        if list_value[i] == value:
            found = 1
            value_of_index = i
            key_to_delet = list_key[value_of_index]
            del a_dictionary[key_to_delet]

    if found == 0:
        return (a_dictionary)

    # key_to_delet = list_key[value_of_index]
    # del a_dictionary[key_to_delet]

    return (a_dictionary)
