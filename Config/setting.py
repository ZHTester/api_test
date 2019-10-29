# encoding: utf-8

"""
# @Time    : 25/10/2019 11:47 上午
# @Author  : Function
# @FileName    : setting.py
# @Software: PyCharm

配置文件 =====-----相关变量-----======
"""

# =============------文件路径------===========================
path_excle = r'../Config/CaseResult.xlsx'   # 接口自动化Excle文件路径


# =============------Email相关变量------===========================
MAIL_HOST = "secure.emailsrvr.com"  # 设置服务器
MAIL_USER = "Function@seektopser.com"  # 用户名
MAIL_PASS = "function@110"  # 密码
PORT = "465"  # 发送端口
SENDER = 'Function@seektopser.com'  # 发送者
RECEIVERS = ['Function@seektopser.com','elma@seektopser.com','leo@seektopser.com','felix@seektopser.com']  # 接收邮件
SUBJECT = "BB项目娱乐端Android、IOS、Web H5 UI自动化"
OUT_FILENAME = 'CaseResult.xlsx'


# ==============-----Excel 相关行号-----============================
case_id = '0'
case_name = '1'
url = '2'
run = '3'
request_way = '4'  # 请求方式
header = '5'  # header
case_depend = '6' # case依赖
data_depend = '7' # 依赖返回的数据
filed_depend = '8'  # 数据依赖字段
data = '9'
expect = '10'
result = '11'
response_result = '12'