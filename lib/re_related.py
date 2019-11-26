#!/usr/bin/python
# -*- coding: UTF-8 -*- 
 

import re
url='https://www.dianping.com/search/keyword/287/0_%E4%BC%91%E9%97%B2%E5%A8%B1%E4%B9%90'

#搜索相关

#返回索引
print(url.find("h"))

#返回
a=re.findall("eyword/(.+?)/",url)[0]
print(a)


record="周大生华联商厦专柜"
key1=record[1][(record[1].find("(")+1):(record[1].find("(")+4)]
print(record[1].find("("))
print(key1)