from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    submitClicked = QtCore.pyqtSignal(float)

    def buttonClicked(self):
        v1 = self.doubleSpinBox_1.value()
        v2 = self.doubleSpinBox_2.value()
        v3 = self.doubleSpinBox_3.value()
        v4 = self.doubleSpinBox_4.value()

        self.submitClicked.emit(v1,v2,v3,v4)
        return v1,v2,v3,v4

        sys.exit(0)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 320)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog, clicked=lambda: self.buttonClicked)
        self.buttonBox.setGeometry(QtCore.QRect(70, 280, 181, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(30, 30, 251, 231))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(165, 41, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 41, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 41, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_1.setGeometry(QtCore.QRect(160, 60, 71, 21))
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(160, 150, 71, 21))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(160, 90, 71, 21))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(160, 120, 71, 21))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 60, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 81, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Diameter"))
        self.label_2.setText(_translate("Dialog", "Gauge Length"))
        self.label_3.setText(_translate("Dialog", "Height"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())