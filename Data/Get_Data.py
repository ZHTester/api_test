# encoding: utf-8

"""
# @Time    : 28/10/2019 1:59 下午
# @Author  : Function
# @FileName    : Get_Data.py
# @Software: PyCharm
"""

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
        case_Name = self.oper_excle.get_cell_value(row,int(case_name))
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
        获取测试依赖数据  ======---依赖返回数据---======
        :param row:
        :return:
        """
        depend_key = self.oper_excle.get_cell_value(row,int(data_depend))
        if depend_key == "":
            return None
        else:
            return depend_key

    def get_depend_field(self,row):
        """
        获取数据依赖字段  =====--数据依赖字段---====
        :param row:
        :return:
        """
        depend_data = self.oper_excle.get_cell_value(row,int(filed_depend)).split(">")
        if depend_data == '':
            return None
        else:
            return depend_data

    def get_request_data(self,row):
        """
        获取请求数据  ====---请求数据---====
        :param row:
        :return:
        """
        request_data = self.oper_excle.get_cell_value(row,int(data))

        if request_data == "":
            return None
        else:
            return request_data

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
    g = GetData(0)
    a = g.get_before_after(2)
    print(a)

