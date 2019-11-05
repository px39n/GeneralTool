import sys
import log
import csv
import platform

def test():
    url=""
    mlist=[]
    mdict={}
    mint=123
    read_csv_to_dict(url,mint,mlist)
    read_csv_to_list(url,mlist)




def write_csv(path, data, way):
    ''' 按传入方式 "a+", "w+", 'r+' 写入csv '''
    if ["a+", "w+", 'r+'].__contains__(way) is False:
        print('当前传入方式错误：'+way)
        sys.exit()

    if type(data) is list:
        data = ','.join(str(v) for v in data)
    elif type(data) is tuple:
        data = ','.join(str(v) for v in data)
    else:
        data = str(data)
    if 'Windows' in platform.platform():
        f = open(path, way, encoding='utf-8')
    else:
        f = open(path, way)
    f.write( data + '\n')
    f.close()

def read_csv(url):
    ''' 读取csv文件 '''
    if 'Windows' in platform.platform():
        csv_data = csv.reader(open(url, encoding='utf-8'))
    else:
        csv_data = csv.reader(open(url))
    return csv_data

def read_csv_to_list(url,index_list):
    '''
    读取csv数组,保留index_list中的序列
    return:list
    '''
    csv_data = csv.reader(open(url, encoding='utf-8'))
    csv_list=[]
    for row in csv_data:
        row_list=[]
        for i in index_list:
            row_list.append(row[i])
        csv_list.append(row_list)
    return csv_list

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

