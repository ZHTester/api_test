# encoding: utf-8

"""
# @Time    : 28/10/2019 1:59 下午
# @Author  : Function
# @FileName    : Get_Data.py
# @Software: PyCharm
"""
import datetime
import os

from Until.Opertion_Excle import OperExcel
from Config.setting import *


class  GetData:
    def __init__(self,sheetId):
        self.oper_excle = OperExcel(sheetId)


    def get_case_lines(self):
        """
        获取case数量
        :return:
        """
        return self.oper_excle.get_lines()

    def get_before_after(self,row):
        """
        获取属于哪个端  ====---获取前后端---====
        :param row:
        :return:
        """
        before_after = self.oper_excle.get_cell_value(row,int(be_after))
        return before_after

    def get_case_name(self,row):
        """
        获取caseName  ====---用例名称---====
        :param row:
        :return:
        """
        case_Name = self.oper_excle.get_cell_value(row,int(case_id))
        return case_Name

    def get_url(self,row):
        """
        获取请求数据url  ====---获取url---=====
        :param row:
        :return:
        """
        url_mode = self.oper_excle.get_cell_value(row,int(url))
        return url_mode

    def get_is_run(self,row):
        """
        获取是否运行  ===----是否执行-----====
        :param row:
        :return:
        """
        run_mode = self.oper_excle.get_cell_value(row,int(run))
        if run_mode == "yes":
            flag = True
        else:
            flag = False
        return flag

    def get_is_requestMethod(self,row):
        """
        获取请求方法 ====---请求方式----====
        :param row:
        :return:
        """
        request_way_mode = self.oper_excle.get_cell_value(row,int(request_way))
        return request_way_mode

    def get_is_header(self,row):
        """
        获取header ====---header---=====
        :param row:
        :return:
        """
        header_mode = self.oper_excle.get_cell_value(row,int(header))
        if header_mode is not '':
            header_mode = eval(header_mode)
        return header_mode

    def get_is_depend(self,row):
        """
        判断case是否有依赖  =====---case依赖----======
        :param row:
        :return:
        """
        depend_case_id = self.oper_excle.get_cell_value(row,int(case_depend))
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    def get_depend_key(self,row):
        """
        获取测试依赖数据  ======---依赖返回数据---====== 9
        :param row:
        :return:
        """
        depend_key = self.oper_excle.get_cell_value(row,int(data_depend))
        if depend_key == "":
            return None
        else:
            return depend_key

    def get_depend_field(self,row,k_num):
        """
        获取数据依赖字段  =====--数据依赖字段---==== 10
        :param k_num:
        :param row:
        :return: 1-token>uid   <2-goodsId
        """
        depend_data = self.oper_excle.get_cell_value(row, int(filed_depend)).split("<")
        for key_num in depend_data:
            kn = key_num.split('-')
            if kn[0] == k_num:
                depend_data = kn[1].split(">")
        if depend_data == '':
            return None
        else:
            return depend_data

    def get_qh_response_name_key(self,row):
        """
        获取前端接口返回值  返回测试用例名称 和 依赖key
        :param row:
        :return:
        """
        response_data_key = self.oper_excle.get_cell_value(row,int(q_name_depend_key)).split("<")

        if response_data_key != ['']:
            caseN = response_data_key[0]
            case_key = response_data_key[1]  # 数据1>数据2>数据3
            return caseN,case_key
        else:
            return ''

    def get_qh_response_key(self,row):
        """
        获取前端key
        :param row:
        :return:
        """
        response_data_key = self.oper_excle.get_cell_value(row,int(h_name_depend_key))
        if response_data_key:
            return response_data_key
        else:
            return None

    def write_qh_response_result(self,row,value):
        """
        前后端结果写入
        :param row:
        :return:
        """
        self.oper_excle.write_value(row, int(qh_result), value)



    def get_request_data(self,row):
        """
        获取请求数据  ====---请求数据---====
        :param row:
        :return:
        """
        request_data = self.oper_excle.get_cell_value(row,int(data))

        if request_data is not '' and request_data == '../Config/test.jpg':
            request_data = {'file': open(request_data, 'rb')}
            return request_data
        elif request_data is not '':
            request_data = eval(request_data)
            return request_data
        return  None

    def get_request_case_depend_value(self,row):
        """
        request_data 获取依赖数据的返回值 表达式
        :param row:
        :return:
        """
        depend_key = self.oper_excle.get_cell_value(row, int(request_case_depend_value))
        if depend_key == "":
            return None
        else:
            return depend_key

    def get_request_case_depend_key(self,row,k_num):
        """
        request_data 获取依赖数据的表达式
        :param k_num:
        :param row:
        :return: 1-token>uid   <2-goodsId
        """
        depend_data = self.oper_excle.get_cell_value(row, int(request_filed_depend_key)).split("<")
        for key_num in depend_data:
            kn = key_num.split('-')
            if kn[0] == k_num:
                depend_data = kn[1].split(">")
        if depend_data == '':
            return None
        else:
            return depend_data
    """==========================取出前后台多个数据进行 前后台数据对比=================================="""
    def get_qh_a_expression_n(self,row):
        """
        a关联场景接口-表达式(长度)
        :param row:
        :return:
        """
        aexpression_n = self.oper_excle.get_cell_value(row,int(qh_a_expression_n))
        if aexpression_n == '':
            return None
        return aexpression_n

    def get_qh_b_expression_n(self,row):
        """
        b本次执行场景接口-表达式(长度)
        :param row:
        :return:
        """
        bexpression_n = self.oper_excle.get_cell_value(row,int(qh_b_expression_n))
        if bexpression_n == '':
            return None
        return bexpression_n

    def get_qh_a_expression(self,row):
        """
        关联场景接口-表达式(数据)
        :param row:
        :return:
        """
        aexpression = self.oper_excle.get_cell_value(row,int(qh_a_expression))
        if aexpression == '':
            return None
        return aexpression

    def get_qh_b_expression(self,row):
        """
        本次场景接口-表达式(数据)
        :param row:
        :return:
        """
        bexpression = self.oper_excle.get_cell_value(row,int(qh_b_expression))
        if bexpression == '':
            return None
        return bexpression

    def write_qh_ab_result(self,row, value):
        """
        多个数据结果写入
        :param value:
        :param row:
        :return:
        """
        self.oper_excle.write_value(row, int(qh_ab_result), value)

    """---------------------------------------------------------------"""

    def get_expected_data(self,row):
        """
        获取预期数据 ==---预期结果---===
        :param row:
        :return:
        """
        expect_data = self.oper_excle.get_cell_value(row,int(expect))
        if expect_data == '':
            return None
        return expect_data

    def get_update_data(self,row):
        """
        获取更新数据
        :param row:
        :return:
        """
        Update_data = self.oper_excle.get_cell_value(row,int(update_data))
        if Update_data == '':
            return None
        Update_data = eval(Update_data)
        return Update_data

    def write_result(self,row,value):
        """
        写入实际结果 测试通过&&测试失败
        :param row:
        :param value:
        :return:
        """
        self.oper_excle.write_value(row, int(result), value)

    def write_response(self,row,value):
        """
        获取接口返回结果
        :param row:
        :param value:
        :return:
        """
        self.oper_excle.write_value(row,int(response_result),value)


if __name__ == '__main__':
    now = datetime.datetime.now()
    user_birthday = now.strftime("%Y-%m-%d")
    print(user_birthday)
