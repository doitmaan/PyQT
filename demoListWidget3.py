# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget3.ui'
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
        self.label.setGeometry(QtCore.QRect(60, 50, 59, 16))
        self.label.setObjectName("label")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(50, 250, 114, 32))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.lineEditFoodItem = QtWidgets.QLineEdit(Dialog)
        self.lineEditFoodItem.setGeometry(QtCore.QRect(30, 20, 113, 21))
        self.lineEditFoodItem.setObjectName("lineEditFoodItem")
        self.listWidgetSelectedItems = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedItems.setGeometry(QtCore.QRect(180, 50, 181, 181))
        self.listWidgetSelectedItems.setObjectName("listWidgetSelectedItems")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "your fav"))
        self.pushButtonAdd.setText(_translate("Dialog", "ADD"))

