import json
import requests
from PIL import Image
def get_token():
    #of getcode
    appid="wxffa6f92be9ce98c7"
    secret="8491252c0ebe2fd410e441972540c6a7"
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(appid,
                                                                                                           secret)
    respon = requests.get(url)
    content = respon.content

    content = content.decode('utf-8')
    data = json.loads(content)
    return data.get("access_token")


def getWXACodeUnlimit(scene):
    #Accroding the token, use the keylist to generate the QRcode，and paste the background
    i=0
    for id in scene:
        id=id[0]
        access_token = get_token()
        if not access_token:
            pass
        else:
            url = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token={}'.format(access_token)
            data = {
                    "page": "pages/hello/hello",
                    "scene": id,
                    "width": 1280,
                    # "auto_color":True,
                    # "line_color":{"r":230,"g":40,"b":22},  # 自定义颜色
                    "line_color": {"r": 255, "g": 255, "b": 255},  # 自定义颜色
                    "is_hyaline": True}
            # todo 不能使用data 要使用json
            # ret = requests.post(url, json=data)
            ret = requests.post(url, json=data)

            with open('temp/{}.png'.format(id), 'wb') as f:
                f.write(ret.content)
            pastimg('template.png','temp/{}.png'.format(id),'result/{}.png'.format(id))
            i=i+1
            print(i)

def pastimg(img1,img2,target):
    #使二维码加载底图
    base_img = Image.open(img1)
    # 可以查看图片的size和mode，常见mode有RGB和RGBA，RGBA比RGB多了Alpha透明度
    # print base_img.size, base_img.mode
    box = (18, 267, 133, 382)  # 底图上需要P掉的区域
    base_img=base_img.convert("RGBA")
    #加载需要P上去的图片
    tmp_img = Image.open(img2)
    #这里可以选择一块区域或者整张图片
    #region = tmp_img.crop((0,0,304,546)) #选择一块区域
    #或者使用整张图片
    region = tmp_img.convert("RGBA")


    #使用 paste(region, box) 方法将图片粘贴到另一种图片上去.
    # 注意，region的大小必须和box的大小完全匹配。但是两张图片的mode可以不同，合并的时候回自动转化。如果需要保留透明度，则使用RGMA mode
    #提前将图片进行缩放，以适应box区域大小
    # region = region.rotate(180) #对图片进行旋转
    region = region.resize((box[2] - box[0], box[3] - box[1]))
    base_img.paste(region, box,region)
    #base_img.show() # 查看合成的图片
    base_img.save(target) #保存图片

# import pandas as pd
# setl=pd.read_csv("data/sql_update.csv",",",header=0,converters={i: str for i in range(0, 100)}).values.tolist()
# getWXACodeUnlimit(setl)