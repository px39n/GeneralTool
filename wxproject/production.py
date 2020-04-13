import random
import string
import sys
import os
import pandas as pd
import numpy as np
from datetime import datetime


def RandomKeyGenerator():
    #初始化10000个随机key
    a = string.ascii_letters + string.digits
    key = []
    def getKey():
        key = random.sample(a, 11)
        keys = "".join(key)
        return keys
    keyset=[]
    for i in range(10000):
        keyset.append([getKey(),"0"])
    if not os.path.isfile('data/keyset.csv'):
        pd.DataFrame(keyset).to_csv('data/keyset.csv', index=False, header=['key','used'], encoding="utf_8_sig")

def QRcodegenerator():
    pass

def SQLRecordGenerator(num):
    #生成指定数量可供wx读取的sql文件
    keyset=pd.read_csv('data/keyset.csv',",",header=0,converters={i: str for i in range(0, 100)}).values.tolist()
    newset=[]
    i = 0
    for item in keyset:
        if item[1]=="0":
            newset.append([item[0]])
            item[1]="1"
            i=i+1
        print(i)
        if i==num:
            break
    pd.DataFrame(keyset).to_csv('data/keyset.csv', index=False, header=['key', 'used'], encoding="utf_8_sig")
    print(newset)
    pd.DataFrame(newset).to_csv('data/sql_update.csv', index=False, header=['_id'], encoding="utf_8_sig")


def sql_update():
    # 1.Extract the used_records
    # 2.Check and update the used SQL Datebase
    # 3.Build a delivery csv named with phase_data
    userdb=pd.read_csv('data/user_db.csv',",",header=0,converters={i: str for i in range(0, 100)})
    a=pd.read_json('data/update.json', lines=True, encoding='utf-8')
    update_db=a[( pd.isnull(a.userName)!=True)]

    delivery_db=pd.DataFrame(columns=('编号','姓名','电话','省','市','区','街道','物流单号'))
    for index, row in update_db.iterrows():
        if getattr(row, "_id") not in userdb['_id'].tolist():
            userdb=userdb.append(row, ignore_index=True)
            delivery_db=delivery_db.append({'编号':row['_id'],'姓名':row['userName'],'电话':row['telNumber'],'省':row['provinceName'],'市':row['cityName'],'区':row['countyName'],'街道':row['detailInfo']}, ignore_index=True)

    time = str(datetime.now().year)+'-'+str(datetime.now().month)+'-'+str(datetime.now().day)+'-'+str(datetime.now().hour)+'-'+str(datetime.now().minute)

    if not delivery_db.empty:
        if os.path.isfile('data/{}.csv'.format(time)):
            delivery_db.to_csv('data/{}_2.csv'.format(time), index=False, encoding="utf_8_sig")
        else:
            delivery_db.to_csv('data/{}.csv'.format(time), index=False, encoding="utf_8_sig")
    userdb.to_csv('data/user_db.csv', index=False, encoding="utf_8_sig")

def delivery_update():
    # 1.Check the data
    # 2.Add the data
    user_db = pd.read_csv('data/user_db.csv', ",", header=None,
                           converters={i: str for i in range(0, 100)}).values.tolist()
    for filepath, dirnames, filenames in os.walk(r'data/delivery'):
        for filename in filenames:
            file_path=os.path.join(filepath, filename)
            delivery = pd.read_csv(file_path, ",", header=None,
                                converters={i: str for i in range(0, 100)}).values.tolist()
            for i in user_db:
                for j in delivery:
                    if j[0]==i[0] :
                        i[4]=j[7]
                        i[11]=str(datetime.now().year)+'-'+str(datetime.now().month)+'-'+str(datetime.now().day)+','+str(datetime.now().hour)+":00"

    pd.DataFrame(user_db).to_csv('data/user_db.csv',index=False,header=False,encoding="utf_8_sig")

sql_update()
delivery_update()

