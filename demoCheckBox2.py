# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox2.ui'
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
        self.label.setGeometry(QtCore.QRect(120, 10, 59, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 121, 16))
        self.label_3.setObjectName("label_3")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(40, 235, 231, 41))
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")
        self.groupBoxIceCreams = QtWidgets.QGroupBox(Dialog)
        self.groupBoxIceCreams.setGeometry(QtCore.QRect(170, 40, 201, 111))
        self.groupBoxIceCreams.setObjectName("groupBoxIceCreams")
        self.groupBoxDrinks = QtWidgets.QGroupBox(Dialog)
        self.groupBoxDrinks.setGeometry(QtCore.QRect(170, 140, 120, 141))
        self.groupBoxDrinks.setObjectName("groupBoxDrinks")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(180, 170, 86, 106))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxCoffee = QtWidgets.QCheckBox(self.widget)
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")
        self.verticalLayout.addWidget(self.checkBoxCoffee)
        self.checkBoxSoda = QtWidgets.QCheckBox(self.widget)
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.verticalLayout.addWidget(self.checkBoxSoda)
        self.checkBoxTea = QtWidgets.QCheckBox(self.widget)
        self.checkBoxTea.setObjectName("checkBoxTea")
        self.verticalLayout.addWidget(self.checkBoxTea)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(180, 60, 169, 41))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxChoclateChips = QtWidgets.QCheckBox(self.widget1)
        self.checkBoxChoclateChips.setObjectName("checkBoxChoclateChips")
        self.verticalLayout_2.addWidget(self.checkBoxChoclateChips)
        self.checkBoxCookieDough = QtWidgets.QCheckBox(self.widget1)
        self.checkBoxCookieDough.setObjectName("checkBoxCookieDough")
        self.verticalLayout_2.addWidget(self.checkBoxCookieDough)
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(180, 100, 150, 41))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBoxChoclateAlmond = QtWidgets.QCheckBox(self.widget2)
        self.checkBoxChoclateAlmond.setObjectName("checkBoxChoclateAlmond")
        self.verticalLayout_3.addWidget(self.checkBoxChoclateAlmond)
        self.checkBoxRockyRoad = QtWidgets.QCheckBox(self.widget2)
        self.checkBoxRockyRoad.setObjectName("checkBoxRockyRoad")
        self.verticalLayout_3.addWidget(self.checkBoxRockyRoad)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Menu"))
        self.label_2.setText(_translate("Dialog", "Select your\n"
"IceCream"))
        self.label_3.setText(_translate("Dialog", "Select your drink"))
        self.groupBoxIceCreams.setTitle(_translate("Dialog", "ice"))
        self.groupBoxDrinks.setTitle(_translate("Dialog", "drink"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee $2"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda $3"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea $1"))
        self.checkBoxChoclateChips.setText(_translate("Dialog", "Mint Choclate Chips $4"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough $2"))
        self.checkBoxChoclateAlmond.setText(_translate("Dialog", "Choclate Almond $3"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road $5"))

