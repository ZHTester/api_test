from jsonpath_rw import jsonpath, parse

demo = {
  "code": 1,
  "data": {
    "amountTotal": 986878616.25,
    "list": [
      {
        "accountType": 0,
        "amount": 2000,
        "balance": 2000,
        "balanceBefore": 0,
        "createTime": 1574660653339,
        "fee": 0,
        "finishTime": 1574660653457,
        "lastUpdate": None,
        "orderDesc": "转账",
        "orderId": "ZZ201911251344DVWGPT",
        "orderType": 3,
        "parentId": 0,
        "parentName": "admin",
        "parentOrderId": "",
        "reallyAmount": 2000,
        "remark": "贝博体育钱包转入中心钱包",
        "splitType": 0,
        "status": 1,
        "subOrderNum": 0,
        "subType": "",
        "transferType": "",
        "userId": 7786,
        "userType": 0,
        "username": "admin123"
      },
      {
        "accountType": 0,
        "amount": 2000,
        "balance": 0,
        "balanceBefore": 2000,
        "createTime": 1574660651214,
        "fee": 0,
        "finishTime": 1574660651413,
        "lastUpdate": None,
        "orderDesc": "转账",
        "orderId": "ZZ201911251344DVWGPS",
        "orderType": 3,
        "parentId": 0,
        "parentName": "admin",
        "parentOrderId": "",
        "reallyAmount": 2000,
        "remark": "中心钱包转入贝博体育钱包",
        "splitType": 0,
        "status": 1,
        "subOrderNum": 0,
        "subType": "",
        "transferType": "",
        "userId": 7786,
        "userType": 0,
        "username": "admin123"
      }
    ],
    "pageNum": 0,
    "pageSize": 0,
    "total": 1220
  },
  "message": "SUCCESS"
}

a = demo['data']['list']

# a = parse('data.list')
# madle = a.find(demo)  # 使用json_path获取数据
# result1 = [math.value for math in madle][0]
#
# print('------------------{0}----------'.format(),len(result1))

for i in range(len(a)):
  i = str(i)
  json_exe = parse('data.list.['+i+'].remark')  # 获取对表达式
  madle = json_exe.find(demo)  # 使用json_path获取数据
  result1 = [math.value for math in madle][0]
  print(result1)

demo1 = ['0.0']
demo2 =['0.0']

print(demo1==demo2)