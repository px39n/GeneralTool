
import sys
import pandas as pd
sys.path.append('..')


import os
print(os.getcwd())
url="D:\Code\GeneralTool\dev\word.txt"
url1="D:\Code\GeneralTool\dev\word.csv"
data=pd.read_table(url,header=None,converters={i: str for i in range(0, 100)}).values.tolist()  #无标题
a=[]
for item in data:

    item1=item[0].split(' ')[-1].lstrip(' ')
    item0 = item[0].lstrip('\u3000\u3000').lstrip(' ').strip(item1).strip(' ')
    a.append([item0, item1])


print(data)
pd.DataFrame(a).to_csv(url1,sep=',',index=False,header=False,encoding="utf_8_sig")