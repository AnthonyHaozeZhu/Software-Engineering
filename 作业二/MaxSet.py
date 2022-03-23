# -*- coding: UTF-8 -*-
"""
@Project ：作业二
@File ：MaxSet.py
@Author ：AnthonyZ
@Date ：2022/3/14 16:08
"""


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

    def get_set(self, in_set):
        """
        给集合赋值
        :return:
        """
        self.array_ls = in_set

    def sum_maxset(self):
        """
        计算最大值集合
        :return: 最大值
        """
        # 判断是否全为负数
        max_item = float('-inf')
        is_allneg = True
        total_length = len(self.array_ls)
        for index in range(total_length):
            if self.array_ls[index] >= 0:
                is_allneg = False
                self.sub_index.clear()
                break
            if self.array_ls[index] > max_item:
                max_item = self.array_ls[index]
                self.sub_index.clear()
                self.sub_index.append(index)
        if is_allneg:
            return max_item
        # 如果不是
        total = 0
        for i in range(total_length):
            total += self.array_ls[i]
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
    msa.sum_maxset()
    return msa.get_sublist()


if __name__ == '__main__':
    array_ls = []
    try:
        length = int(input('请输入集合长度:'))
    except ValueError:
        print("Error: 请输入整数")

    if length < 0:
        raise Exception("请输入大于0的整数")

    while length > 0:
        try:
            array_ls.append(int(input("请输入该集合的元素")))
            length -= 1
        except ValueError:
            print("Error: 请输入整数")
    result_sum = get_sum(array_ls)
    result_list = get_list(array_ls)
    print("最大子数组的和是：", result_sum)
    print("最大子数组是：", result_list)
