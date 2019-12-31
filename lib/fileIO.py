import sys

import csv
import platform
import pandas as pd
import os

sys.path.append('..')
#item="asdf.csv"
#print(os.path.splitext(item)[0]) 去除后缀
url="File\word.csv"
#读取txt
# data=pd.read_csv(url,",",header=None,converters={i: str for i in range(0, 100)}).values.tolist()  #无标题
# gd_data=pd.read_csv(url,",",dtype=object,header=0,usecols=[5,4],names=["tag","wayz"])                       #有标题

#写入txt
# pd.DataFrame(data).to_csv(url,index=False,header=False,encoding="utf_8_sig")


def csv_union(url1,url2,finalurl):
    left = pd.read_csv(url1, ",", header=0, converters={i: str for i in range(0, 100)})  # 无标题
    right = pd.read_csv(url2, ",", header=0, converters={i: str for i in range(0, 100)})  # 无标题
    left.columns = ["city","code","level"]
    right.columns=["city","class_name","amount"]
    result = pd.merge(left, right, how='left', on="city")
    result.to_csv(finalurl,index=False,header=False,encoding="utf_8_sig")
data=pd.read_csv("D:\Code\GeneralTool\File\good.csv",",",header=None,converters={i: str for i in range(0, 100)}).values.tolist()
for i in data:
    i[0]=i[0]+"市"
pd.DataFrame(data).to_csv("D:\Code\GeneralTool\File\good.csv",index=False,header=False,encoding="utf_8_sig")
csv_union("D:\Code\GeneralTool\File\city.csv","D:\Code\GeneralTool\File\good.csv","D:\Code\GeneralTool\File\perfect.csv")
