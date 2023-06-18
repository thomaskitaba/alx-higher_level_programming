#!/usr/bin/python3
""" test Square class
    which is subclass of Base
    1- Test Square instantiation
    2- Test Square width
    3- Test Square height
    4- Test Square x
    5- Test Square y
    6- Test Square area
    7- Test Square stdout
    8- Test Square update *args
    9- Test Square update *kwargs
    10- Test Square to_dictionary
"""
import unittest
import io
import sys
from models.base import Base
from models.square import Square


class Test_Square_instantiation(unittest.TestCase):

    """---1--- Test square INSTANCE """
    def test_if_Base(self):
        self.assertIsInstance(Square(2), Base)

    def test_if_Square(self):
        self.assertIsInstance(Square(2), Square)

    """---2--- Test Number of arguments """
    def test_empty_argument(self):
        with self.assertRaises(TypeError):
            Square()

    def test_six_argument(self):
        with self.assertRaises(TypeError):
            Square(2, 3, 4, 5, 6, 7)

    def test_one_argument(self):
        s1 = Square(3)
        self.assertEqual(s1.width, 3)
    def test_two_argument(self):
        s1 = Square(2, 3)
        s2 = Square(2, 3)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_argument(self):
        s1 = Square(2, 3, 4)
        s2 = Square(3, 4, 5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_argument(self):
        s1 = Square(2, 3, 4)
        s2 = Square(2, 3)
        self.assertEqual(s1.id, s2.id - 1)

    """---3--- TEST getter and setter """
    def test_width_getter(self):
        r = Square(2, 3, 4, 5)
        self.assertEqual(2, r.width)

    def test_width_setter(self):
        r = Square(2, 3, 4, 5)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Square(2, 3, 4, 5)
        self.assertEqual(2, r.height)

    def test_height_setter(self):
        r = Square(2, 3, 4, 5)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Square(2, 3, 4, 5)
        self.assertEqual(3, r.x)

    def test_x_setter(self):
        r = Square(2, 3, 4, 5)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Square(2, 3, 4, 5)
        self.assertEqual(4, r.y)

    def test_y_setter(self):
        r = Square(2, 3, 4, 5)
        r.y = 10
        self.assertEqual(10, r.y)



class Test_Square_size(unittest.TestCase):
    """ ---1--- Test None, boolean, complex, range, bytes(b'Python)
        bytearray bytearray(b'abcdefg'), memoryview(b'abcedfg')
        float('inf'), float('nan'), """
    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 4, 0 , 0)

    # def test_boolean_width(self):
    #     with self.assertRaisesRegex(TypeError, "width must be an integer"):
    #         Square(True, 4, 0 , 0)

    def test_float_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 4, 0 , 0)

    def test_float_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 4, 0 , 0)

    """ --2--string, float, negative, zero"""
    def test_string_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("width", 5, 0, 0)

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(4.5, 5, 6, 7)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-4, 5, 6, 7)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 5, 6, 7)

    """ --3-- Test dictionay, set , tuple, list """
    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((4, 2), 5, 0, 0)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([4], 5, 6, 7)

    def test_dictionary_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"width: 4"}, 5, 6, 7)

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({4, 5}, 5, 6, 7)


class Test_Square_x(unittest.TestCase):
    """ ---1--- Test None, boolean, complex, range, bytes(b'Python)
        bytearray bytearray(b'abcdefg'), memoryview(b'abcedfg')
        float('inf'), float('nan'), """
    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, None, 0)

    # def test_boolean_x(self):
    #     with self.assertRaisesRegex(TypeError, "x must be an integer"):
    #         Square(4, 5, True, 0)

    def test_float_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, float('inf'), 0)

    def test_float_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, float('nan'), 0)

    """ --2--string, float, negative, zero"""
    def test_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, "x", 0)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, 5.5, 0)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(4, -5, 0)

    """ --3-- Test dictionay, set , tuple, list """

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, (5, 6), 0)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, [5], 6)

    def test_dictionary_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, {"width: 5"}, 6)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, {5, 6}, 7)


class Test_Square_y(unittest.TestCase):

    """ ---1--- Test None, boolean, complex, range, bytes(b'Python)
        bytearray bytearray(b'abcdefg'), memoryview(b'abcedfg')
        float('inf'), float('nan'), """
    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, None)

    # def test_boolean_y(self):
    #     with self.assertRaisesRegex(TypeError, "y must be an integer"):
    #         Square(4, 5, 0, False)

    def test_float_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, float('inf'))

    def test_float_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, float('nan'))
    """ --2-- string, float, negative, zero"""
    def test_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, "y")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, 6.5)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(4, 5, -7)

    """ --3-- Test dictionay, set, tuple, list """
    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, (7, 5))

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, [7])

    def test_dictionary_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, {"width: 7"})

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, {6, 7})


