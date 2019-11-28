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

# for i in range(len(a)):
#   i = str(i)
#   json_exe = parse('data.list.['+i+'].remark')  # 获取对表达式
#   madle = json_exe.find(demo)  # 使用json_path获取数据
#   result1 = [math.value for math in madle][0]
#   print(result1)
#
# demo1 = ['0.0']
# demo2 =['0.0']
#
# print(demo1==demo2)

demo = {
  "code": 1,
  "data": {
    "endTime": 1575129599000,
    "propList": [
      {
        "actId": 10,
        "createTime": 1574488719000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 125,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574488756000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 126,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574488812000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 127,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574488835000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 128,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574488921000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 129,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574488953000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 130,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574489078000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 131,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574489806000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 132,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574492177000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 133,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574492189000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 134,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574492249000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 135,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574492399000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 136,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574736224000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 137,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574736467000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 138,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574736839000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 139,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574737160000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 140,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574737498000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 141,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1574747388000,
        "goodsName": "测试软件",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 142,
        "images": "",
        "num": 0,
        "position": 1,
        "price": 1.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1572508870000,
        "goodsName": "球衣",
        "goodsType": 1,
        "grandPrix": 1,
        "id": 104,
        "images": "/api/gl/file/files/5db9811388796311499c650f.jpg",
        "num": 10,
        "position": 2,
        "price": 8000.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1572508876000,
        "goodsName": "礼金",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 103,
        "images": "/api/gl/file/files/5db9815e88796311499c6512.jpg",
        "num": 0,
        "position": 3,
        "price": 88.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1572508899000,
        "goodsName": "礼金",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 101,
        "images": "/api/gl/file/files/5db9827688796311499c651b.jpg",
        "num": 10,
        "position": 6,
        "price": 188.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1572660476000,
        "goodsName": "礼品券2",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 113,
        "images": "/api/gl/file/files/5dbce4fa88796319d4505273.png",
        "num": 0,
        "position": 7,
        "price": 100.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1572504645000,
        "goodsName": "vip升级流水",
        "goodsType": 2,
        "grandPrix": 0,
        "id": 107,
        "images": "/api/gl/file/files/5db9832088796311499c6529.jpg",
        "num": 0,
        "position": 8,
        "price": 188.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1572439353000,
        "goodsName": "LV男士钱夹",
        "goodsType": 1,
        "grandPrix": 0,
        "id": 109,
        "images": "/api/gl/file/files/5db9832788796311499c652b.jfif",
        "num": 0,
        "position": 9,
        "price": 800.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1572506780000,
        "goodsName": "282不是礼金",
        "goodsType": 0,
        "grandPrix": 0,
        "id": 110,
        "images": "/api/gl/file/files/5db9848688796311499c653b.jfif",
        "num": 0,
        "position": 10,
        "price": 288.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1572508915000,
        "goodsName": "VIP升级流水",
        "goodsType": 2,
        "grandPrix": 0,
        "id": 111,
        "images": "/api/gl/file/files/5db9833588796311499c652f.jpg",
        "num": 0,
        "position": 11,
        "price": 288.0,
        "status": 0,
        "weights": 0
      },
      {
        "actId": 10,
        "createTime": 1572439384000,
        "goodsName": "zippo打火机",
        "goodsType": 1,
        "grandPrix": 0,
        "id": 112,
        "images": "/api/gl/file/files/5db9846988796311499c6537.jpg",
        "num": 0,
        "position": 12,
        "price": 188.0,
        "status": 0,
        "weights": 0
      }
    ],
    "rewardImage": "/api/gl/file/files/5db9811388796311499c650f.jpg",
    "rewardName": "球衣",
    "rewardNum": 0,
    "startTime": 1574265600000,
    "taskList": [
      {
        "actId": 10,
        "conditionValue": 1,
        "createTime": 1574747381000,
        "current": 0,
        "id": 94,
        "rewardNum": 12,
        "status": 0,
        "taskId": 1,
        "taskName": "体育H5登录",
        "taskType": 2,
        "type": 0
      }
    ]
  },
  "message": "SUCCESS"
}