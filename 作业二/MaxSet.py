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
        self.sub_list = []

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
        for index in self.array_ls:
            if index >= 0:
                is_allneg = False
                break
            if index > max_item:
                max_item = index
        if is_allneg:
            return max_item
        # 如果不是
        total = 0
        total_length = len(self.array_ls)
        for i in range(total_length):
            total += self.array_ls[i]
            if total > self.result:
                self.result = total
                self.sub_list.append(i)
            elif total < 0:
                total = 0
                self.sub_list.clear()
        return self.result

    def get_sublist(self):
        """
        获得最大数组
        :return: 最大值集合
        """
        return self.sub_list


def main(the_set):
    """
    自动进行生成
    :param msa: 初始化过的MSA类
    :return:求得的值
    """
    msa = MSA()
    msa.get_set(in_set=the_set)
    return msa.sum_maxset()


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
    main(array_ls)
    print("最终结果是", main(array_ls))