class Test_order_of_initialization(unittest.TestCase):

    def test_size_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("size", "x", "y")

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("size", 5, "x", "y")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("size", 0, "y")

    # def test_x_before_y(self):    #TODO: #TODO: #TODO: #TODO:
    #     with self.assertRaisesRegex(TypeError, "x must be an integer"):
    #         Square(4, "x", "y")

    def test_finaly_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 0, "y")

class Test_Square_area(unittest.TestCase):
    """ test large number, small_number, with argument """

    def test_small_width_height(self):
        s1 = Square(3, 4, 0, )
        self.assertEqual(s1.area(), 9)

    def test_large_width_height(self):
        s1 = Square(33333, 4)
        self.assertEqual(s1.area(), 1111088889)


class Test_Square_stdout(unittest.TestCase):
    """ test Square printed on stdout """
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
        s1 = Square(2, 3)
        correct = "[Square] ({}) 3/0 - 2".format(s1.id)
        self.assertEqual(correct, str(s1))

    def test_str_with_width_height_x(self):
        s1 = Square(2, 3, 4)
        correct = "[Square] ({}) 3/4 - 2".format(s1.id)
        self.assertEqual(correct, str(s1))

    def test_str_width_before_height_x_y(self):
        s1 = Square(2, 3, 4, 5)
        correct = "[Square] ({}) 3/4 - 2".format(s1.id)
        self.assertEqual(correct, str(s1))

    def test_str_width_before_height_x_y_id(self):
        s1 = Square(2, 3, 4, 6)
        correct = "[Square] (6) 3/4 - 2"
        self.assertEqual(correct, str(s1))

    """ ---- test __str__ with arg  """
    def test_str_with_argument(self):
        s1 = Square(2, 3)
        with self.assertRaises(TypeError):
            s1.__str__(2)

    """ --3-- display test width, height, x, y, id """

    def test_display_with_only_size(self):
        s1 = Square(2)
        captured = Test_Square_stdout.capture_the_stdout(s1, "display")
        correct = "##\n##\n"
        self.assertEqual(correct, captured)

    def test_display_with_size_x(self): #TODO: turn it back to 2 , 2, 2
        s1 = Square(2, 2)
        captured = Test_Square_stdout.capture_the_stdout(s1, "display")
        correct = "  ##\n  ##\n"
        self.assertEqual(correct, captured)


    def test_display_width_before_height_x_y(self):
        s1 = Square(2, 2, 2, 2)
        captured = Test_Square_stdout.capture_the_stdout(s1, "display")
        correct = "\n\n  ##\n  ##\n"
        self.assertEqual(correct, captured)

    def test_display_width_before_height_x_y_id(self):
        s1 = Square(2, 2, 2, 6)
        captured = Test_Square_stdout.capture_the_stdout(s1, "display")
        correct = "\n\n  ##\n  ##\n"
        self.assertEqual(correct, captured)

    """ --4-- test display with arg  """
    def test_display_with_argument(self):
        s1 = Square(2, 3)
        with self.assertRaises(TypeError):
            s1.display(2)

