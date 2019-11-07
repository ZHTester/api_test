# encoding: utf-8

"""
# @Time    : 28/10/2019 3:23 下午
# @Author  : Function
# @FileName    : Data_Depend.py
# @Software: PyCharm

获取依赖数据   - json_path 提取出依赖数据

"""
import json
import time

from Config.setting import *
from Base.Action_Interface import MethodInterface
from Until.Get_Header import GetHeader
from Until.Opertion_Excle import OperExcel
from  Base.Opertion_Interface import RunMethod
from .Get_Data import GetData
from jsonpath_rw import jsonpath, parse


class DependentData:
    def __init__(self, CaseId,sheetId,up_date):
        self.update = up_date
        self.CaseId = CaseId
        self.oper_excel =OperExcel(sheetId)
        self.getdata = GetData(sheetId)
        self.sheetId = sheetId
        self.sign = MethodInterface(sheetId)
        self.get_hea = GetHeader(sheetId)

    def get_case_data_line(self):
        """
        获取caseID中的整行数据
        :return:
        """
        row_data = self.oper_excel.get_row_data(self.CaseId)
        return row_data

    def run_dependent(self):
        """
        运行依赖的caseID case request 请求
        :return:
        """
        run_method  = RunMethod(self.sheetId)
        row_num = self.oper_excel.get_row_num(self.CaseId)  # 获取caseID对应的行号
        request_data = self.getdata.get_request_data(row_num)  # 拿到请求数据
        request_url = self.getdata.get_url(row_num)
        request_header = self.getdata.get_is_header(row_num)
        request_sheader = self.getdata.get_is_sheader(row_num)
        request_method = self.getdata.get_is_requestMethod(row_num) # 拿到请求方法
        request_ba = self.getdata.get_before_after(row_num)

        if self.update is not None:
            request_data.update(self.update)

        if 'login/username' in request_url:
            self.get_hea.get_qiantai_login(request_header)
            self.get_hea.write_header_qh(row_num,request_header)

        if 'login/submit' in request_url:
            self.get_hea.get_houtai_login(request_header, request_data)
            self.getdata.write_header(row_num, str(request_header))

        if request_ba == 'a':
            res = run_method.run_main(request_method, url_pc + request_url, request_data, request_header)
        else:
            res = run_method.run_main(request_method, url_Htai + request_url, request_data, request_header)
        return json.loads(res)

    def get_data_for_key(self,row):
        """
        根据依赖的key 执行依赖的case想要返回后通过 json_path 提取出对应的数据
        :param row:
        :return:
        """
        global result1
        depend_value = [] # 从返回的json提取出来的值
        depend_data = self.getdata.get_depend_key(row)  # 获取json表达式
        if depend_data:
            depend_data = depend_data.split('>') # 分隔符可以填入多个表达式
            response_data = self.run_dependent()
            for depend_i in depend_data:
                json_exe = parse(depend_i)
                madle = json_exe.find(response_data)
                try:
                    result1 = [math.value for math in madle][0]
                    result1 = str(result1)
                    depend_value.append(result1)
                except IndexError as e:
                    pass
            return depend_value

