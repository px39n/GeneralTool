#人工去重

import sys

sys.path.append('..')
import math
import pandas as pd

def read_csv_to_list(url,mode="r"):
    file_a = pd.read_csv(url)
    file_a = file_a.values.tolist()
    return file_a
def write_csv(url, data,encoding="utf_8"):
    data=pd.DataFrame(data)
    data.to_csv(url,index=False,header=False,encoding="utf_8_sig")



url="config\data_chow.csv"
target_url="config\data_chow1.csv"
final_url="config\lfx_final_data.csv"
tx="config\lfx_data.csv"
dp="config\lfx_datadp.csv"
gd="config\lfx_datagd.csv"

def list_generator(url,target_url):
    a=read_csv_to_list(url)
    tecent_list=[]
    dp_list=[]
    amap_list=[]
    for i in range(0,len(a)-1):
        if a[i][10][0]=="t":
            tecent_list.append("'https://map.qq.com/poi/?sm="+str(a[i][10][23:])+"&keyfrom=3"+"'")
        if a[i][10][0]=="a":
            amap_list.append("'https://www.amap.com/place/"+str(a[i][10][20:])+"'")
        if a[i][10][0]=="d":
            dp_list.append("'http://www.dianping.com/shop/"+str(a[i][10][24:])+"'")
    print(tecent_list)
    write_csv(target_url,[tecent_list,dp_list,amap_list])

def add_tel():
    a=read_csv_to_list(url)
    txd=read_csv_to_list(tx)
    dpd=read_csv_to_list(dp)
    gdd=read_csv_to_list(gd)
    for i in range(0,len(a)-1):
        for config in txd:
            if a[i][10][-5:]==config[1].strip("&keyfrom=3")[-5:]:
                a[i].append(config[2])
        for j in dpd:
            if a[i][10][-5:]==j[1][-5:]:
                a[i].append(j[4])
        for k in gdd:
            if a[i][10][-5:]==k[1][-5:]:
                a[i].append(k[2])     
    write_csv(final_url,a)

