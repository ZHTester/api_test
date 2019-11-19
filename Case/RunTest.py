# encoding: utf-8

"""
# @Time    : 28/10/2019 11:03 上午
# @Author  : Function
# @FileName    : RunTest.py
# @Software: PyCharm

case执行主函数类
"""
import json
import time

from Data.Get_Data import GetData
from Base.Opertion_Interface import RunMethod
from Until.Common_Util import Compared
from Data.Header_DA import DependentDataHeader
from Data.Request_DA import DependentData
from Until.Opertion_Email import SEmail
from Until.Get_Header import GetHeader
from Base.Action_Interface import MethodInterface
from Until.Other_Function import OtherFunction
from Config.setting import *

class RunMain:
    def __init__(self,sheetId):
        self.run_method = RunMethod(sheetId)
        self.get_data  = GetData(sheetId)
        self.comm = Compared()
        self.sendemail = SEmail()
        self.sheetId = sheetId
        self.get_hea = GetHeader(sheetId)
        self.sign = MethodInterface(sheetId)
        self.other_method = OtherFunction()

    def go_run(self):
        # ======----成功失败统计变量----=========
        global data_response_v,res, data_rr_value
        pass_count = []
        fail_count = []
        row_line = self.get_data.get_case_lines()
        for i in range(1,row_line):
            is_run = self.get_data.get_is_run(i)
            if is_run:
                # ======---获取对应Excle中的数据---======
                request_url = self.get_data.get_url(i)
                request_data = self.get_data.get_request_data(i)
                request_expect = self.get_data.get_expected_data(i)
                request_method = self.get_data.get_is_requestMethod(i)
                request_header = self.get_data.get_is_header(i)
                request_ba = self.get_data.get_before_after(i)
                update_da = self.get_data.get_update_data(i)  # 拿到更新数据
                dependCase = self.get_data.get_is_depend(i)  # 拿到case依赖 执行依赖

                # ======---判断是否有依赖case---======
                if dependCase is not None:
                    try:
                        dc = dependCase.split('<')
                        for caseN in dc:
                            kn = caseN.split('-')[0]
                            c_name = caseN.split('-')[1]
                            depend_data_header = DependentDataHeader(c_name,self.sheetId,update_da)   # 初始化数据关联类 header
                            depend_data_Request_data = DependentData(c_name, self.sheetId, update_da)  # 初始化数据关联类 requestData

                            if kn[0] == '1':  # header - 依赖
                                depend_key_header = self.get_data.get_depend_field(i, kn[0])  # key
                                data_response_value = depend_data_header.get_data_for_key(i,kn[0])  # 获取返回数据 value
                                num_a = len(data_response_value)
                                data_r_value = data_response_value[0]
                                for num in range(num_a):
                                    request_header[depend_key_header[num]] = data_r_value[num]
                                    request_header.update(data_response_value[1])

                            if kn[0] == '2':  # 多个依赖 request_data依赖
                                depend_key_request_data = self.get_data.get_request_case_depend_key(i, kn[0])  # key
                                data_response_value = depend_data_Request_data.get_data_for_key(i,kn[0])  # 获取返回数据 value
                                if data_response_value[1] is not None:
                                    data_rr_value =data_response_value[0]
                                    request_header.update(data_response_value[2])
                                num_a = len(data_rr_value)
                                for num in range(num_a):
                                    request_data[depend_key_request_data[num]] = data_rr_value[num]
                    except Exception as e:
                        self.get_data.write_result(i, '测试失败')
                        self.get_data.write_response(i, "依赖数据错误或返回数据错误---错误信息:%s---" % str(e))
                        raise

                if 'login/username' in request_url:
                    self.get_hea.get_qiantai_login(request_header)

                if 'login/submit' in request_url:
                    self.get_hea.get_houtai_login(request_header,request_data)

                # ========---执行接口测试请求---===========
                self.get_data.write_response(i, '')
                if request_ba  == 'a':
                    res = self.run_method.run_main(request_method,url_pc+request_url,request_data,request_header)
                else:
                    res = self.run_method.run_main(request_method, url_Htai+request_url, request_data, request_header)
                    print('-------------------{0}---------------------'.format(i))
                    print(request_data)

                # ======---执行断言操作判断接口是否执行成功---======
                if self.comm.is_contain(request_expect, res):
                    self.get_data.write_result(i, '测试通过')
                    self.get_data.write_response(i, res)  #  写入正常数据
                    pass_count.append(i)
                else:
                    self.get_data.write_result(i, '测试失败')
                    self.get_data.write_response(i, res)  #  写入错误数据
                    fail_count.append(i)

        # message = pass_fail_number(pass_count,fail_count)

        # ======---发送邮件---======
        # self.sendemail.Email_UiTest(message,path_excle,OUT_FILENAME)


        print('======---本次接口测试结束---======')


if __name__ == "__main__":
    r = RunMain(0)
    r.go_run()


















