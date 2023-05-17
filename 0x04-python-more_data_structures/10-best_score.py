#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        if a_dictionary:
            value = list(a_dictionary.values())
            if not value:
                return (None)
            key = list(a_dictionary.keys())
            index_of_max = value.index(max(value))
        return (key[index_of_max])
