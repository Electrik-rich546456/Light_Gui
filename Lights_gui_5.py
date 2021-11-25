#!/usr/bin/python3.8
#import time
from PyQt5 import QtCore, QtWidgets
from functools import partial
import tinytuya
import json
from threading import Thread

#Using threads to turn 3 lights 
#on at same time as they are all on one pendant



with open('snapshot.json') as json_file:
    jdata = json.load(json_file)

br_counter = 0
br2 = 0
col_counter = 0
pow = True
def lights(name, *num):
#    1 = on/ off toggle
#    2 = just off
#    3 = Full Brightness
#    4 = Brightness and temp according to counter
#    5 = Brightness only according to counter
#    6 = Colour Tempature only according to counter
    global br_counter, col_counter
    for item in jdata["devices"]:
        if item["name"] == name:
            break
    d = tinytuya.BulbDevice(item["id"], item["ip"], item["key"])
    d.set_version(float(item["ver"]))
    d.set_socketPersistent(True)
    data = d.status()
    for n in num:
        if n == 2:
            d.turn_off()
        if n == 1:
            if(data['dps']['20'] == True):
                #print("its on Turning off")
                d.turn_off()
            elif(data['dps']['20'] == False):
                #print("its off Turing on")
                d.turn_on()
        if n == 3:
            d.set_brightness_percentage(brightness=100)
            d.set_colourtemp_percentage(100)
        if n == 4:
            #print(counter)
            d.set_brightness_percentage(br_counter)
            d.set_colourtemp_percentage(br_counter)
        if n == 5:
            d.set_brightness_percentage(br_counter)            
        if n == 6:
            d.set_colourtemp_percentage(col_counter) 

