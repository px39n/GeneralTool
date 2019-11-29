import pandas as pd 

a=pd.DataFrame([1,2,3])



#重新排序
a=a[["wayz","tag"]]


#对某一列操作
gd_data["wayz"]=gd_data["wayz"].map(lambda x:x[0:3])



col_name=list(df)                     #获取表头


#插入某一列
df.insert(df.shape[1], 'mark',['' for i in range(df.shape[0])])             #