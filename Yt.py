
import pytube 
from PyQt5 import QtCore, QtGui, QtWidgets
import static.icons
import sys
from socialmedia import smedia
from static.PushbuttonsStyles import stylesheetclass
class Ui_Form(object):
    def setupUi(self,Form):
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
        self.pushButton.setStyleSheet(stylesheetclass.pushbuttonDesign(self))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self. get_movie_from_link())

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 340, 231, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_yt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_yt.setMaximumSize(QtCore.QSize(35, 35))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(14)
        self.pushButton_yt.setFont(font)
        self.pushButton_yt.setStyleSheet(stylesheetclass.pushbuttonDesign(self))
        self.pushButton_yt.setObjectName("pushButton_yt")
        self.horizontalLayout.addWidget(self.pushButton_yt)
        self.pushButton_yt.clicked.connect(smedia.yt)

        self.pushButton_mysite = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_mysite.setMaximumSize(QtCore.QSize(35, 35))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(14)
        self.pushButton_mysite.setFont(font)
        self.pushButton_mysite.setStyleSheet(stylesheetclass.pushbuttonDesign(self))
        self.pushButton_mysite.setObjectName("pushButton_mysite")
        self.pushButton_mysite.clicked.connect(smedia.browse)
        self.horizontalLayout.addWidget(self.pushButton_mysite)

        self.pushButton_fb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_fb.setMaximumSize(QtCore.QSize(35, 35))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(14)
        self.pushButton_fb.setFont(font)
        self.pushButton_fb.setStyleSheet(stylesheetclass.pushbuttonDesign(self))
        self.pushButton_fb.setObjectName("pushButton_fb")
        self.pushButton_fb.clicked.connect(smedia.fb)
        self.horizontalLayout.addWidget(self.pushButton_fb)

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

        self.pushButton_closeapp = QtWidgets.QPushButton(self.widget)
        self.pushButton_closeapp.setGeometry(QtCore.QRect(530, 30, 21, 23))
        font = QtGui.QFont()
        font.setFamily("font bottons music")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_closeapp.setFont(font)
        self.pushButton_closeapp.setStyleSheet(stylesheetclass.pushbuttonclose(self))
        self.pushButton_closeapp.setObjectName("pushButton_closeapp")
        self.pushButton_closeapp.clicked.connect(lambda:sys.exit())

        self.label_3.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.line.raise_()
        self.pushButton.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.pushButton_closeapp.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", " Video Downloader"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Paste link to movie"))
        self.pushButton.setText(_translate("Form", "Download"))
        self.pushButton_yt.setText(_translate("Form", "M"))
        self.pushButton_mysite.setText(_translate("Form", "v"))
        self.pushButton_fb.setText(_translate("Form", "E"))
        self.label_2.setText(_translate("Form", "All right reserved. Jakub Kiełb 2021 © "))
        self.label_5.setText(_translate("Form", "Fast and Free"))
        self.pushButton_closeapp.setText(_translate("Form", "t"))
        
    def get_movie_from_link(self):
              if len(self.lineEdit.text())==0:
                    self.lineEdit.setPlaceholderText("Please paste link to movie")
              else:
                    try:
                        print(pytube.YouTube(self.lineEdit.text()).streams.get_highest_resolution().download('../Video'))
                    except:
                        self.lineEdit.setText("")
                        self.lineEdit.setPlaceholderText("It is not a link to movie")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
