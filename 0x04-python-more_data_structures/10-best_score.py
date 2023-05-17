#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary:
        value = list(a_dictionary.values())
        key = list(a_dictionary.keys())
        index_of_max = value.index(max(value))
    else:
        return (None)
    return (key[index_of_max])
