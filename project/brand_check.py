#人工去重

import math
import pandas as pd
EARTH_REDIUS = 6378.137

def rad(d):
    return d * math.pi / 180.0 

def getDistance(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return s*1000

def read_csv_to_list(url,mode="r"):
    file_a = pd.read_csv(url)
    file_a = file_a.values.tolist()
    return file_a
def write_csv(url, data,encoding="utf_8"):
    data=pd.DataFrame(data)
    data.to_csv(url,index=False,header=False,encoding="utf_8_sig")


url="E:\code\generaltool\config\周大福_官网_gcj02(1).csv"
target_url="E:\code\generaltool\config\周大福_官网_gcj021.csv"
a=read_csv_to_list(url)
for i in range(0,len(a)-1):
    a[i].append(getDistance(a[i][0],a[i][1],a[i+1][0],a[i+1][1]))
#a=getDistance(116.50244997561796,39.91534192673122,116.4490904568603,39.92283770582041)
write_csv(target_url,a)
#print(a)

