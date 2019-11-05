# -*- coding: utf-8 -*-

import fileIO as IO   


list1=[]
list2=[]
#交集
list3=[new for new in list1 if new in list2]

#差集
list3=list(set(list1).difference(set(list2)))