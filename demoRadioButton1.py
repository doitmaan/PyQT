# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButton1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 191, 16))
        self.label.setObjectName("label")
        self.LabelFare = QtWidgets.QLabel(Dialog)
        self.LabelFare.setGeometry(QtCore.QRect(70, 200, 241, 16))
        self.LabelFare.setText("")
        self.LabelFare.setObjectName("LabelFare")
        self.radioButtonBusinessClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonBusinessClass.setGeometry(QtCore.QRect(50, 60, 221, 20))
        self.radioButtonBusinessClass.setObjectName("radioButtonBusinessClass")
        self.radioButtonEconomyClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEconomyClass.setGeometry(QtCore.QRect(50, 110, 101, 20))
        self.radioButtonEconomyClass.setObjectName("radioButtonEconomyClass")
        self.adioButtonFirstClass = QtWidgets.QRadioButton(Dialog)
        self.adioButtonFirstClass.setGeometry(QtCore.QRect(50, 30, 221, 20))
        self.adioButtonFirstClass.setObjectName("adioButtonFirstClass")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose the flight type"))
        self.radioButtonBusinessClass.setText(_translate("Dialog", "Business Class $125"))
        self.radioButtonEconomyClass.setText(_translate("Dialog", "Economy Class $100"))
        self.adioButtonFirstClass.setText(_translate("Dialog", "First Class $150"))

