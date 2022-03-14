# -*- coding: UTF-8 -*-
"""
@Project ：作业二
@File ：MaxSet.py
@Author ：AnthonyZ
@Date ：2022/3/14 16:08
"""


import numpy as np


class MSA:
    """
    用于计算集合中子集的最大值
    """

    def __init__(self):
        """
        启动函数
        """
        self.array_ls = []
        self.result = 0

    def get_set(self):
        """
        给集合赋值
        :return:
        """
        set_length = 0
        try:
            set_length = int(input('请输入集合长度:'))
        except ValueError:
            print("Error: 请输入整数")

        if set_length < 0:
            raise Exception("请输入大于0的整数")

        while set_length > 0:
            try:
                self.array_ls.append(int(input("请输入该集合的元素")))
                set_length -= 1
            except ValueError:
                print("Error: 请输入整数")
        self.array_ls = np.array(self.array_ls)

    def sum_maxset(self):
        """
        计算最大值集合
        :return: 最大值
        """
        while self.array_ls.shape != (0,):
            max_index = np.argmax(self.array_ls)
            if self.array_ls[max_index] < 0:
                break
            self.result += self.array_ls[max_index]
            self.array_ls = np.delete(self.array_ls, max_index)
        return self.result


# def main():
#     """
#     初始化该类
#     :return:
#     """
#     msa = MSA()
#     msa.get_set()
#     msa.sum_maxset()
#
#
# if __name__ == '__main__':
#     print("hello world!")
#     main()

msa = MSA()
msa.get_set()
msa.sum_maxset()