# encoding: utf-8

"""
# @Time    : 7/11/2019 11:15 上午
# @Author  : Function
# @FileName    : test.py
# @Software: PyCharm
测试文件
"""
a = '1-data.token>data.userId<1-data.token>data.userId'
h = None
q = None
try:
    a = a.split("<")
    h = a[0].split('-')
    q = a[1].split('-')
except IndexError as e:
    print('没有请求数据')

print(a)
print(h[1].split(">")[0])
print(q)
