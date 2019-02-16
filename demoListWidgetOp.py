# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidgetOp.ui'
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
        self.label.setGeometry(QtCore.QRect(28, 60, 91, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 60, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(120, 110, 114, 32))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(270, 100, 101, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushButtonEdit = QtWidgets.QPushButton(Dialog)
        self.pushButtonEdit.setGeometry(QtCore.QRect(120, 150, 114, 32))
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.pushButtonDeleteAll = QtWidgets.QPushButton(Dialog)
        self.pushButtonDeleteAll.setGeometry(QtCore.QRect(120, 230, 114, 32))
        self.pushButtonDeleteAll.setObjectName("pushButtonDeleteAll")
        self.pushButtonDelete = QtWidgets.QPushButton(Dialog)
        self.pushButtonDelete.setGeometry(QtCore.QRect(120, 190, 114, 32))
        self.pushButtonDelete.setObjectName("pushButtonDelete")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter an item"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add"))
        self.pushButtonEdit.setText(_translate("Dialog", "Edit"))
        self.pushButtonDeleteAll.setText(_translate("Dialog", "Delete All"))
        self.pushButtonDelete.setText(_translate("Dialog", "Delete"))

