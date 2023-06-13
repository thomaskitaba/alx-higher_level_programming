#!/usr/bin/python3
"""
    student to JSON
"""


class Student:
    """ student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return attribte defined by attrs """
        if isinstance(attrs, list):
            """ filter dict with attrs """
            my_list = list(filter(lambda x: x in attrs, self.__dict__))
            my_dict = {}
            for key in my_list:
                my_dict[key] = self.__dict__.get(key)
            return (my_dict)
        return (self.__dict__)

    def reload_from_json(self, json):
        """ replaces attributes of student """
        for key, value in json.items():
            self.__dict__[key] = value
        return (self.__dict__)
