#检查物美超市是不是
import sys
sys.path.append("..")
import pandas as pd
url="File\wumei.csv"
a=pd.read_csv(url,",",header=None).values.tolist()
c=[]
for item in a:
    item1=item
    if "平价" in item[1] or "批发" in item[1] or"果" in item[1] or"蔬" in item[1]:
        item1.append("0")
    else:
         
            
        if "物美便利店" in item[1] and item[1][0]=="物":
            item1.append("1")
        elif ("物美超市" in item[1] or "大卖场" in item[1]) and item[1][0]=="物":
            item1.append("2")
        else:
            item1.append("0")
    c.append(item1)
pd.DataFrame(c).to_csv("File\wumei.csv",index=False,header=False,encoding="utf_8_sig")
