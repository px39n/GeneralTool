import pandas as pd 

df=pd.DataFrame([1,2,3])



'''excel操作

排序
df=df[["wayz","tag"]]                   #重新排序

插入删除
df.drop(x,axis=1)                                                 #删除x列
df.insert(x, 'mark',['' for i in range(df.shape[0])])             #插入某一列

统计
df.shape[1]                 #列数
col_name=list(df)                     #获取表头列表

'''


'''多值操作
gd_data["wayz"]=gd_data["wayz"].map(lambda x:x[0:3])            #对某一列操作

'''
