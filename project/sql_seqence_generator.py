import pandas as pd
a=["airport,auto_service,bank,chemist,college,education,energy_station,entertainment,entity,factory,farm,food,foreign_institution,government,hall,health,hospital,hotel,institute,kindergarten,mall,market,office,organization,park,parking,pet,port,residential,road_entrance,scenic,school,service,service_area,shop,sports,station,supermarket,theater,toll,tower,venue"]
a=a[0].split(",")


sql=""
for name in a:
    single="union(select '{}',count(1) from {})\n".format(name,name)
    sql=sql+single

print(sql)
url="config/test.txt"
pd.DataFrame([sql]).to_csv(url,index=False,header=False,encoding="utf_8_sig")
