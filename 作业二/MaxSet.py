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
    array_ls = []
    result = 0

    def __init__(self, array_ls):
        """
        启动函数
        :param array_ls:输入的集合
        """
        self.array_ls = np.array(array_ls)
        self.result = 0

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


def main(in_ls):
    """
    主函数
    :param in_ls:
    :return: 最大值
    """
    msa = MSA(in_ls)
    return msa.sum_maxset()


if __name__ == '__main__':
    length = int(input("请输入数组长度:"))
    ls = []
    for i in range(length):
        ls.append(int(input()))
    print("最大值为:", main(ls))

