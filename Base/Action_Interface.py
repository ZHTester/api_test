# encoding: utf-8

"""
# @Time    : 28/10/2019 11:30 上午
# @Author  : Function
# @FileName    : ActionMe.py
# @Software: PyCharm

接口自动化测试 关键字方法
"""
import time
from hashlib import md5

from Base.Opertion_Interface import RunMethod
from Data.Get_Data import GetData
from Until.Common_Util import Compared
from Until.Opertion_Email import SEmail
from Config.setting import *


class MethodInterface:
    def __init__(self,sheetId):
        self.run_method = RunMethod(sheetId)
        self.get_data  = GetData(sheetId)
        self.comm = Compared()
        self.sendemail = SEmail()
        self.sheetId = sheetId

    def getSign(self):
        """
        获取签名
        :return:
        """
        global request_header
        row_line = self.get_data.get_case_lines()
        for i in range(1,row_line):
            is_run = self.get_data.get_is_run(i)
            if is_run:
                request_header = self.get_data.get_is_header(i)
                request_header = eval(request_header)
            try:
                str_time = (str(time.time())[0:10]) + "000"
                request_header.update({'timestamp': str_time, 'version': '1.0'})
                # 拼接字符串
                list_header = []
                for key in request_header:
                    list_header.append(key)
                    list_header.append('=')
                    list_header.append(request_header[key])
                    list_header.append('&')
                linkString = ''.join(list_header)[0:-1]
                # 生成签名
                secret = "global"
                str_sign = linkString + secret
                new_md5 = md5()
                new_md5.update(str_sign.encode(encoding='utf-8'))
                sign = new_md5.hexdigest()
                print('===----sin-----==is:', sign)
                return sign
            except Exception as e:
                print("=======----错误的参数----=======:".format(e))
                raise

if __name__ == '__main__':
    a = MethodInterface(0)
    a.getSign()