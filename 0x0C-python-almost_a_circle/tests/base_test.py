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
import os
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
        b2 = Base(None)
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
    def test_rect_to_json_string_with_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_rect_to_json_string_type(self):
        br1 = Rectangle(2, 2, 2, 2)
        self.assertTrue(Base.to_json_string(br1.to_dictionary()), str)

    def test_rect_to_json_string_multiple_list(self):
        br1 = Rectangle(2, 2, 2, 2)
        br2 = Rectangle(3, 3, 3, 3)
        list_dictionary = [br1.to_dictionary(), br2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_dictionary)), 106)

    def test_square_to_json_string_type(self):
        bs1 = Square(2, 2, 2)
        self.assertTrue(Base.to_json_string(bs1.to_dictionary()), str)

    def test_square_to_json_string_multiple_list(self):
        bs1 = Square(2, 2, 2)
        bs2 = Square(3, 3, 3)
        list_dictionary = [bs1.to_dictionary(), bs2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_dictionary)), 78)


class test_save_to_file(unittest.TestCase):
    """  3- test save_to_file """
    @classmethod
    def tearDown(self):
        try:
            os.remove("Base.json")
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except IOError:
            pass

    def test_rect_to_file(self):
        br1 = Rectangle(2, 2, 2, 2)
        Rectangle.save_to_file([br1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 52)

    def test_rect_to_file_multiple_list(self):
        br1 = Rectangle(2, 2, 2, 2)
        br2 = Rectangle(3, 3, 3, 3)
        list_dictionary = [br1.to_dictionary(), br2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_dictionary)), 106)

    def test_square_to_json_string_type(self):
        bs1 = Square(2, 2, 2)
        self.assertTrue(Base.to_json_string(bs1.to_dictionary()), str)

    def test_square_to_json_string_multiple_list(self):
        bs1 = Square(2, 2, 2)
        bs2 = Square(3, 3, 3)
        list_dictionary = [bs1.to_dictionary(), bs2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_dictionary)), 78)


class test_from_json_string(unittest.TestCase):
    """ 4- test from_json_string """
    """ test to_json_string
        ---1--- edge cases: None, as list empty list
        ---2--- list of tupels, list of lists list of tuples
        ---3---
    """
    def tearDown(self):
        try:
            os.remove("Base.json")
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except:
            pass

    def test_rect_from_json_string_with_no_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_rect_from_json_string_type(self):
        br1 = Rectangle(2, 2, 2, 2)
        with open("Rectangle.json", 'w') as f:
            f = f.write(Base.to_json_string(br1.to_dictionary()))

        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), '{"id": 8, "width": 2, "height": 2, "x": 2, "y": 2}')

    def test_rect_from_json_string_type(self):
        with open("Rectangle.json", 'w') as f:
            f = f.write(Base.to_json_string(None))

        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

    def test_rect_from_json_string_multiple_list(self):
        br1 = Rectangle(2, 2, 2, 2)
        br2 = Rectangle(3, 3, 3, 3)
        list_dictionary = [br1.to_dictionary(), br2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_dictionary)), 104)

    def test_square_from_json_string_type(self):
        bs1 = Square(2, 2, 2)
        self.assertTrue(Base.to_json_string(bs1.to_dictionary()), str)

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
