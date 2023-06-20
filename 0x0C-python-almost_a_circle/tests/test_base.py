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

    def test_with_float_nan_as_id(self):    # TODO:  Read in advance
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
    def test_with_tuple_as_id(self):  # TODO:
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
    """ test save_to_file
        ---1--- Edge Cases: Rectangle.save_to_file(None)
        ---2--- valid arguments: 1
    """
    @classmethod
    def tearDown(self):
        try:
            os.remove("Base.json")
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except IOError:
            pass

    def test_rect_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_rect_to_file(self):
        br1 = Rectangle(2, 2, 2, 2)
        Rectangle.save_to_file([br1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 53)

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
        ---1--- edge cases: with out arg None, as list empty list
                for Rectangle and Square
        ---2--- list of tupels, list of lists list of tuples
    """
    def tearDown(self):
        try:
            os.remove("Base.json")
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except Exception as e:
            pass

    "---1--- edge cases: with out arg None, as list empty list"

    def test_rect_from_json_string_with_no_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_rect_from_json_string_none(self):
        with open("Rectangle.json", 'w') as f:
            f = f.write(Base.to_json_string(None))

        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

    def test_rect_from_jston_string_empty_list(self):
        with open("Rectangle.json", 'w', encoding="utf-8") as f:
            f.write(Base.to_json_string([]))
        with open("Rectangle.json", 'r') as f:
            self.assertTrue("[]" == f.read())

    def test_rect_from_json_string_normal(self):
        br1 = Rectangle(2, 2, 2, 2)
        with open("Rectangle.json", 'w') as f:
            f = f.write(Base.to_json_string(br1.to_dictionary()))
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(len(Base.from_json_string(f.read())), 5)

    # to Square
    def test_square_from_json_string_none(self):
        with open("square.json", 'w') as f:
            f = f.write(Base.to_json_string(None))

        with open("square.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

    def test_square_from_jston_string_empty_list(self):
        with open("square.json", 'w', encoding="utf-8") as f:
            f.write(Base.to_json_string([]))
        with open("square.json", 'r') as f:
            self.assertTrue("[]" == f.read())

    def test_square_from_json_string_normal(self):
        s1 = Square(2, 2, 2)
        with open("Square.json", 'w') as f:
            f = f.write(Base.to_json_string(s1.to_dictionary()))
        with open("Square.json", 'r') as f:
            self.assertEqual(Base.from_json_string(f.read())["size"], 2)


class test_create(unittest.TestCase):
    """ TEST CREATE
        ---1--- Edge cases: no arg, None, empty list, one
        ---2--- Test invalid arguments list, tuple, set
        ---3--- Test invalid date to width, height, x, y
        ---4--- Test 1, 2, 3, 4
    """

    """---1--- Edge cases: no arg, None, empty list, one"""
    def test_create_with_no_args(self):
        r1 = Rectangle(2, 2, 2, 2)
        r2 = Rectangle.create()
        self.assertEqual(r1.id, r2.id - 1)

    def test_create_with_none_as_id(self):
        r1 = Rectangle(2, 2, 2, 2)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(None)

    def test_create_with_none_as_id(self):
        r1 = Rectangle(2, 2, 2, 2)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create({})

    # TODO:
    """---2--- Test invalid arguments list, tuple, set"""

    def test_create_with_list_kwarg(self):

        my_dict = [{'height': 4, 'width': 10, 'id': 89},
                   {'height': 7, 'width': 1, 'id': 7}]
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(**my_dict)

    def test_create_with_tuple_kwarg(self):
        my_dict = (2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(**my_dict)

    def test_create_with_set_kwarg(self):
        my_dict = {2, 4, 6}
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(**my_dict)

    def test_create_with_string(self):
        my_dict = "string"
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(**my_dict)

    """---4--- test 1, 2, 3, 4, 5 arguments"""
    def test_create_with_one_args(self):

        my_dict = {'height': 4}
        r2 = Rectangle.create(**my_dict)
        with open("Rectangle.json", 'w') as f:
            f = f.write(Base.to_json_string(r2.to_dictionary()))
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(Base.from_json_string(f.read())["height"], 4)

    def test_create_with_two_args(self):

        my_dict = {'height': 4, 'width': 10}
        r2 = Rectangle.create(**my_dict)
        with open("Rectangle.json", 'w') as f:
            f = f.write(Base.to_json_string(r2.to_dictionary()))
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(Base.from_json_string(f.read())["height"], 4)

    def test_create_with_three_args(self):

        my_dict = {'height': 4, 'width': 10, 'id': 89}
        r2 = Rectangle.create(**my_dict)
        with open("Rectangle.json", 'w') as f:
            f = f.write(Base.to_json_string(r2.to_dictionary()))
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(Base.from_json_string(f.read())["height"], 4)

    def test_create_with_four_args(self):

        my_dict = {'height': 4, 'width': 10, 'id': 89, 'x': 2}
        r2 = Rectangle.create(**my_dict)
        with open("Rectangle.json", 'w') as f:
            f = f.write(Base.to_json_string(r2.to_dictionary()))
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(Base.from_json_string(f.read())["height"], 4)

    def test_create_with_invalid_key_args(self):

        my_dict = {'height': 4, 'width': 10, 'id': 89, 'x': 2, 'z': 3}
        r2 = Rectangle.create(**my_dict)
        with open("Rectangle.json", 'w') as f:
            f = f.write(Base.to_json_string(r2.to_dictionary()))
        with open("Rectangle.json", 'r') as f:
            with self.assertRaises(KeyError):
                Base.from_json_string(f.read())['']


class test_load_from_file(unittest.TestCase):
    """ test load_from_file
        ---1--- load from single dict
        ---2--- load from multiple dict and check last and first obj
        ---3--- save invalid args
        ---4--- check instances of loaded data
    """
    def tearDown(self):
        try:
            os.remove("Base.json")
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except Exception as e:
            pass

    """---1--- load from single dict"""
    def test_load_from_file_single_obj(self):
        r1 = Rectangle(2, 3, 4)
        Rectangle.save_to_file([r1])
        r2 = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(r2[0]))

    """---2--- load from multiple dict and check last and first obj"""
    def test_load_from_file_single_obj(self):
        r1 = Rectangle(2, 3, 4)
        r2 = Rectangle(5, 6, 7)
        Rectangle.save_to_file([r1, r2])
        r3 = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(r3[1]))

    "---3--- save invalid args"
    def test_for_invalid_arguments(self):
        r1 = Rectangle(2, 3)
        Rectangle.save_to_file([r1])
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([])

    """ ---4--- check instances of loaded data"""
    def test_for_type_of_loaded_object(self):
        r1 = Rectangle(2, 3, 4)
        r2 = Rectangle(5, 6, 7)
        Rectangle.save_to_file([r1, r2])
        r3 = Rectangle.load_from_file()
        self.assertTrue(all(type(dict) == Rectangle for dict in r3))


class test_save_to_file_csv(unittest.TestCase):
    """ test save_to_file_csv
        ---1-- Edge cases: none, emplty list
        ---2--- with 1 and 2 list arguments

    """
    def tearDown(self):
        try:
            os.remove("Base.json")
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except Exception as e:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("Base.json")
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except IOError:
            pass

    """ ---1-- Edge cases: none, emplty list, """

    def test_square_to_csv_empty_list(self):
        # with self.assertRaises(TypeError):
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual("[]", f.read())

    def test_square_to_csv_None(self):
        # with self.assertRaises(TypeError):
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual("[]", f.read())

    """ ---2--- with 1 and 2 list arguments """

    def test_rect_to_file_csv_one_arg(self):
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file_csv(list_rectangles_input)

        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f"{r1.id},10,7,2,8\n", f.read())

    def test_rect_to_csv_multiple_list(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 2, 2, 2)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)

        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f"{r1.id},10,7,2,8\n{r2.id},2,2,2,2\n", f.read())

    def test_square_to_csv_string_multiple_list(self):
        bs1 = Square(2, 2, 2)
        bs2 = Square(3, 3, 3)
        list_dictionary = [bs1.to_dictionary(), bs2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_dictionary)), 78)


class test_load_from_file_csv(unittest.TestCase):
    """ 8- test load_from_file_csv """
    """ test save_to_file_csv
        ---1-- Edge cases: none, emplty list
        ---2--- with 1 and 2 list arguments

    """
    def tearDown(self):
        try:
            os.remove("Base.json")
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except Exception as e:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("Base.json")
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except IOError:
            pass

    """ ---1-- Edge cases: none, emplty list, """

    def test_Rectangle_to_csv_empty_list(self):

        Rectangle.save_to_file_csv([])
        with self.assertRaises(ValueError):
            Rectangle.load_from_file_csv()

    """ ---2--- with 1 and 2 list arguments """

    def test_rect_to_file_csv_one_arg(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file_csv([r1])
        loaded = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(loaded[0]))

    def test_rect_to_csv_multiple_list(self):
        r1 = Square(5, 1, 3, 3)
        r2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([r1, r2])
        loaded = Square.load_from_file_csv()
        self.assertEqual(str(r1), str(loaded[0]))

    def test_square_to_csv_string_multiple_list(self):
        r1 = Square(5, 1, 3, 3)
        r2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([r1, r2])
        loaded = Square.load_from_file_csv()
        self.assertEqual(type(r1), type(loaded[0]))
