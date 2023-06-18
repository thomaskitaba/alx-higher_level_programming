#!/usr/bin/python3
"""
    test instantator,
    static and class methods of
    the base class
    1- Intatansitation test
    2- test to_json_string
    3- test save_to_file
    4- test from_json_string
    5- test create
    6- test load_from_file
    7- test save_to_file_csv
    8- test load_from_file_csv
"""
import unittest
import csv
import json
from models.base import Base

class Intatansitation_test(unittest.TestCase):
    """ 1- Intatansitation test """

    def test_if_instance_is_base(self):
        self.assertIsInstance(Rectangle(2, 3), Base)

class test_to_json_string(unittest.TestCase):
    """ 2- test to_json_string"""
    pass

class test_save_to_file(unittest.TestCase):
    """  3- test save_to_file """
    pass

class test_from_json_string(unittest.TestCase):
    """ 4- test from_json_string """
    pass

class test_create(unittest.TestCase):
    """ 5- test create """
    pass

class test_load_from_file(unittest.TestCase):
    """ 6- test load_from_file """
    pass

class test_save_to_file_csv(unittest.TestCase):
    """ 7- test save_to_file_csv """
    pass

class test_load_from_file_csv(unittest.TestCase):
    """ 8- test load_from_file_csv """
    pass
