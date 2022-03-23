# -*- coding: UTF-8 -*-
"""
@Project ：作业二 
@File ：try_profile.py
@Author ：AnthonyZ
@Date ：2022/3/14 17:26
"""

import profile
import MaxSet
import numpy as np

test1 = list(np.random.randint(-50, 50, size=1000))
test2 = list(np.random.randint(-50, 50, size=1000))

test_module = MaxSet

# profile.run(test_module.get_list(test1))
profile.run(test_module.get_sum(the_set=test2))