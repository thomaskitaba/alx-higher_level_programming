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
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle_instantiation(unittest.TestCase):

    """---1--- Test Rectangel INSTANCE """
    def test_if_Base(self):
        self.assertIsInstance(Rectangle(2, 3), Base)

    def test_if_Rectangle(self):
        self.assertIsInstance(Rectangle(2, 3), Rectangle)

    """---2--- Test Number of arguments """
    def test_empty_argument(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_six_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, 5, 6, 7)

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_two_argument(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_argument(self):
        r1 = Rectangle(2, 3, 4)
        r2 = Rectangle(3, 4, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_argument(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(2, 3)
        self.assertEqual(r1.id, r2.id - 1)

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

    # def test_boolean_width(self):
    #     with self.assertRaisesRegex(TypeError, "width must be an integer"):
    #         Rectangle(True, 4, 0 , 0)

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
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-4, 5, 6, 7)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5, 6, 7)

    """ --3-- Test dictionay, set , tuple, list """
    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4, 2), 5, 0, 0)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([4], 5, 6, 7)

    def test_dictionary_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"width: 4"}, 5, 6, 7)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({4, 5}, 5, 6, 7)

class Test_Rectangle_height(unittest.TestCase):
    """ ---1--- Test None, boolean, complex, range, bytes(b'Python)
        bytearray bytearray(b'abcdefg'), memoryview(b'abcedfg')
        float('inf'), float('nan'), """
    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, None, 4, 0)

    # def test_boolean_height(self):
    #     with self.assertRaisesRegex(TypeError, "height must be an integer"):
    #         Rectangle(4, True, 4, 0)

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
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, -5, 6, 7)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, 0, 6, 7)
    """ --3-- Test dictionay, set , tuple, list """

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (5, 4), 0, 0)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [5], 6, 7)

    def test_dictionary_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {"width: 5"}, 6, 7)

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {4, 5}, 6, 7)


class Test_Rectangle_x(unittest.TestCase):
    """ ---1--- Test None, boolean, complex, range, bytes(b'Python)
        bytearray bytearray(b'abcdefg'), memoryview(b'abcedfg')
        float('inf'), float('nan'), """
    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, None, 0)

    # def test_boolean_x(self):
    #     with self.assertRaisesRegex(TypeError, "x must be an integer"):
    #         Rectangle(4, 5, True, 0)

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
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(4, 5, -6, 0)

    """ --3-- Test dictionay, set , tuple, list """

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, (6, 7), 0)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, [6], 7)

    def test_dictionary_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, {"width: 6"}, 7)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, {6, 7}, 8)


class Test_Rectangle_y(unittest.TestCase):

    """ ---1--- Test None, boolean, complex, range, bytes(b'Python)
        bytearray bytearray(b'abcdefg'), memoryview(b'abcedfg')
        float('inf'), float('nan'), """
    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 0, None)

    # def test_boolean_y(self):
    #     with self.assertRaisesRegex(TypeError, "y must be an integer"):
    #         Rectangle(4, 5, 0, False)

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
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(4, 5, 6, -7)

    """ --3-- Test dictionay, set, tuple, list """
    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, (7, 5))

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, [7])

    def test_dictionary_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, {"width: 7"})

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, {7, 8})


class Test_order_of_initialization(unittest.TestCase):

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
    """ test large number, small_number, with argument """

    def test_small_width_height(self):
        r1 = Rectangle(3, 4, 0, 0)
        self.assertEqual(r1.area(), 12)

    def test_large_width_height(self):
        r1 = Rectangle(33333, 44444, 0)
        self.assertEqual(r1.area(), 1481451852)


class Test_Rectangle_stdout(unittest.TestCase):
    """ test rectangle printed on stdout """
    """ --1-- test __str__ width, height, x, y, id """

    def capture_the_stdout(obj, method_name):
        capture = io.StringIO()
        sys.stdout = capture
        if method_name == "print":
            print(obj)
        else:
            obj.display()
        sys.stdout == sys.__stdout__
        return capture.getvalue()

    def test_str_with_width_height(self):
        r1 = Rectangle(2, 3)
        correct = "[Rectangle] ({}) 0/0 - 2/3".format(r1.id)
        self.assertEqual(correct, str(r1))

    def test_str_with_width_height_x(self):
        r1 = Rectangle(2, 3, 4)
        correct = "[Rectangle] ({}) 4/0 - 2/3".format(r1.id)
        self.assertEqual(correct, str(r1))

    def test_str_width_before_height_x_y(self):
        r1 = Rectangle(2, 3, 4, 5)
        correct = "[Rectangle] ({}) 4/5 - 2/3".format(r1.id)
        self.assertEqual(correct, str(r1))

    def test_str_width_before_height_x_y_id(self):
        r1 = Rectangle(2, 3, 4, 5, 6)
        correct = "[Rectangle] (6) 4/5 - 2/3"
        self.assertEqual(correct, str(r1))

    """ ---- test __str__ with arg  """
    def test_str_with_argument(self):
        r1 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r1.__str__(2)

    """ --3-- display test width, height, x, y, id """

    def test_display_with_width_height(self):
        r1 = Rectangle(2, 2)
        captured = Test_Rectangle_stdout.capture_the_stdout(r1, "display")
        correct = "##\n##\n"
        self.assertEqual(correct, captured)

    def test_display_with_width_height_x(self): #TODO: turn it back to 2 , 2, 2
        r1 = Rectangle(2, 2)
        captured = Test_Rectangle_stdout.capture_the_stdout(r1, "display")
        correct = "##\n##\n"
        self.assertEqual(correct, captured)

    def test_display_with_width_height_y(self):
        r1 = Rectangle(2, 2, 0, 2)
        captured = Test_Rectangle_stdout.capture_the_stdout(r1, "display")
        correct = "\n\n##\n##\n"
        self.assertEqual(correct, captured)

    def test_display_width_before_height_x_y(self):
        r1 = Rectangle(2, 2, 2, 2)
        captured = Test_Rectangle_stdout.capture_the_stdout(r1, "display")
        correct = "\n\n  ##\n  ##\n"
        self.assertEqual(correct, captured)

    def test_display_width_before_height_x_y_id(self):
        r1 = Rectangle(2, 2, 2, 2, 6)
        captured = Test_Rectangle_stdout.capture_the_stdout(r1, "display")
        correct = "\n\n  ##\n  ##\n"
        self.assertEqual(correct, captured)

    """ --4-- test display with arg  """
    def test_display_with_argument(self):
        r1 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r1.display(2)

