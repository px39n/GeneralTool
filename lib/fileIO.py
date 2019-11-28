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
a=pd.read_csv(url,",",dtype=object,header=None).values.tolist()  #无标题
gd_data=pd.read_csv(url,",",dtype=object,header=0,usecols=[5,4],names=["tag","wayz"])    #有标题

#写入txt
pd.DataFrame(data).to_csv(url,index=False,header=False,encoding="utf_8_sig")

def write_csv(url, data,encoding="utf_8"):
    data=pd.DataFrame(data)
    data.to_csv(url,index=False,header=False,encoding="utf_8_sig")


def read_csv(url):
    ''' 读取csv文件 '''
    if 'Windows' in platform.platform():
        csv_data = csv.reader(open(url, encoding='utf-8'))
    else:
        csv_data = csv.reader(open(url))
    return csv_data

def read_csvcolumn_to_list(url,index_list):
    '''
    读取csv数组,保留index_list中的序列
    return:list
    '''
    csv_data = [csv.reader(open(url, encoding='utf-8'))]
    csv_list=[]
    for column in index_list:
        column_list=[]
        for row in csv_data:
            column_list.append(row[column])
        csv_list.append(column_list)
    return csv_list

def read_csv_to_list(url,mode="r"):
 

    file_a = pd.read_csv(url)
    file_a = file_a.values.tolist()
    return file_a

def read_csv_to_dict(dict_file_path, key_index, value_indexs,flag="normal"):
    '''  
    读取csv文件，转为字典； 
    key_index key值  eg:0   
    value_indexs value值 下标数组   
    eg:flag-normal-[1,2,3,4]   flag-concat  |
    '''
    if flag=="normal":
        data = read_csv(dict_file_path)
        result_dicts = {}
        for row in data:
            value_list=[]
            for i in value_indexs:
                value_list.append(row[i].strip().replace('\n',''))
            result_dicts[row[key_index].strip().replace('\n','')] = value_list
        return result_dicts
    if flag=="concat":
        data = read_csv(dict_file_path)
        result_dicts = {}
        for row in data:
            value_list=[""]
            for i in value_indexs:
                if  value_list[0]:
                    value_list[0]=value_list[0]+"|"+row[i].strip().replace('\n','')
                else:   
                    value_list[0]=row[i].strip().replace('\n','')
            result_dicts[row[key_index].strip().replace('\n','')] = value_list
        return result_dicts

