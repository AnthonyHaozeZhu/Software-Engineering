# -*- coding: UTF-8 -*-
"""
@Project ：作业二 
@File ：try_profile.py
@Author ：AnthonyZ
@Date ：2022/3/14 17:26
"""

import yappi
import numpy as np
import MaxSet


yappi.clear_stats()
test1 = [np.random.randint(1, 1000) for i in range(100000000)]
test2 = [np.random.rand() for i in range(100000000)]
test3 = [[np.random.randint(1, 1000) for i in range(10000)] for j in range(10000)]
yappi.start()
MaxSet.get_list(test1)
yappi.stop()
stats = yappi.convert2pstats(yappi.get_func_stats())
stats.sort_stats("cumulative")
stats.print_stats()

yappi.start()
MaxSet.get_list(test2)
yappi.stop()
stats = yappi.convert2pstats(yappi.get_func_stats())
stats.sort_stats("cumulative")
stats.print_stats()

yappi.start()
MaxSet.get_list(test3)
yappi.stop()
stats = yappi.convert2pstats(yappi.get_func_stats())
stats.sort_stats("cumulative")
stats.print_stats()
