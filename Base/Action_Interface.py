# encoding: utf-8

"""
# @Time    : 28/10/2019 11:30 上午
# @Author  : Function
# @FileName    : ActionMe.py
# @Software: PyCharm

接口自动化测试 关键字方法
"""
import time
from hashlib import md5

import pymysql
from hashlib import md5
import base64,time,struct,hmac,hashlib,sys

from Base.Opertion_Interface import RunMethod
from Data.Get_Data import GetData
from Until.Common_Util import Compared
from Until.Opertion_Email import SEmail
from Config.setting import *


class MethodInterface:
    def __init__(self,sheetId):
        self.run_method = RunMethod(sheetId)
        self.get_data  = GetData(sheetId)
        self.comm = Compared()
        self.sendemail = SEmail()
        self.sheetId = sheetId

    def getSign(self,request_headers):
        """
        获取签名
        :return:
        """
        try:
            # 拼接字符串
            list_header = []
            for key in request_headers:
                list_header.append(key)
                list_header.append('=')
                list_header.append(request_headers[key])
                list_header.append('&')
            linkString = ''.join(list_header)[0:-1]
            # 生成签名
            secret = "global"
            str_sign = linkString + secret
            new_md5 = md5()
            new_md5.update(str_sign.encode(encoding='utf-8'))
            sign = new_md5.hexdigest()
            return sign
        except Exception as e:
            print("=======----错误的参数--{0}--=======:".format(e))

    def database(self,sql):
        """
        连接数据库
        :param sql:
        :return:
        """
        global cur, conn
        try:
            conn = pymysql.connect(
                host='203.60.1.61',
                db='global_3rd_db',
                port=3306,
                user='test',
                passwd='Seektop@123',
                charset='utf8',
            )
            cur = conn.cursor()
            cur.execute(sql)
            result_mysql = cur.fetchall()
            return result_mysql
        except:
            print("连接数据库失败")
            raise
        finally:
            pass


    def getGoogleCode(self):
        """
        生成谷歌验证码用户后台登录
        :return:
        """
        # 获取当前系统时间，按照后台校验规则除以30取整
        t = time.time()
        input = int(t / 30)
        # 查询用户的密钥
        result = self.database("SELECT `security` FROM `gl_admin_security` WHERE user_id='421';")
        secretKey = result[0][0]
        # print(secretKey)
        # 打包参数
        key = base64.b32decode(secretKey, casefold=True)
        msg = struct.pack(">Q", input)
        googleCode = hmac.new(key, msg, hashlib.sha1).digest()
        # python版本判断
        if sys.version_info > (2, 7):
            o = googleCode[19] & 15
        else:
            o = ord(googleCode[19]) & 15
        # 生成验证码
        googleCode = str((struct.unpack(">I", googleCode[o:o + 4])[0] & 0x7fffffff) % 1000000)
        if len(googleCode) == 5:  # 如果验证码的第一位是0，则不会显示。此处判断若是5位码，则在第一位补上0
            googleCode = '0' + googleCode
        return googleCode

if __name__ == '__main__':
    a = MethodInterface(0)
    c = a.getGoogleCode()
    print(c)