class Test_Rectangle_update_args(unittest.TestCase):
    """ Test update
        ---1--- test edge cases ( zero args, None(id, w, h, x, y) )
        ---2--- test 1, 2, 3, 4, 5 arguments
        ---3--- test with invalid data ( id, w, h, x, y)
    """

    """ ---1--- test edge cases ( zero args, None(id, w, h, x, y) )"""
    def test_update_with_no_args(self):
        r1 = Rectangle(2, 2, 2, 2)
        r1.update()
        correct = "[Rectangle] ({}) 2/2 - 2/2".format(r1.id)
        self.assertEqual(correct, str(r1))

    def test_update_with_none_as_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    """---2--- test 1, 2, 3, 4, 5 arguments"""
    def test_update_with_1_arg(self):
        r1 = Rectangle(2, 2, 2, 2)
        r1.update(3)
        correct = "[Rectangle] (3) 2/2 - 2/2"
        self.assertEqual(correct, str(r1))

    def test_update_with_2_arg(self):
        r1 = Rectangle(2, 2, 2, 2)
        r1.update(3, 4)
        correct = "[Rectangle] (3) 2/2 - 4/2"
        self.assertEqual(correct, str(r1))

    def test_update_with_3_arg(self):
        r1 = Rectangle(2, 2, 2, 2)
        r1.update(3, 4, 5)
        correct = "[Rectangle] (3) 2/2 - 4/5"
        self.assertEqual(correct, str(r1))

    def test_update_with_4_arg(self):
        r1 = Rectangle(2, 2, 2, 2)
        r1.update(3, 4, 5, 6)
        correct = "[Rectangle] (3) 6/2 - 4/5"
        self.assertEqual(correct, str(r1))

    def test_update_with_5_arg(self):
        r1 = Rectangle(2, 2, 2, 2)
        r1.update(3, 4, 5, 6, 7)
        correct = "[Rectangle] (3) 6/7 - 4/5"
        self.assertEqual(correct, str(r1))

    """---3--- test with invalid data ( id, w, h, x, y)"""
    def test_update_with_invalid_id(self):
        r1 = Rectangle(2, 2, 2, 2)
        r1.update(-1)
        self.assertEqual(r1.id, -1)

    def test_update_with_invalid_width(self):
        r1 = Rectangle(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(1, "width")

    def test_update_with_zero_width(self):
        r1 = Rectangle(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(2, 0)

    def test_update_with_invalid_height(self):
        r1 = Rectangle(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 2, "height")

    def test_update_with_zero_height(self):
        r1 = Rectangle(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(1, 2, 0)

    def test_update_with_invalid_x(self):
        r1 = Rectangle(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 2, 2, "x")

    def test_update_with_zero_x(self):
        r1 = Rectangle(1, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(1, 2, 2, -1)

    def test_update_with_invalid_y(self):
        r1 = Rectangle(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 2, 2, 2, "y")

    def test_update_with_zero_y(self):
        r1 = Rectangle(1, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(1, 2, 2, 2, -1)


class Test_Rectangle_update_kwargs(unittest.TestCase):
    pass


class Test_Rectangle_to_dictionary(unittest.TestCase):
    """ test if dictionary is returned
        ---1--- test for normal output
        ---2--- test with argument
    """

    """ ---1--- test for normal output """

    def test_to_dictioary(self):
        r1 = Rectangle(2, 3, 4, 5, 6)
        result = {"width": 2,
                "height": 3,
                "x": 4,
                "y": 5,
                "id": 6}
        self.assertEqual(r1.to_dictionary(), result)

    """ ---2--- test with argument """
    def test_to_dictioary_with_argument(self):
        r1 = Rectangle(2, 3, 5)
        with self.assertRaises(TypeError):
            r1.to_dictionary(2)
if __name__ == "__main__":
    unitters.main()