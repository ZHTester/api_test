# encoding: utf-8

"""
# @Time    : 28/10/2019 11:03 上午
# @Author  : Function
# @FileName    : RunTest.py
# @Software: PyCharm

case执行主函数类
"""
import json

from Data.Get_Data import GetData
from Base.Opertion_Interface import RunMethod
from Data.qh_Compared import QianHouCompared
from Until.Common_Util import Compared
from Data.DA_Header import DependentDataHeader
from Data.DA_Request import DependentData
from Until.Opertion_Email import SEmail
from Until.Get_Header import GetHeader
from Base.Action_Interface import MethodInterface
from Until.Other_Function import OtherFunction
from Config.setting import *
from Base.Action_data import ActionData


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
        global data_response_v, data_rr_value, Compared_res, res
        # 单一接口统计
        pass_count = []
        fail_count = []
        # 前后端接口统计 单一数据
        c_pass_count = []
        c_fail_count = []
        # 前后端接口统计 单一数据
        d_pass_count = []
        d_fail_count = []

        row_line = self.get_data.get_case_lines()
        for i in range(1,row_line):
            is_run = self.get_data.get_is_run(i)
            if is_run:
                # ======---获取对应Excle中的数据---======
                caseNme =  self.get_data.get_case_name(i)
                request_url = self.get_data.get_url(i)
                request_data = self.get_data.get_request_data(i)
                request_expect = self.get_data.get_expected_data(i)
                request_method = self.get_data.get_is_requestMethod(i)
                request_header = self.get_data.get_is_header(i)
                request_ba = self.get_data.get_before_after(i)
                update_da = self.get_data.get_update_data(i)  # 拿到更新数据
                dependCase = self.get_data.get_is_depend(i)  # 拿到case依赖 执行依赖
                qh_response_data = self.get_data.get_qh_response_name_key(i)  # 拿到前后端需要执行的 case名称以及依赖表达式
                qh_response_key = self.get_data.get_qh_response_key(i) # 拿到当前执行行的依赖表达式
                dt_data = self.get_data.get_dt_data(i)  # 获取方法反射值
                """----------获取多数据形式------------"""
                a_expression_n = self.get_data.get_qh_a_expression_n(i)  # a关联场景接口-表达式(长度)
                b_expression_n = self.get_data.get_qh_b_expression_n(i)  # b本次执行场景接口-表达式(长度)
                a_expression = self.get_data.get_qh_a_expression(i)  # 关联场景接口-表达式(数据)
                b_expression = self.get_data.get_qh_b_expression(i)  #  本次场景接口-表达式(数据)

                # ======---判断是否有依赖case---======
                if dependCase is not None:
                    try:
                        c_name_index = []
                        dc = dependCase.split('<')
                        for caseN in dc:
                            kn = caseN.split('-')[0]
                            c_name = caseN.split('-')[1]
                            c_name_index.append(c_name)
                            name_index = c_name_index.index(c_name)

                            if kn[0] == '1':  # header - 依赖
                                depend_data_header = DependentDataHeader(c_name, self.sheetId,
                                                                         update_da)  # 初始化数据关联类 header
                                depend_key_header = self.get_data.get_depend_field(i, kn[0])  # key
                                data_response_value = depend_data_header.get_data_for_key(i,kn[0])  # 获取返回数据 value
                                data_r_value = data_response_value[0]
                                num_a = len(data_r_value)
                                for num in range(num_a):
                                    request_header[depend_key_header[num]] = data_r_value[num]
                                request_header.update(data_response_value[1])


                            if kn[0] == '2':  # 多个依赖 request_data依赖
                                depend_data_Request_data = DependentData(c_name, self.sheetId,
                                                                         update_da)  # 初始化数据关联类 requestData
                                depend_key_request_data = self.get_data.get_request_case_depend_key(i, kn[0],name_index)  # key
                                data_response_value = depend_data_Request_data.get_data_for_key(i,kn[0],name_index)  # 获取返回数据 value
                                if len(data_response_value) > 1:
                                    if data_response_value[1] is not None:
                                        data_rr_value =data_response_value[0]
                                        if dc[0].split('-')[0] == '1':
                                            if data_response_value[2]['token'] == '':
                                                request_header.update(data_response_value[2])
                                        else:
                                            request_header.update(data_response_value[2])
                                    num_a = len(data_rr_value)
                                    for num in range(num_a):
                                        request_data[depend_key_request_data[num]] = data_rr_value[num]
                                else:
                                    num_a = len(data_response_value)
                                    for num in range(num_a):
                                        request_data[depend_key_request_data[num]] = data_response_value[num]

                    except TypeError as e:
                        print('====系统维护==RunTest=1==错误信息>{0}===错误行>{1}'.format(e,i))
                    except IndexError as e:
                        print('====系统维护==RunTest=2==错误信息>{0}===错误行>{1}'.format(e,i))
                    except Exception as e:
                        self.get_data.write_result(i, '测试失败')
                        self.get_data.write_response(i, "依赖数据错误或返回数据错误---错误信息:%s---" % str(e))
                        raise

                if 'login/username' in request_url:
                    self.get_hea.get_qiantai_login(request_header)

                if 'login/submit' in request_url:
                    self.get_hea.get_houtai_login(request_header,request_data)

                if 'recharge/do/submit' in request_url:
                    uid = request_header['uid']
                    token = request_header['token']
                    device_id = request_header['device-id']
                    os_type = request_header['os-type']
                    timestamp = request_header['timestamp']
                    dic_submit = {"uid":uid,"token":token,"device-id": device_id,"os-type": os_type,"timestamp": timestamp}
                    request_data.update(dic_submit)

                # ========---单一接口执行接口测试请求---===========
                print('----------------------{0}-----------------'.format(caseNme))
                self.get_data.write_response(i, '')

                # ========-- 方法反射 --========
                if dt_data is not None:
                    getattr_method = ActionData()
                    excute_method = getattr(getattr_method, dt_data)
                    excute_method()

                if request_ba  == 'a':
                    res = self.run_method.run_main(request_method,url_pc+request_url,request_data,request_header)
                elif request_ba == 'b':
                    res = self.run_method.run_main(request_method, url_Htai+request_url, request_data, request_header)
                elif request_ba == 'x':
                    res = self.run_method.run_main(request_method, url_xht+request_url, request_data, request_header)
                print(res)
                print(request_data)


                if qh_response_data is not '':
                    # =====-----前后端返回接口数据对比 单一数据-----======
                    caseName_q = qh_response_data[0]  # 获取需要执行的用例名称
                    caseName_k = qh_response_data[1]  # 获取需要执行的用例关键字 key
                    run_depend_qh = QianHouCompared(caseName_q,self.sheetId)
                    d_Compared_q = run_depend_qh.run_qhInterface_key(caseName_k)  # 前端数据返回list
                    d_Compared_h = run_depend_qh.run_response_Interface_key(res1=res,depend_value=qh_response_key)  # 后端数据返回list
                    print(d_Compared_q,d_Compared_h)

                    # ======---前后端返回接口数据对比单一数据 判断场景是否执行成功---======
                    if d_Compared_q == d_Compared_h:
                        self.get_data.write_qh_response_result(i,'前后端接口数据一致:测试通过')
                        c_pass_count.append(i)
                    else:
                        self.get_data.write_qh_response_result(i, '前后端接口数据不一致:测试失败')
                        c_fail_count.append(i)

                    # =====-----场景接口前后台多数据对比逻辑-----======

                    if a_expression_n:
                        Compared_res = run_depend_qh.run_qhInterface()  # 返回数据
                        a_Compared = run_depend_qh.get_num_key(res=Compared_res, key1=a_expression_n,
                                                               key2=a_expression)  # 前关联数据
                        b_Compared = run_depend_qh.get_num_key(res=json.loads(res), key1=b_expression_n,
                                                               key2=b_expression)  # 后关联数据

                        # 多数据打印
                        print(a_Compared)
                        print('=======-----多数据---=============')
                        print(b_Compared)


                    # ======---前后端返回接口数据对比多数据 判断场景是否执行成功---======
                        if a_Compared == b_Compared:
                            self.get_data.write_qh_ab_result(i, '前后端接口数据一致:测试通过')
                            d_pass_count.append(i)
                        else:
                            self.get_data.write_qh_ab_result(i, '前后端接口数据不一致:测试失败')
                            d_fail_count.append(i)

                # ======---单一接口 执行断言操作判断接口是否执行成功---======
                if self.comm.is_contain(request_expect[0], request_expect[0],res):
                    self.get_data.write_result(i, '测试通过')
                    self.get_data.write_response(i, res)  #  写入正常数据
                    pass_count.append(i)
                else:
                    self.get_data.write_result(i, '测试失败')
                    self.get_data.write_response(i, res)  #  写入错误数据
                    fail_count.append(i)

        d_message = self.other_method.pass_fail_number(pass_count,fail_count,"单一接口自动化测试")  # 单一接口数据统计
        c_message = self.other_method.pass_fail_number(c_pass_count, c_fail_count, "前后端接口数据对比自动化测试")  # 前后端数据接口统计
        dd_message = self.other_method.pass_fail_number(d_pass_count, d_fail_count, "q前后端接口多数据对比自动化测试")  # 单一接口数据统计

        print(d_message)
        print(c_message)
        print(dd_message)

        # ======---发送邮件---======
        # self.sendemail.Email_UiTest(message,path_excle,OUT_FILENAME)
        print('======---本次接口测试结束---======')


if __name__ == "__main__":
    r = RunMain(0)
    r.go_run()










