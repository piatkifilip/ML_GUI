# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 395)
        self.OkButton = QtWidgets.QDialogButtonBox(Dialog)
        self.OkButton.setGeometry(QtCore.QRect(230, 320, 181, 31))
        self.OkButton.setOrientation(QtCore.Qt.Horizontal)
        self.OkButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.OkButton.setObjectName("OkButton")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(180, 60, 311, 231))
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
        self.GaugeLenbox = QtWidgets.QDoubleSpinBox(self.frame)
        self.GaugeLenbox.setGeometry(QtCore.QRect(220, 60, 71, 21))
        self.GaugeLenbox.setObjectName("GaugeLenbox")
        self.GaugeDbox = QtWidgets.QDoubleSpinBox(self.frame)
        self.GaugeDbox.setGeometry(QtCore.QRect(220, 90, 71, 21))
        self.GaugeDbox.setObjectName("GaugeDbox")
        self.Heightbox = QtWidgets.QDoubleSpinBox(self.frame)
        self.Heightbox.setGeometry(QtCore.QRect(220, 120, 71, 21))
        self.Heightbox.setObjectName("Heightbox")
        self.GaugeLen = QtWidgets.QLabel(self.frame)
        self.GaugeLen.setGeometry(QtCore.QRect(10, 60, 191, 16))
        self.GaugeLen.setObjectName("GaugeLen")
        self.GaugeD = QtWidgets.QLabel(self.frame)
        self.GaugeD.setGeometry(QtCore.QRect(10, 90, 191, 21))
        self.GaugeD.setObjectName("GaugeD")
        self.Height = QtWidgets.QLabel(self.frame)
        self.Height.setGeometry(QtCore.QRect(10, 120, 201, 21))
        self.Height.setObjectName("Height")
        self.NumElbox = QtWidgets.QSpinBox(self.frame)
        self.NumElbox.setGeometry(QtCore.QRect(220, 180, 71, 21))
        self.NumElbox.setObjectName("NumElbox")
        self.NumEl = QtWidgets.QLabel(self.frame)
        self.NumEl.setGeometry(QtCore.QRect(10, 180, 201, 21))
        self.NumEl.setObjectName("NumEl")
        self.ConnectorD = QtWidgets.QLabel(self.frame)
        self.ConnectorD.setGeometry(QtCore.QRect(10, 150, 201, 16))
        self.ConnectorD.setObjectName("ConnectorD")
        self.ConnectorDbox = QtWidgets.QDoubleSpinBox(self.frame)
        self.ConnectorDbox.setGeometry(QtCore.QRect(220, 150, 71, 21))
        self.ConnectorDbox.setObjectName("ConnectorDbox")
        self.Diagram = QtWidgets.QLabel(Dialog)
        self.Diagram.setGeometry(QtCore.QRect(10, 10, 161, 371))
        self.Diagram.setText("")
        self.Diagram.setPixmap(QtGui.QPixmap("map.png"))
        self.Diagram.setScaledContents(True)
        self.Diagram.setObjectName("Diagram")

        self.retranslateUi(Dialog)
        self.OkButton.accepted.connect(Dialog.accept)
        self.OkButton.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.GaugeLen.setText(_translate("Dialog", "<html><head/><body><p>Gauge Length - <span style=\" font-style:italic;\">L</span><span style=\" font-style:italic; vertical-align:sub;\">o</span></p></body></html>"))
        self.GaugeD.setText(_translate("Dialog", "<html><head/><body><p>Gauge Diameter - <span style=\" font-style:italic;\">d</span><span style=\" font-style:italic; vertical-align:sub;\">0 </span></p></body></html>"))
        self.Height.setText(_translate("Dialog", "<html><head/><body><p>Specimen Height -<span style=\" font-style:italic;\"> L</span><span style=\" font-style:italic; vertical-align:sub;\">t</span><span style=\" font-style:italic;\"/></p></body></html>"))
        self.NumEl.setText(_translate("Dialog", "Number of Elements"))
        self.ConnectorD.setText(_translate("Dialog", "<html><head/><body><p>Connector Diameter - <span style=\" font-style:italic;\">d</span><span style=\" font-style:italic; vertical-align:sub;\">1 </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

