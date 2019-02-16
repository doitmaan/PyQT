# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoSpinner.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(727, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(12, 136, 102, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(12, 169, 71, 16))
        self.label_2.setObjectName("label_2")
        self.labelTotalAmount = QtWidgets.QLabel(Dialog)
        self.labelTotalAmount.setGeometry(QtCore.QRect(12, 234, 376, 25))
        self.labelTotalAmount.setText("")
        self.labelTotalAmount.setObjectName("labelTotalAmount")
        self.spinBoxBookQty = QtWidgets.QSpinBox(Dialog)
        self.spinBoxBookQty.setGeometry(QtCore.QRect(310, 130, 42, 21))
        self.spinBoxBookQty.setObjectName("spinBoxBookQty")
        self.doubleSpinBoxSugarWeight = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxSugarWeight.setGeometry(QtCore.QRect(300, 170, 62, 21))
        self.doubleSpinBoxSugarWeight.setObjectName("doubleSpinBoxSugarWeight")
        self.lineEditBookAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookAmount.setEnabled(True)
        self.lineEditBookAmount.setGeometry(QtCore.QRect(120, 130, 125, 21))
        self.lineEditBookAmount.setText("")
        self.lineEditBookAmount.setObjectName("lineEditBookAmount")
        self.lineEditSugarPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarPrice.setEnabled(True)
        self.lineEditSugarPrice.setGeometry(QtCore.QRect(450, 160, 125, 21))
        self.lineEditSugarPrice.setObjectName("lineEditSugarPrice")
        self.lineEditSugarAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarAmount.setEnabled(True)
        self.lineEditSugarAmount.setGeometry(QtCore.QRect(120, 170, 125, 21))
        self.lineEditSugarAmount.setText("")
        self.lineEditSugarAmount.setObjectName("lineEditSugarAmount")
        self.lineEditBookPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookPrice.setEnabled(True)
        self.lineEditBookPrice.setGeometry(QtCore.QRect(440, 120, 125, 21))
        self.lineEditBookPrice.setObjectName("lineEditBookPrice")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.spinBoxBookQty, self.doubleSpinBoxSugarWeight)
        Dialog.setTabOrder(self.doubleSpinBoxSugarWeight, self.lineEditBookAmount)
        Dialog.setTabOrder(self.lineEditBookAmount, self.lineEditSugarAmount)
        Dialog.setTabOrder(self.lineEditSugarAmount, self.lineEditSugarPrice)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Book Price value"))
        self.label_2.setText(_translate("Dialog", "Sugar\n"
"Price"))

