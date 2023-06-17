#!/usr/bin/python3
""" test rectangle class
    which is subclass of Base
    1- Test Rectangle instantiation
    2- Test Rectangle width
    3- Test Rectangle height
    4- Test Rectangle x
    5- Test Rectangle y
    6- Test order of initialization
    7- Test Rectangle area
    8 Test Rectangle stdout
    9- Test Rectangle update *args
    10- Test Rectangle update *kwargs
    11- Test Rectangle to_dictionary
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle_instantiation(unittest.TestCase):

    """---1--- Test Rectangel INSTANCE """
    def test_if_Base(self):
        self.assertisinstance(Rectangle(2, 3), Base)

    def test_if_Rectangle(self):
        self.assertisinstance(Rectangle(2, 3), Rectangle)

    """---2--- Test Number of arguments """
    def test_empty_argument(self):  # TODO:  check in advance
        with self.assertRaises(TypeError):
            Square()

    def test_five_argument(self):   # TODO: test cases
        with self.assertRaises(TypeError)
            Square(2, 3, 4, 5, 6)

    def test_one_argument(self):
        s1 = Square(2)
        self.assertEqual(s1.id, 1)

    def test_two_argument(self):
        s1 = Square(2, 3)
        self.assertEqual(s1.id, 1)

    def test_three_argument(self):
        s1 = Square(2, 3, 4)
        self.assertEqual(s1.id, 1)

    def test_four_argument(self):
        s1 = Square(2, 3, 4, 5)
        self.assertEqual(s1.id, 1)

    """---3--- TEST getter and setter """
    def test_width_getter(self):
        r = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(2, r.width)

    def test_width_setter(self):
        r = Rectangle(2, 3, 4, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(3, r.height)

    def test_height_setter(self):
        r = Rectangle(2, 3, 4, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(4, r.x)

    def test_x_setter(self):
        r = Rectangle(2, 3, 4, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(2, 3, 4, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)

class Test_Rectangle_width(unittest.TestCase):
    """ ---1--- Test None, boolean, complex, range, bytes(b'Python)
        bytearray bytearray(b'abcdefg'), memoryview(b'abcedfg')
        float('inf'), float('nan'), """
    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4, 0 , 0)

    def test_boolean_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 4, 0 , 0)

    def test_float_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 4, 0 , 0)

    def test_float_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 4, 0 , 0)

    """ --2--string, float, negative, zero"""
    def test_string_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 5, 0, 0)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(4.5, 5, 6, 7)

    def test_negative_width(self):
        with self.assertRaisesRegex(TypeError, "width must be >= 0"):
            Rectangle(-4, 5, 6, 7)

    def test_zero_width(self):
        with self.assertRaisesRegex(TypeError, "width must be >= 0"):
            Rectangle(0, 5, 6, 7)
    """ --3-- Test dictionay, set , tuple, list """
    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4), 5, 0, 0)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([4], 5, 6, 7)

    def test_dictionary_width(self):
        with self.assertRaisesRegex(TypeError, "width must be >= 0"):
            Rectangle({"width: 4"}, 5, 6, 7)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be >= 0"):
            Rectangle({4, 5}, 5, 6, 7)

class Test_Rectangle_height(unittest.TestCase):
    """ ---1--- Test None, boolean, complex, range, bytes(b'Python)
        bytearray bytearray(b'abcdefg'), memoryview(b'abcedfg')
        float('inf'), float('nan'), """
    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, None, 4, 0)

    def test_boolean_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, True, 4, 0)

    def test_float_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('inf'), 4, 0)

    def test_float_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('nan'), 4, 0)

    """ --2--string, float, negative, zero"""
    def test_string_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "height", 0, 0)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, 5.5, 6, 7)

    def test_negative_height(self):
        with self.assertRaisesRegex(TypeError, "height must be >= 0"):
            Rectangle(4, -5, 6, 7)

    def test_zero_height(self):
        with self.assertRaisesRegex(TypeError, "height must be >= 0"):
            Rectangle(4, 0, 6, 7)
    """ --3-- Test dictionay, set , tuple, list """

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (5), 0, 0)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [5], 6, 7)

    def test_dictionary_height(self):
        with self.assertRaisesRegex(TypeError, "height must be >= 0"):
            Rectangle(4, {"width: 5"}, 6, 7)

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be >= 0"):
            Rectangle(4, {4, 5}, 6, 7)


class Test_Rectangle_x(unittest.TestCase):
    """ ---1--- Test None, boolean, complex, range, bytes(b'Python)
        bytearray bytearray(b'abcdefg'), memoryview(b'abcedfg')
        float('inf'), float('nan'), """
    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, None, 0)

    def test_boolean_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, True, 0)

    def test_float_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, float('inf'), 0)

    def test_float_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, float('nan'), 0)

    """ --2--string, float, negative, zero"""
    def test_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, "x", 0)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, 6.5, 0)

    def test_negative_x(self):
        with self.assertRaisesRegex(TypeError, "x must be >= 0"):
            Rectangle(4, 5, -6, 0)

    def test_zero_x(self):
        with self.assertRaisesRegex(TypeError, "x must be >= 0"):
            Rectangle(4, 5, 0, 5)

    """ --3-- Test dictionay, set , tuple, list """

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, (6), 0)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, [6], 7)

    def test_dictionary_x(self):
        with self.assertRaisesRegex(TypeError, "x must be >= 0"):
            Rectangle(4, 5, {"width: 6"}, 7)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be >= 0"):
            Rectangle(4, 5, {6, 7}, 8)


class Test_Rectangle_y(unittest.TestCase):

    """ ---1--- Test None, boolean, complex, range, bytes(b'Python)
        bytearray bytearray(b'abcdefg'), memoryview(b'abcedfg')
        float('inf'), float('nan'), """

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 0, None)

    def test_boolean_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5,  0, True)

    def test_float_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 0, float('inf'))

    def test_float_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 0, float('nan'))
    """ --2-- string, float, negative, zero"""
    def test_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 0, "y")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, 6.5)

    def test_negative_y(self):
        with self.assertRaisesRegex(TypeError, "y must be >= 0"):
            Rectangle(4, 5, 6, -7)

    def test_zero_y(self):
        with self.assertRaisesRegex(TypeError, "y must be >= 0"):
            Rectangle(4, 5, 6, 0)

    """ --3-- Test dictionay, set, tuple, list """
    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, (7))

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, [7])

    def test_dictionary_y(self):
        with self.assertRaisesRegex(TypeError, "y must be >= 0"):
            Rectangle(4, 5, 6, {"width: 7"})

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be >= 0"):
            Rectangle(4, 5, 6, {7, 8})


class Test_order_of_initialization(unittest.Testcase):

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", "height", "x", "y")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 5, "x", "y")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 5, 0, "y")

    def test_height_before_x_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "height", "x", "y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, "x", "y")

    def test_finaly_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 0, "y")

class Test_Rectangle_area(unittest.TestCase):
    pass


class Test_Rectangle_stdout(unittest.TestCase):
    pass


class Test_Rectangle_update_args(unittest.TestCase):
    pass


class Test_Rectangle_update_kwargs(unittest.TestCase):
    pass


class Test_Rectangle_to_dictionary(unittest.TestCase):
    pass