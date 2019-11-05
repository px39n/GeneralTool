# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import lib.fileIO as IO

if __name__ == "__main__":
    
    list1=IO.read_csv_to_list("config\dianping_category_to_tag.csv",[6,7])[0]
    list2=IO.read_csv_to_list("123",[6,7])
    list3=list(set(list1).difference(set(list2)))