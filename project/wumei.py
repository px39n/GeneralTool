import sys
sys.path.append("..")
import pandas as pd
from PyQt5 import QtWidgets,QtMultimedia,QtCore
from PyQt5.QtCore import pyqtSignal
from xml.etree.ElementTree import ElementTree, Element
from PyQt5.QtWebEngineWidgets import * 
import time
class Example(QtWidgets.QWidget):
    save_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.count=0
        self.urlcol=3
        self.initUI()
    def initUI(self):    
        # 创建输入框
        ipt = QtWidgets.QLineEdit("0")
        # 创建按钮
        btn = QtWidgets.QLabel("ALT保存 0不是物美相关	1是物美便利店	2是物美超市	3需删除")
        self.webview = QWebEngineView()
        self.webview.load(QtCore.QUrl("https://stackoverflow.com"))
        if a[self.count][self.urlcol].find("19Q2"):
            aurl=a[self.count][self.urlcol][int(a[self.count][self.urlcol].find("19Q2"))+5:].strip("}")
            burl=QtCore.QUrl("https://www.amap.com/place/"+aurl)
            self.webview.setUrl(burl)
            #self.webview.stop()
        # self.browser = QWebEngineView()
        # #加载外部页面，调用
        
        #self.setCentraWidget(self.browser)
        #btn.clicked.connect(lambda: self.word_check(ipt,player) )      # 给按钮添加响应
        ipt.returnPressed.connect(lambda: self.word_check(ipt))
        self.save_signal.connect(self.save_csv)
        # 创建对话框
        vbl = QtWidgets.QVBoxLayout()
        vbl.addWidget(ipt)
        vbl.addWidget(btn)
        vbl.addWidget(self.webview)
        self.setLayout(vbl)
        self.show()
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Alt):
            self.save_signal.emit()
    def save_csv(self):
        pd.DataFrame(a).to_csv("File\wumei.csv",index=False,header=False,encoding="utf_8_sig")
        print(self.count)
    def word_check(self,edit):
        
        a[self.count].append(edit.text())
        self.count=self.count+1
        edit.setText("0")
        if a[self.count][self.urlcol].find("19Q2"):
            
            if "便利" in a[self.count][1]:
                edit.setText("1")
            if "超市" in a[self.count][1]:
                edit.setText("2")  
            
            aurl=a[self.count][self.urlcol][int(a[self.count][self.urlcol].find("19Q2"))+5:].strip("}")
            burl=QtCore.QUrl("https://www.amap.com/place/"+aurl)
            try:
                self.webview.setUrl(burl)
            except:
                pass
            #time.sleep(3)
            #self.webview.stop()
            edit.setFocus()
            #btn.setText(res.content)
            #QtCore.QUrl("http://dict.youdao.com/dictvoice?type=1&audio={}"
        
if __name__ == '__main__':
    url="File/wumei.csv"
    a=pd.read_csv(url,",",header=None).values.tolist()
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# #检查物美超市是不是
# import sys
# sys.path.append("..")
# import pandas as pd
# url="File\word - 副本.csv"
# a=pd.read_csv(url,",",header=None).values.tolist()
# c=[]
# for item in a:
#     item1=item
#     if "便利" in item[1]:
#         item1.append("1")
#     if "超市" in item[1]:
#         item1.append("2")
#     c.append(item1)
# pd.DataFrame(c).to_csv("File\wumei.csv",index=False,header=False,encoding="utf_8_sig")
