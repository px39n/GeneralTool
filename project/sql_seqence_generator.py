a=["airport,auto_service,bank,chemist,college,education,energy_station,entertainment,entity,factory,farm,food,foreign_institution,government,hall,health,hospital,hotel,institute,kindergarten,mall,market,office,organization,park,parking,pet,port,residential,road_entrance,scenic,school,service,service_area,shop,sports,station,supermarket,theater,toll,tower,venue"]
a=a[0].split(",")


sql=""
for name in a:
    single="union(select '{}',count(*) from {} where tag_names is not null)\n".format(name,name)
    sql=sql+single


