import pandas as pd

# url="config\点评原始ID.csv"
# url2="config\点评源二.csv"
# dp_url='config\dianping_category_to_tag.csv'
# final='config/点评原始ID1.csv'
# df=pd.read_csv(url,",",header=0,names=['ID','name','tag'],converters={i: str for i in range(0, 100)})
# af=pd.read_csv(url2,",",header=0,names=['ID','name','tag'],converters={i: str for i in range(0, 100)})
# df.append(af)
# df.drop_duplicates(subset=['ID'],keep='first',inplace=True)

# dp=pd.read_csv(dp_url,",",header=0,usecols=[1,3,5],names=['first_category','tag','third'],converters={i: str for i in range(0, 100)})
# sec=pd.DataFrame(dp,columns = ['tag','first_category'])
# thi=pd.DataFrame(dp,columns = ['third','first_category']).rename(columns={'third': 'tag'})
# fir=pd.DataFrame(dp,columns = ['first_category','first_category'])
# fir.columns = ['tag','first_category']
# sec=sec.append(thi,ignore_index=True).append(fir,ignore_index=True)
# sec.drop_duplicates(subset=['tag'],keep='first',inplace=True)
# print(len(df))
# result=pd.merge(df,sec,how='left', on="tag")
# result.to_csv(final,index=False,encoding="utf_8_sig")

# print(len(result))


url="config\点评原始ID1.csv"
df=pd.read_csv(url,",",header=0,usecols=[0,1,3],names=['ID','name','first'],converters={i: str for i in range(0, 100)})
df.to_csv(url,index=False,encoding="utf_8_sig")