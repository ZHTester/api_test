# encoding: utf-8

"""
# @Time    : 28/10/2019 3:23 下午
# @Author  : Function
# @FileName    : Data_Depend.py
# @Software: PyCharm
获取依赖数据   - json_path 提取出依赖数据 获取request_data依赖数据  关联性的接口

"""
import json
import time

from Config.setting import *
from Base.Action_Interface import MethodInterface
from Until.Get_Header import GetHeader
from Until.Opertion_Excle import OperExcel
from  Base.Opertion_Interface import RunMethod
from Data.Get_Data import GetData
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

    def get_Association_case(self,update_da=None):
        global dependCase
        """第一个接口关联运行方式"""
        run_method = RunMethod(self.sheetId)
        row_num = self.oper_excel.get_row_num(self.CaseId)  # 获取 casename 对应的行号
        dependCase = self.getdata.get_is_depend(row_num)  # 拿到case依赖执行依赖
        if "<" in dependCase:
            dependCase = dependCase.split("<")[0]

        dependCase = dependCase.split('-')[1]
        row_num_header = self.oper_excel.get_row_num(dependCase)  # 获取 casename 对应的行号

        "执行获取header的行号"
        request_data = self.getdata.get_request_data(row_num_header)  # 拿到请求数据
        request_url = self.getdata.get_url(row_num_header)
        request_ba = self.getdata.get_before_after(row_num)
        request_header = self.getdata.get_is_header(row_num_header)
        request_method = self.getdata.get_is_requestMethod(row_num_header)  # 拿到请求方法


        if self.update is not None:
            request_data.update(self.update)

        if 'login/username' in request_url:
            if update_da is not None:
                request_data.update(update_da)
            self.get_hea.get_qiantai_login(request_header)

        if 'login/submit' in request_url:
            self.get_hea.get_houtai_login(request_header, request_data)

        if request_ba == 'a':
            res = run_method.run_main(request_method, url_pc + request_url, request_data, request_header)
            res = json.loads(res)
            try:
                token1 = res['data']['token']
                uid = res['data']['id']
                request_header.update({'token': token1, 'uid': str(uid)})
                return request_header,row_num
            except Exception as e:
                self.getdata.write_result(row_num, '系统维护')
                print('====a系统维护=====错误信息>{0}===错误行>{1}'.format(e,row_num))
        elif request_ba == 'b':
            res = run_method.run_main(request_method, url_Htai + request_url, request_data, request_header)
            res = json.loads(res)
            try:
                token1 = res['data']['token']
                uid = res['data']['userId']
                request_header.update({'token': token1, 'uid': str(uid)})
                return request_header,row_num
            except Exception as e:
                self.getdata.write_result(row_num, '系统维护')
                print('===b系统维护=====错误信息>{0}===错误行>{1}'.format(e,row_num))
        elif request_ba == 'x':
            res = run_method.run_main(request_method, url_xht+request_url, request_data, request_header)
            res = json.loads(res)
            try:
                token1 = res['data']['token']
                uid = res['data']['userId']
                request_header.update({'token': token1, 'uid': str(uid)})
                return request_header,row_num
            except Exception as e:
                self.getdata.write_result(row_num, '系统维护')
                print('===b系统维护=====错误信息>{0}===错误行>{1}'.format(e,row_num))

    def run_dependent(self):
        """
        运行依赖的caseID case request 请求
        :return:
        """
        global AssociationH_Header, res
        run_method  = RunMethod(self.sheetId)
        row_num = self.oper_excel.get_row_num(self.CaseId)  # 获取 casename 对应的行号
        dependCase = self.getdata.get_is_depend(row_num)  # 拿到case依赖 执行依赖
        request_data = self.getdata.get_request_data(row_num)  # 拿到请求数据
        request_url = self.getdata.get_url(row_num)
        request_header = self.getdata.get_is_header(row_num)
        request_ba = self.getdata.get_before_after(row_num)
        request_method = self.getdata.get_is_requestMethod(row_num) # 拿到请求方法
        update_da = self.getdata.get_update_data(row_num)  # 拿到更新数据

        if dependCase is not None:
            if update_da is not None:
                AssociationH_Header = self.get_Association_case(update_da)
            else:
                AssociationH_Header = self.get_Association_case()

            try:
                request_header = AssociationH_Header[0]
            except Exception as e:
                self.getdata.write_qh_response_result(row_num, '系统维护')
                print('====系统维护=====错误信息>{0}===错误行>{1}'.format(e,row_num))

        if 'login/username' in request_url:
            self.get_hea.get_qiantai_login(request_header)
            if self.update is not None:
                request_data.update(self.update)

        if 'login/submit' in request_url:
            self.get_hea.get_houtai_login(request_header, request_data)

        if request_ba == 'a':
            res = run_method.run_main(request_method, url_pc + request_url, request_data, request_header)
        elif request_ba == 'b':
            res = run_method.run_main(request_method, url_Htai + request_url, request_data, request_header)
        elif request_ba == 'x':
            res = run_method.run_main(request_method, url_xht + request_url, request_data, request_header)

        try:
            if dependCase is not None:
                if AssociationH_Header[1]:
                    return json.loads(res),AssociationH_Header[1],request_header
            else:
                return json.loads(res)
        except Exception as e:
            print('====系统维护=====错误信息>{0}===错误行>{1}'.format(e,row_num))



    def get_data_for_key(self,row,num_dk,name_index):
        """
        根据依赖的key 执行依赖的case想要返回后通过 json_path 提取出对应的数据
        :param name_index:
        :param num_dk:
        :param row:
        :return:
        """
        global result1,depend_value
        depend_value = [] # 从返回的json提取出来的值
        depend_data = self.getdata.get_request_case_depend_value(row).split("<")  # 获取json表达式
        if len(depend_data)>1:
            if depend_data:
                kn = depend_data[name_index].split('-')
                if kn[0] == num_dk:
                    depend_data  = kn[1].split(">") # 分隔符可以填入多个表达式
                    response_data = self.run_dependent()
                    for depend_i in depend_data:
                        try:
                            json_exe = parse(depend_i)  # 获取对表达式
                            if type(response_data) is  tuple:
                                madle = json_exe.find(response_data[0])  # 使用json_path获取数据
                            else:
                                madle = json_exe.find(response_data)
                            result1 = [math.value for math in madle][0]
                            result1 = str(result1)
                            depend_value.append(result1)
                        except IndexError as e:
                            pass
                        except TypeError as e:
                            print('====系统维护=====错误信息>{0}===错误行>{1}'.format(e,row))
                    if type(response_data) is  tuple:
                        return depend_value,response_data[1],response_data[2]
                    else:
                        return depend_value
        else:
            if depend_data:
                for key_num in depend_data:
                    kn = key_num.split('-')
                    if kn[0] == num_dk:
                        depend_data  = kn[1].split(">") # 分隔符可以填入多个表达式
                        response_data = self.run_dependent()
                        for depend_i in depend_data:
                            try:
                                json_exe = parse(depend_i)  # 获取对表达式
                                if type(response_data) is  tuple:
                                    madle = json_exe.find(response_data[0])  # 使用json_path获取数据
                                else:
                                    madle = json_exe.find(response_data)
                                result1 = [math.value for math in madle][0]
                                result1 = str(result1)
                                depend_value.append(result1)
                            except IndexError as e:
                                pass
                            except TypeError as e:
                                print('====系统维护=====错误信息>{0}===错误行>{1}'.format(e,row))
                        if type(response_data) is  tuple:
                            return depend_value,response_data[1],response_data[2]
                        else:
                            return depend_value

