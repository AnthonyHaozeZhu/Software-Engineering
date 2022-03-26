# -*- coding: UTF-8 -*-
"""
@Project ：作业二 
@File ：try_unittest.py
@Author ：AnthonyZ
@Date ：2022/3/14 17:49
"""


import unittest
import MaxSet


class Testing(unittest.TestCase):
    """
    测试
    """

    def test_getsum(self):
        self.assertEqual(MaxSet.get_sum([-1, 2, 3, -4]), 5)
        self.assertEqual(MaxSet.get_sum([-1, 2, -5, 3, -4]), 3)
        self.assertEqual(MaxSet.get_sum([-1, 20, -5, 30, -4]), 45)
        self.assertEqual(MaxSet.get_sum([-2, -3, -5, -1, -9]), -1)

    def test_getlist(self):
        self.assertEqual(MaxSet.get_list([-1, 2, 3, -4]), [2, 3])
        self.assertEqual(MaxSet.get_list([-1, 2, -5, 3, -4]), [3])
        self.assertEqual(MaxSet.get_list([-1, 20, -5, 30, -4]), [20, -5, 30])
        self.assertEqual(MaxSet.get_list([-2, -3, -5, -1, -9]), [-1])

    def test_sum2D(self):
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
