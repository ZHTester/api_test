# encoding: utf-8

"""
# @Time    : 28/10/2019 11:03 上午
# @Author  : Function
# @FileName    : RunTest.py
# @Software: PyCharm

case执行主函数类
"""
from Data.Get_Data import GetData
from Base.Opertion_Interface import RunMethod
from Until.Common_Util import Compared
from Data.Data_Depend import DependentData
from Until.Opertion_Email import SEmail
from Until.Other_Function import pass_fail_number
from Config.setting import *

class RunMain:
    def __init__(self,sheetId):
        self.run_method = RunMethod()
        self.get_data  = GetData(sheetId)
        self.comm = Compared()
        self.sendemail = SEmail()
        self.sheetId = sheetId

    def go_run(self):
        # ======----成功失败统计变量----=========
        pass_count = []
        fail_count = []
        row_line = self.get_data.get_case_lines()
        for i in range(1,row_line):
            is_run = self.get_data.get_is_run(i)
            if is_run:
                # ======---获取对应Excle中的数据---======
                url = self.get_data.get_url(i)
                request_data = self.get_data.get_request_data(i)
                expect = self.get_data.get_expected_data(i)
                method = self.get_data.get_is_requestMethod(i)
                header = self.get_data.get_is_header(i)
                dependCase = self.get_data.get_is_depend(i)  # 拿到case依赖 执行依赖

                # ======---判断是否有依赖case---======
                if dependCase is not None:
                    """
                    异常捕获 返回的异常写入到Excel
                    """
                    try:
                        depend_data = DependentData(dependCase, self.sheetId)   # 初始化数据关联类
                        data_response_key = depend_data.get_data_for_key(i)
                        depend_key = self.get_data.get_depend_field(i)
                        request_data[depend_key] = data_response_key
                    except Exception as e:
                        self.get_data.write_result(i, "依赖数据未在Response中找到或表达式错误****错误信息:%s" % str(e))
                        print("catch Error", e)
                        continue

                # ======---执行接口测试请求---======
                res = self.run_method.run_main(method,url,request_data,header)

                if self.comm.is_contain(expect, res):
                    # print('******测试通过********')
                    self.get_data.write_result(i, 'pass')
                    pass_count.append(i)
                else:
                    # 如果失败了就把失败的返回信息打印出来
                    self.get_data.write_result(i, res)
                    fail_count.append(i)


            pass_count = len(pass_count)
            fail_count = len(fail_count)
            message = pass_fail_number(pass_count,fail_count)
            self.sendemail.Email_UiTest(message,path_excle,OUT_FILENAME)


if __name__ == "__main__":
    r = RunMain(0)
    r.go_run()


















