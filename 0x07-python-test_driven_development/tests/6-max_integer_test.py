#!/usr/bin/python3
""" unittest for max_integer function """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Diffrent catagories to test diffrent cases"""
    """ -----------check the list itself-------------- """

    def test_if_list(self):
        """ check if list is of type list """
        self.assertTrue(isinstance(list, list))

    def test_empty_list(self):
        """ check if list is empty or with zero elements """
        self.assertEqual(len(list), 0)
        self.assertListEqual(list, [])

    def test_list_content(self):
        """ check if list content is integer or float number """
        self.assertTrue(not all(isinstance(val, (int, float)) for val in list))

    """ ---------------------------------------------- """
    """ -------Check for ordering of list elements---- """
    def test_identical_elements(self):
        """ List with identical_elements """
        test_list = [3, 3, 3, 3, 3]
        self.assertEqual(max_integer(test_list), 3)

    def test_ordered_elements(self):
        """ List with ordered_elements """
        test_list = [1, 3, 5, 7, 9]
        self.assertEqual(max_integer(test_list), 9)

    def test_unordered_elements(self):
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

    def test_single_number(self):
        """ max for a single number """
        test_list = [4]
        self.assertEqual(max_integer(test_list), 4)

    """ ---------------------------------------------- """
    """ ----------Check for float ---------"""
    def test_list_of_float(self):
        """ list with only floats """
        test_list = [-0.1, -0.5, -9.0, -7.2]
        self.assertEqual(max_integer(test_list), -0.1)

    def test_list_of_integers_and_float(self):
        """ list with float and inteter """
        test_list = [1, 3.3, 3.5, -7, -9]
        self.assertEqual(max_integer(test_list), 3.5)
    """ ---------------------------------------------- """

if __name__ == '__main__':
    unittest.main()