################status get from tuya######
def l_status(name,  *sta):
# sta's ### statuses
# 1 = Brightness 
# 2 = Colour Temp
# 3 = Power Status 
    for item in jdata["devices"]:
        if item["name"] == name:
            break
    d = tinytuya.BulbDevice(item["id"], item["ip"], item["key"])
    d.set_version(float(item["ver"]))
    status = d.status()
    global br_counter, col_counter,  pow
    #print('Status',  status)
    for n in sta:
        if n == 1:
            br_counter = (int(status['dps']['22']) // 10)
            #print('Brightness', (br_counter))
            return br_counter
        if n == 2:
            col_counter = (int(status['dps']['23']) //10)
            #print('Color Temp',  col_counter)
            return col_counter
        if n ==3:
            if(status['dps']['20'] == True):
                pow = True
                #print(pow)
                return pow
                #print("its on")                
            elif(status['dps']['20'] == False):
                pow = False
                return pow
                #print("its off")
###############################
#print(type(br_counter))
l_status('Light_3', 1)
l_status('Light_3', 2)
l_status('Light_3', 3)

#print(br_counter)

#######
####Gui stuff
class Ui_Lights(object):
    def setupUi(self, Lights):
        global br_counter,  col_counter
        Lights.setObjectName("Lights")
        Lights.setEnabled(True)
        Lights.resize(315, 133)
#        self.setWindowIcon(QtCore.QIcon("icon.png"))
#        setIcon(QMessageBox.Information)
#        self.setWindowIcon(QtGui.QIcon('logo.png'))

        self.hidden = QtWidgets.QWidget(Lights)
        self.hidden.setObjectName("hidden")
        self.label = QtWidgets.QLabel(self.hidden)
        self.label.setGeometry(QtCore.QRect(30, 10, 57, 15))
        self.label.setObjectName("label")
        self.Br_Slide = QtWidgets.QSlider(self.hidden)
        self.Br_Slide.setGeometry(QtCore.QRect(120, 30, 170, 16))
        
        self.Br_Slide.setMinimum(0)
        self.Br_Slide.setMaximum(100)
        
        self.Br_Slide.setValue(l_status('Light_3', 1))
        self.Br_Slide.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Br_Slide.setTickInterval(10)
        self.Br_Slide.setSingleStep(10)
#        self.label_4.label = QtWidgets.QLabel("0")

        self.Br_Slide.setOrientation(QtCore.Qt.Horizontal)
        self.Br_Slide.setObjectName("Br_Slide")
        
        self.hoz_line = QtWidgets.QFrame(self.hidden)
        self.hoz_line.setGeometry(QtCore.QRect(0, 140, 591, 20))
        self.hoz_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.hoz_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hoz_line.setObjectName("hoz_line")
        self.Vert_line_2 = QtWidgets.QFrame(self.hidden)
        self.Vert_line_2.setGeometry(QtCore.QRect(100, -40, 20, 511))
        self.Vert_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.Vert_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Vert_line_2.setObjectName("Vert_line_2")
        self.Col_Slide = QtWidgets.QSlider(self.hidden)
        self.Col_Slide.setGeometry(QtCore.QRect(120, 90, 170, 16))
        self.Col_Slide.setMinimum(0)
        self.Col_Slide.setMaximum(100)
        self.Col_Slide.setValue(l_status('Light_3', 2))
        self.Col_Slide.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Col_Slide.setTickInterval(10)
        self.Col_Slide.setSingleStep(10)
        self.Col_Slide.setOrientation(QtCore.Qt.Horizontal)
        self.Col_Slide.setObjectName("Col_Slide")
        self.label_2 = QtWidgets.QLabel(self.hidden)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 71, 16))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.hidden)
        self.label_3.setGeometry(QtCore.QRect(120, 60, 141, 20))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.hidden)
        self.label_4.setGeometry(QtCore.QRect(265, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText(str(br_counter))
        
        self.label_5 = QtWidgets.QLabel(self.hidden)
        self.label_5.setGeometry(QtCore.QRect(265, 60, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setText(str(col_counter))
        
        self.pushButton = QtWidgets.QPushButton(self.hidden)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 80, 23))
        self.pushButton.setCheckable(True)
#     self.pushButton.setChecked(True)
        self.pushButton.setChecked(pow)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        Lights.setCentralWidget(self.hidden)
        self.statusbar = QtWidgets.QStatusBar(Lights)
        self.statusbar.setObjectName("statusbar")
        Lights.setStatusBar(self.statusbar)
        self.checkBox = QtWidgets.QCheckBox(self.hidden)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QtCore.QRect(10, 80, 51, 16))

        self.retranslateUi(Lights)
        self.statusbar.messageChanged['QString'].connect(self.statusbar.showMessage)
        self.Br_Slide.valueChanged.connect(self.br_Slide)
        self.Col_Slide.valueChanged['int'].connect(self.col_slide)
        self.pushButton.clicked.connect(partial(self.clicked_btn))
        self.checkBox.toggled.connect(self.ticked)

        
        #self.pushButton.clicked['bool'].connect(Lights.setAnimated)
        #QtCore.QMetaObject.connectSlotsByName(Lights)

    def retranslateUi(self, Lights):
        _translate = QtCore.QCoreApplication.translate
        Lights.setWindowTitle(_translate("Lights", "Light Controller"))
        self.label.setText(_translate("Lights", "Lounge"))
        self.label_2.setText(_translate("Lights", "Brightness"))
        self.label_3.setText(_translate("Lights", "Color Temperature"))
        self.label_4.setText(_translate("Lights",  str(br_counter)))
        self.label_5.setText(_translate("Lights",  str(col_counter)))
        self.checkBox.setText(_translate("Lights", u"Lock", None))

        self.pushButton.setText(_translate("Lights", "Power"))
    def clicked_btn(self, value):
        Thread(target = lights, args=('Light_1', 1)).start()
        Thread(target = lights, args=('Light_2', 1)).start() #Living Room
        Thread(target = lights, args=('Light_3', 1)).start()
        
###testing to see btn click in terminal
#        print(value)
    
    def br_Slide(self):
        global br_counter
        br_counter = int(self.Br_Slide.value())
        self.label_4.setText(str(br_counter))
        Thread(target = lights, args=('Light_1', 5)).start()
        Thread(target = lights, args=('Light_2', 5)).start() #Living Room
        Thread(target = lights, args=('Light_3', 5)).start()
        
        
#        testing to see Br_Slide value in terminal
#        my_br = str(self.Br_Slide.value())
#        print('Brightness' , my_br)
    def col_slide(self):
        global col_counter
        col_counter = int(self.Col_Slide.value())
        self.label_5.setText(str(col_counter))
        Thread(target = lights, args=('Light_1', 6)).start()
        Thread(target = lights, args=('Light_2', 6)).start() #Living Room
        Thread(target = lights, args=('Light_3', 6)).start()
    def ticked(self,  value):
        if value:
            print("ticked",  value)
        else:
            print("ticked^%U&*B&*b",  value)
        

#        testing to see Col_Slide value in terminal.
#        my_colour = str(self.Col_Slide.value())
#        print('Colour' , my_colour)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Lights = QtWidgets.QMainWindow()
    ui = Ui_Lights()
    ui.setupUi(Lights)
    Lights.show()
    sys.exit(app.exec_())
