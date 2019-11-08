# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import lib.fileIO as IO
import re
import os

if __name__ == "__main__":

    r_url="C:/Users/admin/Documents/Spider/process"
    for item in os.listdir(r_url):
        item=os.path.splitext(item)[0]
        url=r_url+"/"+item
        list1=IO.read_csv_to_list(url+".csv")
        list1=[i[1:] for i in list1]
        new_list=[]
        for i in list1:
            i[0]=int(re.findall("eyword/(.+?)/",i[0])[0])
            new_list.append(i)
        new_list.sort()
        new_list.insert(0,["web_url","count","name","type"])
        IO.write_csv(r_url+"/"+new_list[1][3]+".csv",new_list)
    #print(new_list)