# encoding: utf-8

"""
# @Time    : 28/10/2019 10:44 上午
# @Author  : Function
# @FileName    : Opertion_Interface.py
# @Software: PyCharm

get post 请求方法封装
"""
import requests
import json



class RunMethod:
    def __init__(self):
        self.r = requests.session()  # 保存登陆的session

    def post_main(self,url,data,header=None):
        """
        post 请求方法
        :param url:
        :param data:
        :param header:
        :return:
        """
        if header is not None:
            res = self.r.post(url=url,data=data,headers=header,timeout=10).json()
        else:
            res = self.r.post(url=url,data=data,timeout=10).json()
        return res

    def get_main(self,url,data,header=None):
        """
        get请求方法
        :param url:
        :param data:
        :param header:
        :return:
        """
        if header is not None:
            res = self.r.get(url=url,data=data,headers=header,timeout=10).json()
        else:
            res = self.r.get(url=url,data=data,timeout=10).json()
        return res

    def run_main(self,method,url,data=None,header=None):
        """
        主函数选择请求方法
        :param method:
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None

        if method == 'post':
            res  = self.post_main(url,data,header)
        elif method == 'get':
            res = self.get_main(url,data,header)
        else:
            print("=====================----不好意思该方法不存在----===========================")

        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)


if __name__ == '__main__':
    pass
