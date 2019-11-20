# encoding: utf-8

"""
# @Time    : 19/11/2019 7:18 下午
# @Author  : Function
# @FileName    : qh_Compared.py
# @Software: PyCharm

前后端接口对比 依赖执行脚本

"""
import json

from jsonpath_rw import jsonpath, parse

from Base.Opertion_Interface import RunMethod
from Data.DA_Header import DependentDataHeader
from Data.DA_Request import DependentData
from Data.Get_Data import GetData
from Until.Opertion_Excle import OperExcel
from Config.setting import *


class QianHouCompared:
    def __init__(self,Cass_name,sheetId):
        self.oper_excel = OperExcel(sheetId)
        self.sheetId = sheetId
        self.Cass_name = Cass_name
        self.get_data = GetData(sheetId)



    def run_qhInterface(self):
        """
         运行前后台关联的用例
        :return:
        """
        global data_rr_value
        run_method  = RunMethod(self.sheetId)
        row_num = self.oper_excel.get_row_num(self.Cass_name)  # 获取 casename 对应的行号
        request_url = self.get_data.get_url(row_num)  # 获取到对应的url
        request_data = self.get_data.get_request_data(row_num) # 获取到对应的请求数据
        request_method = self.get_data.get_is_requestMethod(row_num)
        request_header = self.get_data.get_is_header(row_num) # 获取到对应的header
        dependCase = self.get_data.get_is_depend(row_num)  # 拿到case依赖 执行依赖
        update_da = self.get_data.get_update_data(row_num)  # 拿到更新数据
        request_ba = self.get_data.get_before_after(row_num)

        if dependCase is not None:
            try:
                dc = dependCase.split('<')
                for caseN in dc:
                    kn = caseN.split('-')[0]
                    c_name = caseN.split('-')[1]
                    depend_data_header = DependentDataHeader(c_name, self.sheetId, update_da)  # 初始化数据关联类 header
                    depend_data_Request_data = DependentData(c_name, self.sheetId,update_da)  # 初始化数据关联类 requestData

                    if kn[0] == '1':  # header - 依赖
                        depend_key_header = self.get_data.get_depend_field(row_num, kn[0])  # key
                        data_response_value = depend_data_header.get_data_for_key(row_num, kn[0])  # 获取返回数据 value
                        data_r_value = data_response_value[0]
                        num_a = len(data_r_value)
                        for num in range(num_a):
                            request_header[depend_key_header[num]] = data_r_value[num]
                            request_header.update(data_response_value[1])

                    if kn[0] == '2':  # 多个依赖 request_data依赖
                        depend_key_request_data = self.get_data.get_request_case_depend_key(row_num, kn[0])  # key
                        data_response_value = depend_data_Request_data.get_data_for_key(row_num, kn[0])  # 获取返回数据 value
                        if data_response_value[1] is not None:
                            data_rr_value = data_response_value[0]
                            request_header.update(data_response_value[2])
                        num_a = len(data_rr_value)
                        for num in range(num_a):
                            request_data[depend_key_request_data[num]] = data_rr_value[num]
            except Exception as e:
                self.get_data.write_result(row_num, '测试失败')
                self.get_data.write_response(row_num, "依赖数据错误或返回数据错误---错误信息:%s---" % str(e))
                raise

        if request_ba == 'a':
            res = run_method.run_main(request_method, url_pc + request_url, request_data, request_header)
        else:
            res = run_method.run_main(request_method, url_Htai + request_url, request_data, request_header)
        return json.loads(res)

    def run_qhInterface_key(self,depend_value):
        depend_value1 = []
        depend_data = depend_value.split(">")  # 获取json表达式
        if data_depend:
            response_data = self.run_qhInterface()
            for depend_i in depend_data:
                json_exe = parse(depend_i)  # 获取对表达式
                madle = json_exe.find(response_data)  # 使用json_path获取数据
                try:
                    result1 = [math.value for math in madle][0]
                    result1 = str(result1)
                    depend_value1.append(result1)
                except IndexError as e:
                    pass
            return depend_value1

    @staticmethod
    def run_response_Interface_key(res1, depend_value):
        depend_value1 = []
        res1 = json.loads(res1)
        depend_data = depend_value.split(">")  # 获取json表达式
        if data_depend:
            for depend_i in depend_data:
                json_exe = parse(depend_i)  # 获取对表达式

                madle = json_exe.find(res1)  # 使用json_path获取数据
                try:
                    result1 = [math.value for math in madle][0]
                    result1 = str(result1)
                    depend_value1.append(result1)
                except IndexError as e:
                    pass
            return depend_value1