class Test_Square_update_args(unittest.TestCase):
    """ Test update
        ---1--- test edge cases ( zero args, None(id, w, h, x, y) )
        ---2--- test 1, 2, 3, 4, 5 arguments
        ---3--- test with invalid data ( id, w, h, x, y)
    """

    """ ---1--- test edge cases ( zero args, None(id, w, h, x, y) )"""
    def test_update_with_no_args(self):
        s1 = Square(2, 2, 2, 2)
        s1.update()
        correct = "[Square] ({}) 2/2 - 2/2".format(s1.id)
        self.assertEqual(correct, str(s1))

    def test_update_with_none_as_id(self):
        r = Square(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Square] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    """---2--- test 1, 2, 3, 4, 5 arguments"""
    def test_update_with_1_arg(self):
        s1 = Square(2, 2, 2, 2)
        s1.update(3)
        correct = "[Square] (3) 2/2 - 2/2"
        self.assertEqual(correct, str(s1))

    def test_update_with_2_arg(self):
        s1 = Square(2, 2, 2, 2)
        s1.update(3, 4)
        correct = "[Square] (3) 2/2 - 4/2"
        self.assertEqual(correct, str(s1))

    def test_update_with_3_arg(self):
        s1 = Square(2, 2, 2, 2)
        s1.update(3, 4, 5)
        correct = "[Square] (3) 2/2 - 4/5"
        self.assertEqual(correct, str(s1))

    def test_update_with_4_arg(self):
        s1 = Square(2, 2, 2, 2)
        s1.update(3, 4, 5, 6)
        correct = "[Square] (3) 6/2 - 4/5"
        self.assertEqual(correct, str(s1))

    def test_update_with_5_arg(self):
        s1 = Square(2, 2, 2, 2)
        s1.update(3, 4, 5, 6, 7)
        correct = "[Square] (3) 6/7 - 4/5"
        self.assertEqual(correct, str(s1))

    """---3--- test with invalid data ( id, w, h, x, y)"""
    def test_update_with_invalid_id(self):
        s1 = Square(2, 2, 2, 2)
        s1.update(-1)
        self.assertEqual(s1.id, -1)

    def test_update_with_invalid_width(self):
        s1 = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(1, "width")

    def test_update_with_zero_width(self):
        s1 = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(2, 0)

    def test_update_with_invalid_height(self):
        s1 = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            s1.update(1, 2, "height")

    def test_update_with_zero_height(self):
        s1 = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            s1.update(1, 2, 0)

    def test_update_with_invalid_x(self):
        s1 = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(1, 2, 2, "x")

    def test_update_with_zero_x(self):
        s1 = Square(1, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(1, 2, 2, -1)

    def test_update_with_invalid_y(self):
        s1 = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(1, 2, 2, 2, "y")

    def test_update_with_zero_y(self):
        s1 = Square(1, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(1, 2, 2, 2, -1)


class Test_Square_update_kwargs(unittest.TestCase):
    """ Test update
        ---1--- test edge cases ( zero args, None(id, w, h, x, y) )
        ---2--- test 1, 2, 3, 4, 5 arguments
        ---3--- test with invalid data ( id, w, h, x, y)
    """

    """ ---1--- test edge cases ( zero args, None(id, w, h, x, y) )"""

    def test_update_with_none_as_id(self):
        s1 = Square(2, 2, 2, 2)
        s1.update(id=None)
        correct = "[Square] ({}) 2/2 - 2".format(s1.id)
        self.assertEqual(correct, str(s1))

    """---2--- test 1, 2, 3, 4, 5 arguments"""
    def test_update_with_1_kwarg(self):
        s1 = Square(2, 2, 2, 2)
        kw = {"id": 2}
        s1.update(**kw)
        correct = "[Square] (2) 2/2 - 2"
        self.assertEqual(correct, str(s1))

    def test_update_with_3_kwarg(self):
        s1 = Square(2, 2, 2, 2)
        kw = {"id": 3, "size": 4}
        s1.update(**kw)
        correct = "[Square] (3) 2/2 - 4"
        self.assertEqual(correct, str(s1))

    def test_update_with_5_kwarg(self):
        s1 = Square(2, 2, 2, 2)
        kw = {"id": 3, "size": 4, "x": 6, "y": 7}
        s1.update(**kw)
        correct = "[Square] (3) 6/7 - 4"
        self.assertEqual(correct, str(s1))

    """---3--- test with invalid data ( id, w, h, x, y)"""
    def test_update_with_invalid_id_kwargs(self):
        s1 = Square(2, 2, 2, 2)
        kw = {"id": -1}
        s1.update(**kw)
        self.assertEqual(s1.id, -1)

    def test_update_with_invalid_width_kwargs(self):
        s1 = Square(2, 2, 2, 2)
        kw = {"id": 2, "size": "size"}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(**kw)

    def test_update_with_zero_width_kwargs(self):
        s1 = Square(2, 2, 2, 2)
        kw = {"id": 2, "size": 0}
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(**kw)

    def test_update_with_invalid_height_kwargs(self): # TODO: #TODO: TODO:CHECK width must be  should be height
        s1 = Square(2, 2, 2, 2)
        kw = {"id": 2, "width": 2, "height": "height"}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(*kw)

    def test_update_with_zero_height_kwargs(self):
        s1 = Square(2, 2, 2, 2)
        kw = {"id": 2, "size": 0}
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(**kw)

    def test_update_with_invalid_x_kwargs(self):
        s1 = Square(2, 2, 2, 2)
        kw = {"id": 2, "width": 2, "height": 2, "x": "x"}
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(**kw)

    def test_update_with_zero_x_kwargs(self):
        s1 = Square(1, 2, 2, 2)
        kw = {"id": 2, "width": 2, "height": 2, "x": -1}
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(**kw)

    def test_update_with_invalid_y_kwargs(self):
        s1 = Square(1, 2, 2, 2)
        kw = {"id": 2, "width": 2, "height": 2, "x": 2, "y": "y"}
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(**kw)

    def test_update_with_zero_y_kwargs(self):
        s1 = Square(1, 2, 2, 2)
        kw = {"id": 2, "width": 2, "height": 2, "x": 2, "y": -1}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(**kw)


class Test_Square_to_dictionary(unittest.TestCase):
    """ test if dictionary is returned
        ---1--- test for normal output
        ---2--- test with argument
    """

    """ ---1--- test for normal output """

    def test_to_dictioary(self):
        s1 = Square(3, 4, 5, 6)
        result = {"size": 3,
                "x": 4,
                "y": 5,
                "id": 6}
        self.assertEqual(s1.to_dictionary(), result)

    """ ---2--- test with argument """
    def test_to_dictioary_with_argument(self):
        s1 = Square(2, 3, 5)
        with self.assertRaises(TypeError):
            s1.to_dictionary(2)


if __name__ == "__main__":
    unitters.main()