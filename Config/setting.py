# encoding: utf-8

"""
# @Time    : 25/10/2019 11:47 上午
# @Author  : Function
# @FileName    : setting.py
# @Software: PyCharm

配置文件 =====-----相关变量-----======
"""
# =============------文件路径------================================
path_excle = r'../Config/CaseResult.xls'   # 接口自动化Excle文件路径

# =============------Email相关变量------===========================
MAIL_HOST = "secure.emailsrvr.com"  # 设置服务器
MAIL_USER = "Function@seektopser.com"  # 用户名
MAIL_PASS = "function@110"  # 密码
PORT = "465"  # 发送端口
SENDER = 'Function@seektopser.com'  # 发送者
RECEIVERS = ['Function@seektopser.com','elma@seektopser.com','leo@seektopser.com','felix@seektopser.com']  # 接收邮件
SUBJECT = "BB项目娱乐端Android、IOS、Web H5 UI自动化"
OUT_FILENAME = 'CaseResult.xls'

# ==============-----Excel 相关行号-----============================
case_id = '0'
be_after = '1'
case_name = '2'
url = '3'
run = '4'
request_way = '5'  # 请求方式
header = '6'  # header
"""header依赖数据"""
case_depend = '7' # case依赖
data_depend = '8' # header 依赖返回的数据
filed_depend = '9'  # header 数据依赖字段
"""--------------"""
data = '10'
dynamic_data = '11'  # 动态传入值
"""-----------request_data 依赖数据----------"""
request_case_depend_value = '12'
request_filed_depend_key = '13'
"""-----------------------------------------"""
update_data = '14' # 更新数据
q_name_depend_key = '15'
h_name_depend_key = '16'
qh_result = '17'
expect = '18'
result = '19'
response_result = '20'

# ==============-----数据库配置谷歌生成器-----===========================
host_Mysql = '203.60.1.61'
db_Mysql = 'global_3rd_db'
port_Mysql = 3306
user_Mysql = 'test'
passwd_Mysql = 'Seektop@123'
charset_Mysql = 'utf8'

# ==============-----前后台接口地址前缀-----===========================
url_pc = 'http://www.aalgds.com/api/'
url_Htai = 'http://intra.aalgds.com/api/'
