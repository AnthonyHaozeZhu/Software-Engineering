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
