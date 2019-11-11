# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import lib.fileIO as IO
import re
import os

if __name__ == "__main__":
    
    a=IO.read_csv_to_dict("config/tag.csv",0,[4])
    b=IO.read_csv_to_list("config\Wayz_Tag_Update.csv")
    c=[]
    i=0
    for item in b:
        temp=item
        if a.get(item[1]) and a.get(item[1])[0]:
            temp[2]=a.get(item[1])[0]
            i=i+1
        c.append(temp)
    IO.write_csv("config\Wayz_Tag_Update_1.csv",c)
    print("旧标签数量:"+str(len(b)))
    print("覆盖范围:"+str(i/len(b)))
    print("未覆盖标签数量:"+str(len(b)-i))