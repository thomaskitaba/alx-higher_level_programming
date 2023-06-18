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
from models.rectangle import Rectangle
from models.square import Square

class Intatansitation_test(unittest.TestCase):
    """  Intatansitation test
        ---1--- Edge cases: None as id, float('inf'), float('nan')
        ---2--- Test single base, double base
        ---3--- Test with datastructures as id (dictionary, list, set, tuple)

    """

    """ Edge cases: None as id, float('inf'), float('nan')"""
    def test_with_None_as_id(self):
        b1 = Base(None)
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_float_inf_as_id(self):
        b1 = Base(float('inf'))
        self.assertEqual(float('inf'), b1.id)

    def test_with_float_nan_as_id(self):    #TODO: #TODO: #TODO: Read in advance
        b1 = Base(float('nan'))
        self.assertNotEqual(float('nan'), b1.id)

    """---2--- Test single base, double base"""
    def test_with_single_base(self):
        b1 = Base()
        self.assertTrue(b1.id > 0)

    def test_with_double_base(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    """---3--- Test with datastructures as id (tuple, list, dictionary,set)"""
    def test_with_tuple_as_id(self):  #TODO: #TODO: #TODO:
        self.assertEqual((2, 3), Base((2, 3)).id)

    def test_with_list_as_id(self):
        self.assertEqual([2, 3], Base([2, 3]).id)

    def test_with_dictionary_as_id(self):
        self.assertEqual({"id": 2}, Base({"id": 2}).id)

    def test_with_set_as_id(self):
        self.assertEqual({2, 3}, Base({2, 3}).id)

class test_to_json_string(unittest.TestCase):
    """ test to_json_string
        ---1--- edge cases: None, as list empty list, empty dict
        ---2--- list of tupels, list of lists list of tuples
        ---3---
    """
    def test_to_json_string_with_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_id_none(self):
        b1 = Base(None)
        b2 =Base(None)
        self.assertEqual(b1.id, b2.id - 1)

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
