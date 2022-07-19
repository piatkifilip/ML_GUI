# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog3(object):

    CSAval = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 200)
        Dialog.setMinimumSize(QtCore.QSize(200, 200))
        Dialog.setMaximumSize(QtCore.QSize(200, 200))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)

        self.pushButton.setGeometry(QtCore.QRect(50, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 90, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 121, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        # Create a hidden label, value of diameter will be assigned to label
        # Once window is opened. When the user clicks "Calculate" it will use the
        # Value from the label to calculate the CSA

        self.hiddenLabel = QtWidgets.QSpinBox(Dialog)
        self.hiddenLabel.move(100,100)
        self.hiddenLabel.setHidden(True)
        self.hiddenLabel.setValue(10)

        self.pushButton.clicked.connect(self.calcCSA)


    def calcCSA(self):
        self.diameter = self.hiddenLabel.value()
        self.CSA = (np.square(self.diameter))*np.pi
        self.lineEdit.setText(str(round(self.CSA, 6)))
        Ui_Dialog3.CSAval = self.CSA

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Calculate"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Cross-Sectional </p><p align=\"center\"> Area is</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

