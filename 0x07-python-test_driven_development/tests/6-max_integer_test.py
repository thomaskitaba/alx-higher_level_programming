#!/usr/bin/python3
""" unittest for max_integer function """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Diffrent catagories to test diffrent cases"""
    """ -------Check for ordering of list elements---- """

    def test_identical_elements(self):
        """ List with identical_elements """
        test_list = [3, 3, 3, 3, 3]
        self.assertEqual(max_integer(test_list), 3)

    def test_ordered_elements(self):  # TODO:
        """ List with ordered_elements """
        test_list = [1, 3, 5, 7, 9]
        self.assertEqual(max_integer(test_list), 9)

    def test_unordered_elements(self):  # TODO:
        """ List with unordered_elements """
        test_list = [5, 7, 9, 3, 1]
        self.assertEqual(max_integer(test_list), 9)

    """ ---------------------------------------------- """
    """ Check list with positive and negative content  """
    def test_list_with_positive_num(self):
        """ list with positive num """
        test_list = [1, 3, 5, 7, 9]
        self.assertEqual(max_integer(test_list), 9)

    def test_list_with_negative_num(self):
        """ list with negative num """
        test_list = [-1, -3, -5, -7, -9]
        self.assertEqual(max_integer(test_list), -1)

    def test_list_positive_negative_num(self):
        """list with positive and negative num """
        test_list = [-1, 3, -5, 7, -9]
        self.assertEqual(max_integer(test_list), 7)

    def test_single_number(self):  # TODO:
        """ max for a single number """
        test_list = [4]
        self.assertEqual(max_integer(test_list), 4)

    """ ---------------------------------------------- """
    """ ----------Check for float ---------"""

    def test_list_of_float(self):  # TODO:
        """ list with only floats """
        test_list = [-0.1, -0.5, -9.0, -7.2]
        self.assertEqual(max_integer(test_list), -0.1)

    def test_list_of_integers_and_float(self):  # TODO:
        """ list with float and integer """
        test_list = [1, 3.3, 3.5, -7, -9]
        self.assertEqual(max_integer(test_list), 3.5)
    """ ---------------------------------------------- """

    def test_string(self):
        """ string passed as argument """
        test_string = "thomas"
        self.assertEqual(max_integer(test_string), "thomas")
    """ -----------------------------------------------"""

    def test_string_list(self):
        """ test list with strings """
        list_string = ["abebe", "kebede", "feyissa", "zegeye"]
        self.assertEqual(max_integer(list_string), "zegeye")

    def test_empty_string(self):
        """ test for empty string """
        empty_string = ""
        self.assertEqual(max_integer(empty_string), None)

if __name__ == '__main__':
    unittest.main()
