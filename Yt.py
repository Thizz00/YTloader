
from youtubesearchpython import VideosSearch
import pytube 
from PyQt5.QtCore import Qt,QPoint
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import webbrowser
import youtube_dl
class Ui_Form(object):
    def setupUi(self,Form):
        def close_clicked(self):
                self.close()
        def fb():
                webbrowser.open("https://www.facebook.com/profile.php?id=100004259290790&sk=about")
        def yt():
                webbrowser.open("https://www.youtube.com/channel/UCzLnIfC562M6ZgI2V3Y3wnQ")
        def browse():
                webbrowser.open("https://kielbjakub.netlify.app")
        def do_action(self):
            url= self.text()
        def Downloader(self):
                print(pytube.YouTube(self).streams.get_highest_resolution().download('../Video'))
                #youtube = pytube.YouTube(self)
                #video = youtube.streams.first()
                #video.download('../Video')
                #dictionary= {}
               # with youtube_dl.YoutubeDL(dictionary) as dictionary:
                        #dictionary.download([self])
        Form.setObjectName("Form")
        Form.resize(625, 565)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 30, 550, 500))
        font = QtGui.QFont()
        font.setKerning(False)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image:url(:/images/LxJwPs.jpg);\n"
"border-top-left-radius:50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(320, 30, 231, 430))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:white;\n"
"border-bottom-right-radius:50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(350, 20, 241, 80))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#1b2037;")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 150, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgb(59,64,116);\n"
"color:#3b4074;\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        #self.lineEdit.returnPressed.connect(lambda: do_action(self))
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(320, 280, 231, 16))
        self.line.setStyleSheet("color:rgb(65,55,78)")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(330, 220, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(82,84,100),stop:1 rgb(59,64,116));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(59,64,116),stop:1 rgb(135,143,177));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(111,81,118);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: Downloader(self.lineEdit.text()))
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 340, 231, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(35, 35))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(82,84,100),stop:1 rgb(59,64,116));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(59,64,116),stop:1 rgb(135,143,177));\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(111,81,118);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(yt)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(35, 35))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(82,84,100),stop:1 rgb(59,64,116));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(59,64,116),stop:1 rgb(135,143,177));\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(111,81,118);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(browse)
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(35, 35))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(82,84,100),stop:1 rgb(59,64,116));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(59,64,116),stop:1 rgb(135,143,177));\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(111,81,118);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(fb)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(360, 430, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#1b2037;")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(390, 80, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#1b2037;")
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(530, 30, 21, 23))
        font = QtGui.QFont()
        font.setFamily("font bottons music")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5{\n"
"background-color: rgba(255, 255, 255, 0)\n"
"}\n"
"QPushButton#pushButton_5:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(59,64,116),stop:1 rgb(135,143,177));\n"
"}\n"
"QPushButton#pushButton_5:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(111,81,118);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda:close_clicked(self))
        self.label_3.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.line.raise_()
        self.pushButton.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.pushButton_5.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", " Video Downloader"))
        self.lineEdit.setPlaceholderText(_translate("Form", " link to the video"))
        self.pushButton.setText(_translate("Form", "Download"))
        self.pushButton_4.setText(_translate("Form", "M"))
        self.pushButton_3.setText(_translate("Form", "v"))
        self.pushButton_2.setText(_translate("Form", "E"))
        self.label_2.setText(_translate("Form", "All right reserved. Jakub Kiełb 2021 © "))
        self.label_5.setText(_translate("Form", "Fast and Free"))
        self.pushButton_5.setText(_translate("Form", "t"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
