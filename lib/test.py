import urllib.request
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko')
opener = urllib.request.build_opener()
opener.addheaders = [headers]  
op = opener.open('https://www.amap.com/place/B0FFK296BR') 
c=op.read().decode(encoding='UTF-8')  
print(c)