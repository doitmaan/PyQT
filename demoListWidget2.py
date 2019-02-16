# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(455, 300)
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 10, 151, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 0, 111, 16))
        self.label_2.setObjectName("label_2")
        self.listWidgetDiagnosis = QtWidgets.QListWidget(Dialog)
        self.listWidgetDiagnosis.setGeometry(QtCore.QRect(260, 40, 161, 171))
        self.listWidgetDiagnosis.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetDiagnosis.setObjectName("listWidgetDiagnosis")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        self.listWidgetSelectedTests = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedTests.setGeometry(QtCore.QRect(20, 30, 141, 192))
        self.listWidgetSelectedTests.setObjectName("listWidgetSelectedTests")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Diagnosis Tests"))
        self.label_2.setText(_translate("Dialog", "Selected tests are"))
        __sortingEnabled = self.listWidgetDiagnosis.isSortingEnabled()
        self.listWidgetDiagnosis.setSortingEnabled(False)
        item = self.listWidgetDiagnosis.item(0)
        item.setText(_translate("Dialog", "urin"))
        item = self.listWidgetDiagnosis.item(1)
        item.setText(_translate("Dialog", "x"))
        item = self.listWidgetDiagnosis.item(2)
        item.setText(_translate("Dialog", "y"))
        item = self.listWidgetDiagnosis.item(3)
        item.setText(_translate("Dialog", "z"))
        item = self.listWidgetDiagnosis.item(4)
        item.setText(_translate("Dialog", "w"))
        item = self.listWidgetDiagnosis.item(5)
        item.setText(_translate("Dialog", "q"))
        item = self.listWidgetDiagnosis.item(6)
        item.setText(_translate("Dialog", "a"))
        item = self.listWidgetDiagnosis.item(7)
        item.setText(_translate("Dialog", "c"))
        item = self.listWidgetDiagnosis.item(8)
        item.setText(_translate("Dialog", "d"))
        self.listWidgetDiagnosis.setSortingEnabled(__sortingEnabled)

