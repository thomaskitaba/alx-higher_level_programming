#!/usr/bin/python3
import unittest

max_integer = __import__('6-max_integer').max_integer

class max_integer_test(unittest.TestCase):

    """ check the list itself """

    def check_if_list(self):
        """ check if list is of type list """
        self.assertTrue(isinstance(list, list))

    def check_empty_list(self):
        """ check if list is empty """
        self.assertEqual(len(list), 0)
        self.assertListEqual(list, [])

    def check_list_content(self):
        """ check if list content is only number """
        self.assertTrue(all (isinstance(val, (int, float)) for val in list))

    """ Check for ordering of list elements """
    def identical_elements(self):
        """ List with identical_elements """
        test_list = [3, 3, 3, 3, 3]
        self.assertEqual(max_integer(test_list), 3)

    def ordered_elements(self):
        """ List with ordered_elements """
        test_list = [1, 3, 5, 7, 9]
        self.assertEqual(max_integer(test_list), 9)

    """ Check lsit with positive and negative content  """
    def list_with_positive_num(self):
        """ list with positive num """
        test_list = [1, 3, 5, 7, 9]
        self.assertEqual(max_integer(test_list), 9)

    def list_with_negative_num(self):
        """ list with negative num """
        test_list = [-1, -3, -5, -7, -9]
        self.assertEqual(max_integer(test_list), -1)

    def list_positive_negative_num(self):
        """list with positive and negative num """
        test_list = [-1, 3, -5, 7, -9]
        self.assertEqual(max_integer(test_list), 7)

    def single_number(self):
        """ max for a single number """
        test_list = [4]
        self.assertEqual(max_integer(test_list), 4)
