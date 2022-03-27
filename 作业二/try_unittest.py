# -*- coding: UTF-8 -*-
"""
@Project ：作业二 
@File ：try_unittest.py
@Author ：AnthonyZ
@Date ：2022/3/14 17:49
"""


import unittest
import MaxSet
from unittest.mock import patch


class Testing(unittest.TestCase):
    """
    测试
    """

    def test_getsum(self):
        self.assertEqual(MaxSet.get_sum([-1, 2, 3, -4]), 5)
        self.assertEqual(MaxSet.get_sum([1, 2, 3, 4]), 10)
        self.assertEqual(MaxSet.get_sum([-1, 2, -5, 3, -4]), 3)
        self.assertEqual(MaxSet.get_sum([-1, 20, -5, 30, -4]), 45)
        self.assertEqual(MaxSet.get_sum([-2, -3, -5, -1, -9]), -1)
        self.assertEqual(MaxSet.get_sum([-2.0, -3.0, -5.0, -1.0, -9.0]), -1)
        self.assertEqual(MaxSet.get_sum([-2.0, -3.0, -5.0, -1, -9]), -1)

    def test_getlist(self):
        self.assertEqual(MaxSet.get_list([-1, 2, 3, -4]), [2, 3])
        self.assertEqual(MaxSet.get_list([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(MaxSet.get_list([-1, 2, -5, 3, -4]), [3])
        self.assertEqual(MaxSet.get_list([-1, 20, -5, 30, -4]), [20, -5, 30])
        self.assertEqual(MaxSet.get_list([-1.0, 20.0, -5.0, 30.0, -4.0]), [20.0, -5.0, 30.0])
        self.assertEqual(MaxSet.get_list([-1.0, 20.0, -5, 30, -4]), [20.0, -5, 30])
        self.assertEqual(MaxSet.get_list([-2, -3, -5, -1, -9]), [-1])

    def test_sum2D(self):
        self.assertEqual(MaxSet.get_sum([[-1, -1],
                                         [-1, -1]]), -1)
        self.assertEqual(MaxSet.get_sum([[1, 1],
                                         [1, 1]]), 4)
        self.assertEqual(MaxSet.get_sum([[-15, -21, 5, -12],
                                         [-7, 21, 20, 12],
                                         [21, 0, -1, 13],
                                         [10, 20, -10, -18]]), 81)
        self.assertEqual(MaxSet.get_sum([[3, 6, 8, 9],
                                         [2, 5, 1, 8],
                                         [4, 7, 3, 9]]), 65)
        self.assertEqual(MaxSet.get_sum([[10, 1, 2, 3, 34],
                                         [1, -1, -3, -5, 98],
                                         [-8, 9, 7, -2, 2]]), 148)
        self.assertEqual(MaxSet.get_sum([[10, 1, 2, 3, 34],
                                         [1, 23, -3, -5, -34],
                                         [-8, 9, 7, -31, 2]]), 50)
        self.assertEqual(MaxSet.get_sum([[10, 1, -50, 3, 34],
                                         [-3, 25, 25, 50, -34],
                                         [-8, 9, 7, -31, -2]]), 100)
        self.assertEqual(MaxSet.get_sum([[10, 1, -50, 3, 34],
                                         [-3, 25, -25, 50, -34],
                                         [-8, 9, 7, -31, -2]]), 53)

        self.assertEqual(MaxSet.get_sum([[10.0, 1.0, -50.0, 3.0, 34.0],
                                         [-3, 25, -25, 50, -34],
                                         [-8, 9, 7, -31, -2]]), 53)

        self.assertEqual(MaxSet.get_sum([[10.0, 1.0, -50.0, 3.0, 34.0],
                                         [-3.0, 25.0, -25.0, 50.0, -34.0],
                                         [-8.0, 9.0, 7.0, -31.0, -2.0]]), 53)

    @patch('builtins.input')
    def test_in(self, mock_input):
        mock_input.return_value = '1'
        self.assertEqual(MaxSet.get_in(), [1])

        mock_input.return_value = '[1, 2]'
        self.assertEqual(MaxSet.get_in(), [1, 2])

        mock_input.return_value = '1, 2'
        self.assertEqual(MaxSet.get_in(), [1, 2])

        mock_input.return_value = '[[1, 2], [3, 4]]'
        self.assertEqual(MaxSet.get_in(), [[1, 2], [3, 4]])

        mock_input.return_value = '[1, 2], [3, 4]'
        self.assertEqual(MaxSet.get_in(), [[1, 2], [3, 4]])

        mock_input.return_value = '(1, 2)'
        self.assertEqual(MaxSet.get_in(), [1, 2])

    @patch('builtins.input')
    @unittest.expectedFailure
    def test_error(self, mock_input):
        self.assertEqual(MaxSet.get_sum([[[10.0, 1.0, -50.0, 3.0, 34.0],
                                         [-3.0, 25.0, -25.0, 50.0, -34.0],
                                         [-8.0, 9.0, 7.0, -31.0, -2.0]], [[1]]]), 53)

        mock_input.return_value = '[1, 2 ,'
        self.assertEqual(MaxSet.get_in(), 1)

        mock_input.return_value = '[[-50.0, 3.0, 34.0], ' \
                                  '[-3.0, 25.0, -25.0, 50.0, -34.0], [-8.0, 9.0, 7.0, -31.0, -2.0]])'
        self.assertEqual(MaxSet.get_in(), 53)

        mock_input.return_value = "['a', 'b', 'c']"
        self.assertEqual(MaxSet.get_in(), 1)

