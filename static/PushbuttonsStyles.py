class stylesheetclass(object):
    def pushbuttonDesign(self):
        return("QPushButton{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(82,84,100),stop:1 rgb(59,64,116));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(59,64,116),stop:1 rgb(135,143,177));\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(111,81,118);\n"
"}")
    def pushbuttonclose(self):
        return("QPushButton{\n"
"background-color: rgba(255, 255, 255, 0)\n"
"}\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgb(59,64,116),stop:1 rgb(135,143,177));\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(111,81,118);\n"
"}")