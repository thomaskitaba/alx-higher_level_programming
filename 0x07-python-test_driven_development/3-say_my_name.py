#!/usr/bin/python3
""" say_my_name
Parameters:
- first_name (string): The first number.
- last_name (string, optional): The second name. Defaults to "".
"""


def say_my_name(first_name, last_name=""):
    """ print first_name and last_name """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
