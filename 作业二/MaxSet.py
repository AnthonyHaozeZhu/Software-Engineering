# -*- coding: UTF-8 -*-
"""
@Project ：作业二
@File ：MaxSet.py
@Author ：AnthonyZ
@Date ：2022/3/14 16:08
"""
from ast import literal_eval

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
        self.sub_index = []
        self.shape = 0

    def get_set(self, in_set):
        """
        给集合赋值
        :return:
        """
        self.array_ls = in_set
        self.shape = len(np.array(self.array_ls).shape)

    def sum_maxset(self):
        """
        对其进行处理
        :return:
        """
        if self.shape == 1:
            return self.max_list(self.array_ls)
        if self.shape == 2:
            temp_sum = float('-inf')
            for i in range(len(self.array_ls)):
                temp_list = [0 for temp in range(len(self.array_ls[0]))]
                for j in range(i, len(self.array_ls)):
                    for h_index in range(len(self.array_ls[0])):
                        temp_list[h_index] += self.array_ls[j][h_index]
                    temp_max = self.max_list(temp_list)
                    if temp_max > temp_sum:
                        temp_sum = temp_max
            self.result = temp_sum
            return self.result

        print("程序出错")
        return TypeError

    def max_list(self, temp_list):
        """
        计算一维数组最大值集合
        :return: 最大值
        """
        # 判断是否全为负数
        max_item = float('-inf')
        is_allneg = True
        total_length = len(temp_list)
        for j in range(total_length):
            if temp_list[j] >= 0:
                is_allneg = False
                self.sub_index.clear()
                break
            if temp_list[j] > max_item:
                max_item = temp_list[j]
                self.sub_index.clear()
                self.sub_index.append(j)
        if is_allneg:
            return max_item
        # 如果不是
        total = 0
        for i in range(total_length):
            total += temp_list[i]
            if total >= self.result:
                self.result = total
                self.sub_index.append(i)
            elif total < 0:
                total = 0
                if i != total_length - 1:
                    self.sub_index.clear()
        return self.result

    def get_sublist(self):
        """
        获得最大数组
        :return: 最大值集合
        """
        return self.array_ls[self.sub_index[0]: self.sub_index[-1] + 1]


def get_sum(the_set):
    """
    自动进行生成
    :param the_set:要处理的集合
    :return: 求得的值
    """
    msa = MSA()
    msa.get_set(in_set=the_set)
    return msa.sum_maxset()


def get_list(the_set):
    """
    :param the_set: 要处理的集合
    :return:最大的数组集合
    """
    msa = MSA()
    msa.get_set(in_set=the_set)
    if msa.shape == 2:
        return "暂不支持本功能，敬请期待！"
    msa.sum_maxset()
    return msa.get_sublist()

def get_in():
    """
    输入函数，包括错误处理
    :return: 输入的矩阵
    """
    array_ls = []
    try:
        array_ls = literal_eval(input("请输入矩阵或向量，输入格式参照[[1, 2 ,3], [4, 5, 6]]或[1, 2, 3, 4], [1, 2, 3, 4]:"))
    except (SyntaxError, ValueError):
        print("非法输入!")
    except TypeError:
        print("请按照格式输入！")
    if isinstance(array_ls, tuple):
        array_ls = list(array_ls)
    elif isinstance(array_ls, int):
        array_ls = [array_ls]
    if isinstance(array_ls, list):
        temp = np.array(array_ls)
        if len(temp.shape) == 1:
            for index in array_ls:
                try:
                    assert isinstance(index, (int, float))
                except AssertionError:
                    print("非法输入!")
        elif len(temp.shape) == 2:
            for index_1 in array_ls:
                for index_2 in index_1:
                    try:
                        assert isinstance(index_2, (int, float))
                    except AssertionError:
                        print("非法输入!")
        else:
            print("Sorry!本程序现在仅支持一维或二维数组")
            return TypeError
    else:
        print("非法输入!")
        return TypeError
    return array_ls


if __name__ == '__main__':
    temp_ls = get_in()
    result_sum = get_sum(temp_ls)
    result_list = get_list(temp_ls)
    print("最大子数组的和是：", result_sum)
    print("最大子数组是：", result_list)
