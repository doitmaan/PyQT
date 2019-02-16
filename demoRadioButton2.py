# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButton2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(734, 473)
        font = QtGui.QFont()
        font.setPointSize(16)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelSelected = QtWidgets.QLabel(Dialog)
        self.labelSelected.setGeometry(QtCore.QRect(40, 380, 331, 41))
        self.labelSelected.setText("")
        self.labelSelected.setObjectName("labelSelected")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 40, 51, 77))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonMedian = QtWidgets.QRadioButton(self.widget)
        self.radioButtonMedian.setObjectName("radioButtonMedian")
        self.verticalLayout.addWidget(self.radioButtonMedian)
        self.radioButtonLarge = QtWidgets.QRadioButton(self.widget)
        self.radioButtonLarge.setObjectName("radioButtonLarge")
        self.verticalLayout.addWidget(self.radioButtonLarge)
        self.radioButtonXL = QtWidgets.QRadioButton(self.widget)
        self.radioButtonXL.setObjectName("radioButtonXL")
        self.verticalLayout.addWidget(self.radioButtonXL)
        self.radioButtonXXL = QtWidgets.QRadioButton(self.widget)
        self.radioButtonXXL.setObjectName("radioButtonXXL")
        self.verticalLayout.addWidget(self.radioButtonXXL)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(70, 210, 134, 58))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButtonDebitCard = QtWidgets.QRadioButton(self.widget1)
        self.radioButtonDebitCard.setObjectName("radioButtonDebitCard")
        self.verticalLayout_5.addWidget(self.radioButtonDebitCard)
        self.radioButtonNetBanking = QtWidgets.QRadioButton(self.widget1)
        self.radioButtonNetBanking.setObjectName("radioButtonNetBanking")
        self.verticalLayout_5.addWidget(self.radioButtonNetBanking)
        self.radioButtonCashOnDelivery = QtWidgets.QRadioButton(self.widget1)
        self.radioButtonCashOnDelivery.setObjectName("radioButtonCashOnDelivery")
        self.verticalLayout_5.addWidget(self.radioButtonCashOnDelivery)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "choose size"))
        self.label_2.setText(_translate("Dialog", "choose payment"))
        self.radioButtonMedian.setText(_translate("Dialog", "M"))
        self.radioButtonLarge.setText(_translate("Dialog", "L"))
        self.radioButtonXL.setText(_translate("Dialog", "XL"))
        self.radioButtonXXL.setText(_translate("Dialog", "XXL"))
        self.radioButtonDebitCard.setText(_translate("Dialog", "Debit/Credit Card"))
        self.radioButtonNetBanking.setText(_translate("Dialog", "NetBanking"))
        self.radioButtonCashOnDelivery.setText(_translate("Dialog", "Cash On Delivery"))

