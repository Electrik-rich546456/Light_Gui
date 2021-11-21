#!/usr/bin/python3.8
import time
from PyQt5 import QtCore, QtWidgets
from functools import partial
import tinytuya
import json
from threading import Thread

with open('snapshot.json') as json_file:
    jdata = json.load(json_file)

counter = 0
def lights(name, *num):
#    1 = on/ off toggle
#    2 = just off
#    3 = Full Brightness
#    4 = Brightness according to counter
    global counter
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
            d.set_brightness_percentage(counter)
            d.set_colourtemp_percentage(counter)
            time.sleep(1)
            #print(counter)
            if counter == 100:
                counter = 0


####Gui stuff
class Ui_Lights(object):
    def setupUi(self, Lights):
        Lights.setObjectName("Lights")
        Lights.setEnabled(True)
        Lights.resize(315, 133)
        self.hidden = QtWidgets.QWidget(Lights)
        self.hidden.setObjectName("hidden")
        self.label = QtWidgets.QLabel(self.hidden)
        self.label.setGeometry(QtCore.QRect(30, 10, 57, 15))
        self.label.setObjectName("label")
        self.Br_Slide = QtWidgets.QSlider(self.hidden)
        self.Br_Slide.setGeometry(QtCore.QRect(120, 30, 170, 16))
        self.Br_Slide.setMaximum(100)
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
        self.Col_Slide.setMaximum(100)
        self.Col_Slide.setOrientation(QtCore.Qt.Horizontal)
        self.Col_Slide.setObjectName("Col_Slide")
        self.label_2 = QtWidgets.QLabel(self.hidden)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.hidden)
        self.label_3.setGeometry(QtCore.QRect(150, 60, 141, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.hidden)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 80, 23))
        self.pushButton.setCheckable(True)
#     self.pushButton.setChecked(True)
        self.pushButton.setChecked(False)
        
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        Lights.setCentralWidget(self.hidden)
        self.statusbar = QtWidgets.QStatusBar(Lights)
        self.statusbar.setObjectName("statusbar")
        Lights.setStatusBar(self.statusbar)

        self.retranslateUi(Lights)
        self.statusbar.messageChanged['QString'].connect(self.statusbar.showMessage)
        self.Br_Slide.valueChanged.connect(self.br_Slide)
        self.Col_Slide.valueChanged['int'].connect(self.col_slide)
        self.pushButton.clicked.connect(partial(self.clicked_btn))
        
        #self.pushButton.clicked['bool'].connect(Lights.setAnimated)
        #QtCore.QMetaObject.connectSlotsByName(Lights)

    def retranslateUi(self, Lights):
        _translate = QtCore.QCoreApplication.translate
        Lights.setWindowTitle(_translate("Lights", "Light Controller"))
        self.label.setText(_translate("Lights", "Lounge"))
        self.label_2.setText(_translate("Lights", "Brightness"))
        self.label_3.setText(_translate("Lights", "Color Temperature"))
        self.pushButton.setText(_translate("Lights", "Power"))
    def clicked_btn(self, value):
        Thread(target = lights, args=('Light_1', 1)).start()
        Thread(target = lights, args=('Light_2', 1)).start() #Living Room
        Thread(target = lights, args=('Light_3', 1)).start()
        
###testing###
#        print(value)
#        self.pushButton.isChecked() #think it checks said button
#        print('ok')
#        self.pushButton.setChecked(False) # changes btn state 
#        print('done')

    def br_Slide(self):
        global counter 
        counter = int(self.Br_Slide.value())
        lights('Light_3',4)
        
#        testing
#        my_br = str(self.Br_Slide.value())
#        print('Brightness' , my_br)
    def col_slide(self):
        pass
#        testing
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
