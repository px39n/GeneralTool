import pandas as pd

tag="config/test1.csv"
all="config/test.csv"
tag=pd.read_csv(tag,",",dtype=object,header=None).values.tolist()  #无标题
all=pd.read_csv(all,",",dtype=object,header=None).values.tolist()  #无标题
other=pd.read_csv("config/test1.csv",",",dtype=object,header=None,usecols=[0]).values.tolist()  #无标题
for record in tag:
    for count in all:
        if record[0]==count[0]:
            record.append(count[1])
for i in all:
    if [i[0]] not in other:
        tag.append(i)
    
print(1)

pd.DataFrame(tag).to_csv("config/final.csv",index=False,header=False,encoding="utf_8_sig")

