# encoding: utf-8

"""
# @Time    : 28/10/2019 11:10 上午
# @Author  : Function
# @FileName    : Other_Function.py
# @Software: PyCharm

其余相关工具类方法
"""
import time


class OtherFunction:


    def pass_fail_number(self,pass_list,fail_list,title):
        """
        发送消息
        :return:
        """
        pass_num = float(len(pass_list))  # 百分比就是float 也就是浮点类型
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num  # 测试用例总数
        # 90%
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)

        content = ["[**********"+title+"**********]:",
                   "本次接口自动化测试总接口数量为:%s" % count_num,
                   "*1*通过个数为:%s个" % pass_num,
                   "*2*失败个数为:%s个" % fail_num,
                   "*3*通过率为:%s" % pass_result,
                   "*4*失败率为:%s"%fail_result
                   ]

        msg = '\n'.join(content)
        return  msg

    def key_segmentation(self,request_header_data):
        """
        关联数据拆分
        :param request_header_data:  1-data.token>data.userId<2-data.token>data.userId
        :return:
        """
        header_data = None
        request_data = None
        request_header_data = request_header_data.split("<")
        try:
            header_data = request_header_data[0].split('-')  # 拆分出的header请求数据  '1', 'data.token>data.userId'
            request_data = request_header_data[1].split('-') # 拆分出的request_data请求数据  '2', 'data.token>data.userId'
        except IndexError as e:
            print('没有请求数据',e)
        return header_data,request_data