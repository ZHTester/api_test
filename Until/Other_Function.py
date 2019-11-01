# encoding: utf-8

"""
# @Time    : 28/10/2019 11:10 上午
# @Author  : Function
# @FileName    : Other_Function.py
# @Software: PyCharm

其余相关工具类方法
"""
def pass_fail_number(pass_list,fail_list):
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


    content = ["[**********接口自动化测试**********]:",
               "本次接口自动化测试总接口数量为:%s" % count_num,
               "*1*通过个数为:%s个" % pass_num,
               "*2*失败个数为:%s个" % fail_num,
               "*3*通过率为:%s" % pass_result,
               "*4*失败率为:%s"%fail_result
               ]

    msg = '\n'.join(content)
    return  msg
