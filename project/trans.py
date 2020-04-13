import json
import glob, os
from shutil import copytree

import requests
from xml.etree.ElementTree import ElementTree, Element
# 翻译函数，word 需要翻译的内容
from googletrans import Translator

def dictmaker(url):
    translator = Translator()

    XML_PATH = url
    tree = ElementTree()
    tree.parse(XML_PATH)
    root = tree.getroot()
    try:
        print(root[0][0].text)
        for item in root:
            for iitem in item:
                iitem.text = translator.translate(iitem.text, dest='zh-CN').text+'('+iitem.text+')'
                print(iitem.text)
    except:
        for item in root:
            #print(item.text)
            item.text=translator.translate(item.text, dest='zh-CN').text+'('+item.text+')'
            print(item.text)
    tree.write(url,encoding="UTF-8")
def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "en2zh-CHS",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 然后相应的结果
        return response.text
    else:
        print("有道词典调用失败")
        # 相应失败就返回空
        return None


def get_reuslt(repsonse):
    # 通过 json.loads 把返回的结果加载成 json 格式
    result = json.loads(repsonse)

    return result['translateResult'][0][0]['tgt']


# a="D:\Game\X64\\a\\"
#print(os.getcwd())
#a=os.getcwd()
# ChineseSimplified

# for entry in os.listdir(a):
#     if os.path.isdir(os.path.join(a, entry)):
#         if not os.path.isdir(a+'\\'+entry+'\languages\ChineseSimplified'):
#             print(a+'\\'+entry)
#             #os.system('copy 1.txt.py D:\Game\X64\a\2.txt.py'.format(a+entry,))
#             copytree(a+'\\'+entry, 'D:\Game\X64\\a\\'+entry)

# a="D:\Game\X64\\a\\"
# for entry in os.listdir(a):
#     if os.path.isdir(os.path.join(a, entry)):
#         if  os.path.isdir(a+'\\'+entry+'\languages\ChineseSimplified'):
#             print(a+'\\'+entry)
#             #os.system('copy 1.txt.py D:\Game\X64\a\2.txt.py'.format(a+entry,))
#             copytree(a+'\\'+entry+'\languages\ChineseSimplified', 'D:\Game\X64\\b\\'+entry+'\languages\ChineseSimplified')

a="D:\Game\X64\\b\\"
for root, dirs, files in os.walk(a):
    for file in files:
        if file.endswith(".xml"):
            dictmaker(os.path.join(root, file))

