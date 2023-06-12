#!/usr/bin/bash
"""
class Mylist that inherits from list

"""


class MyList(list):
    """ print the list """

    def print_sorted(self):
        """ print sorted """
        print(sorted(self))
