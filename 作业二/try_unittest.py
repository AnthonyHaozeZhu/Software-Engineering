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

    def test_main(self):
        self.assertEqual(MaxSet.main([-1, 2, 3, -4]), 5)
        self.assertEqual(MaxSet.main([-1, 2, -5, 3, -4]), 3)
        self.assertEqual(MaxSet.main([-1, 20, -5, 30, -4]), 45)
        self.assertEqual(MaxSet.main([-2, -3, -5, -1, -9]), -1)


