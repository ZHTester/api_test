# encoding: utf-8

"""
# @Time    : 28/10/2019 3:23 下午
# @Author  : Function
# @FileName    : Data_Depend.py
# @Software: PyCharm

获取依赖数据   - json_path 提取出依赖数据  获取Header的依赖数据

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


class DependentDataHeader:
    def __init__(self, CaseId,sheetId,up_date):
        self.update = up_date
        self.CaseId = CaseId
        self.oper_excel =OperExcel(sheetId)
        self.getdata = GetData(sheetId)
        self.sheetId = sheetId
        self.sign = MethodInterface(sheetId)
        self.get_hea = GetHeader(sheetId)

    def get_case_data_line(self,CaseId=None):
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
        row_num = self.oper_excel.get_row_num(self.CaseId)  # 获取 casename 对应的行号
        request_data = self.getdata.get_request_data(row_num)  # 拿到请求数据
        request_url = self.getdata.get_url(row_num)
        request_header = self.getdata.get_is_header(row_num)
        request_method = self.getdata.get_is_requestMethod(row_num) # 拿到请求方法
        request_ba = self.getdata.get_before_after(row_num)

        if 'login/username' in request_url:
            self.get_hea.get_qiantai_login(request_header)
            if self.update is not None:
                request_data.update(self.update)

        if 'login/submit' in request_url:
            self.get_hea.get_houtai_login(request_header, request_data)

        if request_ba == 'a':
            res = run_method.run_main(request_method, url_pc + request_url, request_data, request_header)
        else:
            res = run_method.run_main(request_method, url_Htai + request_url, request_data, request_header)
        return json.loads(res),request_header

    def get_data_for_key(self,row,num_dk):
        """
        根据依赖的key 执行依赖的case想要返回后通过 json_path 提取出对应的数据
        :param num_dk:
        :param row:
        :return:
        """
        global result1,depend_value
        depend_value = [] # 从返回的json提取出来的值
        depend_data = self.getdata.get_depend_key(row).split("<")  # 获取json表达式
        if depend_data:
            for key_num in depend_data:
                kn = key_num.split('-')
                if kn[0] == num_dk:
                    depend_data  = kn[1].split(">") # 分隔符可以填入多个表达式
                    response_data = self.run_dependent()
                    for depend_i in depend_data:
                        json_exe = parse(depend_i)  # 获取对表达式
                        madle = json_exe.find(response_data[0])  # 使用json_path获取数据
                        try:
                            result1 = [math.value for math in madle][0]
                            result1 = str(result1)
                            depend_value.append(result1)
                        except IndexError as e:
                            pass
                    return depend_value,response_data[1]


