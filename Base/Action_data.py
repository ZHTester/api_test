# encoding: utf-8

"""
# @Time    : 22/11/2019 2:29 下午
# @Author  : Function
# @FileName    : Action_data.py
# @Software: PyCharm

动态生成值  方法反射

"""
import datetime
import time


class ActionData:
    @staticmethod
    def ftime_three(*args):
        now = datetime.datetime.now()
        tmp = now + datetime.timedelta(days=-2)
        startDate = tmp.strftime("%Y-%m-%d") + " 00:00:00"
        return startDate

    @staticmethod
    def etime_now(*args):
        now = datetime.datetime.now()
        endDate = now.strftime("%Y-%m-%d") + " 00:00:00"
        return endDate

    @staticmethod
    def time_sleep(*args):
        time.sleep(3)

if __name__ == "__main__":
   a =  ActionData()
   a.ftime_three()
   a.etime_now()


