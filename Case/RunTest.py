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
from Base.Action_Interface import MethodInterface
from Config.setting import *

class RunMain:
    def __init__(self,sheetId):
        self.run_method = RunMethod(sheetId)
        self.get_data  = GetData(sheetId)
        self.comm = Compared()
        self.sendemail = SEmail()
        self.sheetId = sheetId
        self.sign = MethodInterface(sheetId)

    def go_run(self):
        # ======----成功失败统计变量----=========
        pass_count = []
        fail_count = []
        row_line = self.get_data.get_case_lines()
        for i in range(1,row_line):
            is_run = self.get_data.get_is_run(i)
            if is_run:
                # ======---获取对应Excle中的数据---======
                CaseN = self.get_data.get_case_name(i)
                request_url = self.get_data.get_url(i)
                request_data = self.get_data.get_request_data(i)
                request_expect = self.get_data.get_expected_data(i)
                request_method = self.get_data.get_is_requestMethod(i)
                request_header = self.get_data.get_is_header(i)
                request_ba = self.get_data.get_before_after(i)
                dependCase = self.get_data.get_is_depend(i)  # 拿到case依赖 执行依赖
                # ======---判断是否有依赖case---======
                if dependCase is not None:
                    try:
                        depend_data = DependentData(dependCase, self.sheetId)   # 初始化数据关联类
                        data_response_key = depend_data.get_data_for_key(i)
                        depend_key = self.get_data.get_depend_field(i)
                        request_data[depend_key] = data_response_key
                    except Exception as e:
                        self.get_data.write_result(i, '测试失败')
                        self.get_data.write_response(i, "依赖数据未在Response中找到或表达式错误****错误信息:%s" % str(e))
                        continue

                if 'login' in request_url:
                    request_header = eval(request_header)
                    sign = self.sign.getSign()
                    dic_sign = {"sign": sign}
                    request_header.update(dic_sign)
                else:
                    request_header = eval(request_header)

                # ======---执行接口测试请求---======
                if request_ba  == 'a':
                    request_data = eval(request_data)
                    res = self.run_method.run_main(request_method,url_pc+request_url,request_data,request_header)
                    print(res)
                else:
                    res = self.run_method.run_main(request_method, url_Htai + request_url, request_data, request_header)

                # ======---执行断言操作判断接口是否执行成功---======
                if self.comm.is_contain(request_expect, res):
                    self.get_data.write_result(i, '测试通过')
                    pass_count.append(i)
                else:
                    self.get_data.write_result(i, '测试失败')
                    self.get_data.write_response(i, res)  #  写入错误数据
                    fail_count.append(i)

        message = pass_fail_number(pass_count,fail_count)

        # ======---发送邮件---======
        # self.sendemail.Email_UiTest(message,path_excle,OUT_FILENAME)
        print('======---本次接口测试结束---======')


if __name__ == "__main__":
    r = RunMain(0)
    r.go_run()


















