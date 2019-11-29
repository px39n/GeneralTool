import pandas as pd
import sys
sys.path.append("..")
url="config\gd_category_to_tag.csv"
durl="config\dianping_category_to_tag.csv"
wayz="config\gd_category_to_tag - 副本.csv"
gd_data=pd.read_csv(url,",",header=0,usecols=[5,4],converters={"wayz":str,"tag":str},names=["tag","wayz"])[["wayz","tag"]]
dp_data=pd.read_csv(durl,",",header=0,usecols=[10,6,7],names=["tag1","tag2","wayz"],converters={"wayz":str,"tag1":str,"tag2":str})[["wayz","tag1","tag2"]]
a=pd.read_csv(wayz,",",header=0,usecols=[2],converters={i: str for i in range(0, 100)}).values.tolist()  #无标题

gd_data["wayz"]=gd_data["wayz"].map(lambda x:x[0:3])
dp_data["wayz"]=dp_data["wayz"].map(lambda x:x[0:3])


gd_data=gd_data.values.tolist()
dp_data=dp_data.values.tolist()
for row in dp_data:
        if row[1]:
            if row[2]:
                row[1]=row[1]+"|"+row[2]
        else:
            if row[2]:
                row[1]=row[2]

def detect_value(a,list_x):
    for row in a:
        row.append([])
        for tagrow in list_x:
            if row[0] in tagrow[1]:
                
                row[1].append(tagrow[0])
        row[1]=list(set(row[1]))

detect_value(a,gd_data)
detect_value(a,dp_data)
for row in a:
    row[1]="|".join(row[1]) 

final="config/final.csv"
pd.DataFrame(a).to_csv(final,index=False,header=False,encoding="utf_8_sig")

print(1)
# dp_groupby


# merge


# tag_list.append 