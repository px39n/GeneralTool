import json
import requests

def get_token():
    appid="wxffa6f92be9ce98c7"
    secret="8491252c0ebe2fd410e441972540c6a7"
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(appid,
                                                                                                           secret)
    respon = requests.get(url)
    content = respon.content

    content = content.decode('utf-8')
    data = json.loads(content)
    return data.get("access_token")


def getWXACodeUnlimit():
    access_token = get_token()
    if not access_token:
        pass
    else:
        url = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token={}'.format(access_token)
        data = {
                "page": "pages/hello/hello",
                "scene": "15746151545fdfs56456",
                "width": 1280,
                # "auto_color":True,
                # "line_color":{"r":230,"g":40,"b":22},  # 自定义颜色
                "line_color": {"r": 43, "g": 162, "b": 69},  # 自定义颜色
                "is_hyaline": True}
        # todo 不能使用data 要使用json
        # ret = requests.post(url, json=data)
        ret = requests.post(url, json=data)

        # print(ret.text)
        print(ret.content)
        with open('getWXACodeUnlimit.png', 'wb') as f:
            f.write(ret.content)
getWXACodeUnlimit()