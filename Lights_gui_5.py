#!/usr/bin/python3.8

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lights_gui_5.ui'

#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_LightControler(object):
    def setupUi(self, LightControler):
        LightControler.setObjectName("LightControler")
        LightControler.resize(267, 229)
        self.gridLayout = QtWidgets.QGridLayout(LightControler)
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.Lounge = QtWidgets.QLabel(LightControler)
        self.Lounge.setObjectName("Lounge")
        self.gridLayout.addWidget(self.Lounge, 0, 0, 1, 1)
        self.Lounge_Br_lable = QtWidgets.QLabel(LightControler)
        self.Lounge_Br_lable.setObjectName("Lounge_Br_lable")
        self.gridLayout.addWidget(self.Lounge_Br_lable, 0, 1, 1, 1)
        self.Powe_button = QtWidgets.QPushButton(LightControler)
        self.Powe_button.setObjectName("Powe_button")
        self.gridLayout.addWidget(self.Powe_button, 1, 0, 1, 1)
        self.Lounge_br_sl = QtWidgets.QSlider(LightControler)
        self.Lounge_br_sl.setEnabled(True)
        self.Lounge_br_sl.setMaximum(100)
        self.Lounge_br_sl.setTracking(True)
        self.Lounge_br_sl.setOrientation(QtCore.Qt.Horizontal)
        self.Lounge_br_sl.setInvertedControls(False)
        self.Lounge_br_sl.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Lounge_br_sl.setObjectName("Lounge_br_sl")
        self.gridLayout.addWidget(self.Lounge_br_sl, 1, 1, 1, 1)
        self.Lounge_tmp_lable = QtWidgets.QLabel(LightControler)
        self.Lounge_tmp_lable.setObjectName("Lounge_tmp_lable")
        self.gridLayout.addWidget(self.Lounge_tmp_lable, 2, 1, 1, 1)
        self.Lounge_col_tmp_sl = QtWidgets.QSlider(LightControler)
        self.Lounge_col_tmp_sl.setEnabled(True)
        self.Lounge_col_tmp_sl.setMaximum(100)
        self.Lounge_col_tmp_sl.setTracking(True)
        self.Lounge_col_tmp_sl.setOrientation(QtCore.Qt.Horizontal)
        self.Lounge_col_tmp_sl.setInvertedControls(False)
        self.Lounge_col_tmp_sl.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Lounge_col_tmp_sl.setObjectName("Lounge_col_tmp_sl")
        self.gridLayout.addWidget(self.Lounge_col_tmp_sl, 3, 1, 1, 1)
        self.line = QtWidgets.QFrame(LightControler)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 2)
        self.Leo_room = QtWidgets.QLabel(LightControler)
        self.Leo_room.setObjectName("Leo_room")
        self.gridLayout.addWidget(self.Leo_room, 5, 0, 1, 1)
        self.Leo_Br_lable = QtWidgets.QLabel(LightControler)
        self.Leo_Br_lable.setObjectName("Leo_Br_lable")
        self.gridLayout.addWidget(self.Leo_Br_lable, 5, 1, 1, 1)
        self.Power_button = QtWidgets.QPushButton(LightControler)
        self.Power_button.setObjectName("Power_button")
        self.gridLayout.addWidget(self.Power_button, 6, 0, 1, 1)
        self.Leos_br_sl = QtWidgets.QSlider(LightControler)
        self.Leos_br_sl.setEnabled(True)
        self.Leos_br_sl.setMaximum(100)
        self.Leos_br_sl.setTracking(True)
        self.Leos_br_sl.setOrientation(QtCore.Qt.Horizontal)
        self.Leos_br_sl.setInvertedControls(False)
        self.Leos_br_sl.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Leos_br_sl.setObjectName("Leos_br_sl")
        self.gridLayout.addWidget(self.Leos_br_sl, 6, 1, 1, 1)
        self.Leo_col_tmp_lable = QtWidgets.QLabel(LightControler)
        self.Leo_col_tmp_lable.setObjectName("Leo_col_tmp_lable")
        self.gridLayout.addWidget(self.Leo_col_tmp_lable, 7, 1, 1, 1)
        self.Leos_col_tem_sl = QtWidgets.QSlider(LightControler)
        self.Leos_col_tem_sl.setEnabled(True)
        self.Leos_col_tem_sl.setMaximum(100)
        self.Leos_col_tem_sl.setTracking(True)
        self.Leos_col_tem_sl.setOrientation(QtCore.Qt.Horizontal)
        self.Leos_col_tem_sl.setInvertedControls(False)
        self.Leos_col_tem_sl.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Leos_col_tem_sl.setObjectName("Leos_col_tem_sl")
        self.gridLayout.addWidget(self.Leos_col_tem_sl, 8, 1, 1, 1)

        self.retranslateUi(LightControler)
        self.Lounge_br_sl.valueChanged['int'].connect(self.Lounge_br_sl.setValue)
        self.Powe_button.pressed.connect(self.Powe_button.toggle)
        self.Power_button.toggled['bool'].connect(self.Power_button.toggle)
        self.Lounge_col_tmp_sl.sliderMoved['int'].connect(self.Lounge_col_tmp_sl.setValue)
        self.Leos_br_sl.valueChanged['int'].connect(self.Leos_br_sl.setValue)
        self.Leos_col_tem_sl.valueChanged['int'].connect(self.Leos_col_tem_sl.setValue)
        QtCore.QMetaObject.connectSlotsByName(LightControler)
        LightControler.setTabOrder(self.Lounge_br_sl, self.Lounge_col_tmp_sl)
        LightControler.setTabOrder(self.Lounge_col_tmp_sl, self.Power_button)
        LightControler.setTabOrder(self.Power_button, self.Leos_br_sl)
        LightControler.setTabOrder(self.Leos_br_sl, self.Leos_col_tem_sl)

    def retranslateUi(self, LightControler):
        _translate = QtCore.QCoreApplication.translate
        LightControler.setWindowTitle(_translate("LightControler", "Form"))
        self.Lounge.setText(_translate("LightControler", "Lounge"))
        self.Lounge_Br_lable.setText(_translate("LightControler", "Brightness"))
        self.Powe_button.setText(_translate("LightControler", "Power"))
        self.Lounge_tmp_lable.setText(_translate("LightControler", "Colour Temp"))
        self.Leo_room.setText(_translate("LightControler", "Leo\'s Room"))
        self.Leo_Br_lable.setText(_translate("LightControler", "Brightness"))
        self.Power_button.setText(_translate("LightControler", "Power"))
        self.Leo_col_tmp_lable.setText(_translate("LightControler", "Colour Temp"))
    
    def get_tuya_status_for_lights_online(self):
        pass
        #populate gui with appropriate data eg power toggle on, name of light
    def b_press(self, LightControler):
        pass
    def button_press(self):
        pass
    def bri_scale_moved(self):
        pass
    def col_temp_scale_moved(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LightControler = QtWidgets.QWidget()
    ui = Ui_LightControler()
    ui.setupUi(LightControler)
    LightControler.show()
    sys.exit(app.exec_())
