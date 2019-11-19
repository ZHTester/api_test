# encoding: utf-8

"""
# @Time    : 29/10/2019 2:34 下午
# @Author  : Function
# @FileName: common_util.py
# @Software: PyCharm

公共部分-预期结果实际结果对比操作 ···单一接口结果判断
"""
class Compared:
    @staticmethod
    def is_contain(str_one, str_two):
        """
        判断一个字符是否在另一个字符串中
        :param str_one: 查找的字符串
        :param str_two: 被查找的字符串
        :return:
        """

        if str(str_one) in str(str_two):
            flag = True
        else:
            flag = False
        return flag
