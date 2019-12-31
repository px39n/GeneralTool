#人工去重

import sys

sys.path.append('..')
import math
import pandas as pd



def dp_statistic_generator():
    a=[17,267,8,9,219,344,16,160,21,11,3,6,5,18,10]
    class_list=["酒店","小区","商务楼","美食","综合商场","居家日用","成品家具","床品家纺","其他家具家居","家具家居","飞机场","智能家居","家用电器","超市","便利店","火车站","停车场","加油站","加气站","银行","银行","营业网点","ATM","自助网点","信用社","美容","SPA","祛痘","美发","养发","KTV","电影院","景点","医学美容","美容整形","药店"]
    scraper1=r'{"_id":"dianping_statistic_amount","startUrl":['
    scraper2='],"selectors":[{"id":"city","type":"SelectorText","parentSelectors":["_root"],"selector":".city span:nth-of-type(2)","multiple":false,"regex":"","delay":0},{"id":"class","type":"SelectorText","parentSelectors":["_root"],"selector":".bread span:nth-of-type(2)","multiple":false,"regex":"(?<=\\").*?(?=\\")","delay":0},{"id":"count","type":"SelectorText","parentSelectors":["_root"],"selector":".bread span:nth-of-type(2)","multiple":false,"regex":"(?<=到).*?(?=个)","delay":0}]}'
    url_list=""
    for class_name in class_list:
            for j in a:
                url='"http://www.dianping.com/search/keyword/{}/0_{}",'.format(str(j),str(class_name))
                url_list=url_list+url
    final=scraper1+url_list.strip(',')+scraper2
    print(final)

dp_statistic_generator()
def list_generator(url,target_url):
    a=pd.read_csv(url,",",header=None,converters={i: str for i in range(0, 100)}).values.tolist()
    tecent_list=[]
    dp_list=[]
    amap_list=[]
    for i in range(0,len(a)-1):
        if a[i][10][0]=="t":
            tecent_list.append("'https://map.qq.com/poi/?sm="+str(a[i][10][23:])+"&keyfrom=3"+"'")
        if a[i][10][0]=="a":
            amap_list.append("'https://www.amap.com/place/"+str(a[i][10][20:])+"'")
        if a[i][10][0]=="d":
            dp_list.append("'http://www.dianping.com/shop/"+str(a[i][10][24:])+"'")
    print(tecent_list)
    pd.DataFrame([tecent_list,dp_list,amap_list]).to_csv(target_url, index=False, header=False, encoding="utf_8_sig")

def add_tel(url,tx,dp,gd,final_url):
    a=pd.read_csv(url,",",header=None,converters={i: str for i in range(0, 100)}).values.tolist()
    txd=pd.read_csv(tx,",",header=None,converters={i: str for i in range(0, 100)}).values.tolist()
    dpd=pd.read_csv(dp,",",header=None,converters={i: str for i in range(0, 100)}).values.tolist()
    gdd=pd.read_csv(gd,",",header=None,converters={i: str for i in range(0, 100)}).values.tolist()
    for i in range(0,len(a)-1):
        for config in txd:
            if a[i][10][-5:]==config[1].strip("&keyfrom=3")[-5:]:
                a[i].append(config[2])
        for j in dpd:
            if a[i][10][-5:]==j[1][-5:]:
                a[i].append(j[4])
        for k in gdd:
            if a[i][10][-5:]==k[1][-5:]:
                a[i].append(k[2])     

    pd.DataFrame(a).to_csv(final_url, index=False, header=False, encoding="utf_8_sig")

