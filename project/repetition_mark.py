import pandas as pd
import difflib

url="config/test.csv"
name_col=16
rep_col=7
addr_col=3
dis_col=5
ind_col=4

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

df=pd.read_csv(url,",",header=None,converters={i: str for i in range(0, 100)})
mark_col=df.shape[1]
df.insert(df.shape[1], 'mark',['' for i in range(df.shape[0])])    
all=df.values.tolist()  #获取列表
print(1)
for i in range(1,len(all)-20):
    all[i][rep_col]=""
    all[i][name_col]="梁哲豪"
    if all[i][mark_col]!="rep":
        for j in range(1,20):
            if string_similar(all[i][addr_col],all[i+j][addr_col])>0.7 or (j==1 and float(all[i][dis_col])<4):
                if all[i+j][mark_col]=="rep":
                    for k in range(1,20):
                        if all[i+j][ind_col] in all[i+j-k][rep_col]:
                            all[i][mark_col]="rep"
                            all[i+j-k][rep_col]=all[i+j-k][rep_col]+"|"+all[i][ind_col]
                            break
                else:
                    all[i+j][mark_col]="rep"
                    all[i][rep_col]=all[i][rep_col]+all[i+j][ind_col]+"|"
                    
        all[i][rep_col]=all[i][rep_col].strip("|")
        if not all[i][rep_col] and all[i][mark_col]!="rep":
            all[i][rep_col]="0"
    
final="config/final.csv"
pd.DataFrame(all).to_csv(final,index=False,header=None,encoding="utf_8_sig")


