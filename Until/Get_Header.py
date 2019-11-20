# encoding: utf-8

"""
# @Time    : 6/11/2019 4:59 下午
# @Author  : Function
# @FileName    : Get_Header.py
# @Software: PyCharm
"""
import time

from Base.Action_Interface import MethodInterface
from Data.Get_Data import GetData


class GetHeader:

    def __init__(self,sheetId):
        self.sign = MethodInterface(sheetId)
        self.getdata = GetData(sheetId)

    def get_qiantai_login(self,request_headers):
        """
        前台header获取方式
        :param request_headers:
        :return:
        """
        str_time = (str(time.time())[0:10]) + "000"
        request_headers.update({'timestamp': str_time, 'version': '1.0'})
        sign = self.sign.getSign(request_headers)
        dic_sign = {"sign": sign}
        request_headers.update(dic_sign)

    def get_houtai_login(self, request_headers,request_datas):
        """
        后台header获取方式
        :param request_datas:
        :param request_headers:
        :return:
        """
        str_time = (str(time.time())[0:10]) + "000"
        request_headers.update({'timestamp': str_time, 'version': '1.0'})
        sign = self.sign.getSign(request_headers)
        GoogleCode = self.sign.getGoogleCode()
        dic_sign = {"sign": sign}
        request_headers.update(dic_sign)
        request_datas.update({'code': GoogleCode})

