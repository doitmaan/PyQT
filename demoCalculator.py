# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(504, 300)
        self.pushButtonPlus = QtWidgets.QPushButton(Dialog)
        self.pushButtonPlus.setGeometry(QtCore.QRect(30, 190, 114, 32))
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.labelFirstNumber = QtWidgets.QLabel(Dialog)
        self.labelFirstNumber.setGeometry(QtCore.QRect(120, 60, 131, 16))
        self.labelFirstNumber.setObjectName("labelFirstNumber")
        self.labelSecondNumber = QtWidgets.QLabel(Dialog)
        self.labelSecondNumber.setGeometry(QtCore.QRect(110, 110, 161, 16))
        self.labelSecondNumber.setObjectName("labelSecondNumber")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(50, 260, 411, 20))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.lineEditFirstNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirstNumber.setGeometry(QtCore.QRect(250, 60, 113, 21))
        self.lineEditFirstNumber.setObjectName("lineEditFirstNumber")
        self.lineEditSecondNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecondNumber.setGeometry(QtCore.QRect(250, 110, 113, 21))
        self.lineEditSecondNumber.setObjectName("lineEditSecondNumber")
        self.pushButtonSubtract = QtWidgets.QPushButton(Dialog)
        self.pushButtonSubtract.setGeometry(QtCore.QRect(140, 190, 114, 32))
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.pushButtonMultiply = QtWidgets.QPushButton(Dialog)
        self.pushButtonMultiply.setGeometry(QtCore.QRect(250, 190, 114, 32))
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.pushButtonDivide = QtWidgets.QPushButton(Dialog)
        self.pushButtonDivide.setGeometry(QtCore.QRect(360, 190, 114, 32))
        self.pushButtonDivide.setObjectName("pushButtonDivide")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonPlus.setText(_translate("Dialog", "+"))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter First Number"))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter Second Number"))
        self.pushButtonSubtract.setText(_translate("Dialog", "-"))
        self.pushButtonMultiply.setText(_translate("Dialog", "x"))
        self.pushButtonDivide.setText(_translate("Dialog", "/"))

