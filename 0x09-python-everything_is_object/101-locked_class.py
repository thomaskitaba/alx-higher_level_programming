#!/usr/bin/python3
""" Create locked class """


class LockedClass:
    """
    allow only for the creation of first name attribute
    """
    __slots__ = ['first_name']
