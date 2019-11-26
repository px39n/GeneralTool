import sys
sys.path.append("..")
import pandas as pd
from PyQt5 import QtWidgets,QtMultimedia,QtCore
from PyQt5.QtCore import pyqtSignal
from xml.etree.ElementTree import ElementTree, Element

class Example(QtWidgets.QWidget):
    voice_signal = pyqtSignal()
    trans_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.count=0
        self.initUI()

    def initUI(self):    
        # 创建输入框
        ipt = QtWidgets.QLineEdit("请输入单词")
        # 创建按钮
        btn = QtWidgets.QLabel("sad")
        
        player = QtMultimedia.QMediaPlayer()
        #btn.clicked.connect(lambda: self.word_check(ipt,player) )      # 给按钮添加响应
        ipt.returnPressed.connect(lambda: self.word_check(ipt,player,btn))
        self.voice_signal.connect(lambda: self.voice(player))
        self.trans_signal.connect(lambda:self.trans_show(btn))
        # 创建对话框
        vbl = QtWidgets.QVBoxLayout()
        vbl.addWidget(ipt)
        vbl.addWidget(btn)
        
        self.setLayout(vbl)
        self.show()
    def trans_show(self,btn):
        btn.setText(a[self.count][3])
    def keyPressEvent(self, event):
        
        if (event.key() == QtCore.Qt.Key_Alt):
            self.voice_signal.emit()
        if (event.key() == QtCore.Qt.Key_Control):
            del a[self.count]
            self.voice_signal.emit()
        if (event.key() == QtCore.Qt.Key_Tab):
            self.trans_signal.emit()

    def word_check(self,edit,player,btn):
        word=a[self.count][0]
        if edit.text()==word:
            btn.setText("right")
            a[self.count][2]=a[self.count][2]+1
            self.count=self.count+1
            content = QtMultimedia.QMediaContent(QtCore.QUrl("http://dict.youdao.com/dictvoice?type=1&audio={}".format(a[self.count][0])))
            player.setMedia(content)
            player.play()
        else:
            btn.setText("wrong")
            a[self.count][1]=a[self.count][1]+1
            content = QtMultimedia.QMediaContent(QtCore.QUrl("http://dict.youdao.com/dictvoice?type=1&audio={}".format(a[self.count][0])))
            player.setMedia(content)
            player.play()
        if self.count%2==0:
            data=pd.DataFrame(a)
            data.to_csv(url,index=False,header=False,encoding="utf_8_sig")
        edit.setText("")
        edit.setFocus()
    def voice(self,player):
        content = QtMultimedia.QMediaContent(QtCore.QUrl("http://dict.youdao.com/dictvoice?type=1&audio={}".format(a[self.count][0])))
        player.setMedia(content)
        player.play()
# 创建垂直布局，并将输入框和按钮都添加到布局中
def dictmaker():
    import pandas as pd
    XML_PATH = "File/abc.xml"
    tree = ElementTree()
    tree.parse(XML_PATH)
    objs=tree.findall("item")
    wordl=[]
    for item in objs:
        word=item.find("word").text
        trans=item.find("trans").text
        if trans:
            trans=trans.replace("\n", "")
        wordl.append([word,0,0,trans])
    pd.DataFrame(wordl).to_csv("File\word.csv",index=False,header=False,encoding="utf_8_sig")
if __name__ == '__main__':
    url="File\word.csv"
    a=pd.read_csv(url,",",header=None).values.tolist()
    a.sort(key=lambda x : x[2]/2-x[1]) 
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    #print(dictmaker())
     

