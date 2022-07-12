from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 395)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
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
        self.GaugeLenbox.setGeometry(QtCore.QRect(200, 60, 71, 21))
        self.GaugeLenbox.setObjectName("GaugeLenbox")
        self.GaugeLenbox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.GaugeLen = QtWidgets.QLabel(self.frame)
        self.GaugeLen.setGeometry(QtCore.QRect(10, 60, 191, 21))
        self.GaugeLen.setObjectName("GaugeLen")

        self.NumElbox = QtWidgets.QSpinBox(self.frame)
        self.NumElbox.setGeometry(QtCore.QRect(200, 180, 71, 21))
        self.NumElbox.setObjectName("NumElbox")
        self.NumElbox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.NumEl = QtWidgets.QLabel(self.frame)
        self.NumEl.setGeometry(QtCore.QRect(10, 180, 201, 21))
        self.NumEl.setObjectName("NumEl")

        self.ConnectorD = QtWidgets.QLabel(self.frame)
        self.ConnectorD.setGeometry(QtCore.QRect(10, 150, 201, 16))
        self.ConnectorD.setObjectName("ConnectorD")

        self.ConnectorDbox = QtWidgets.QDoubleSpinBox(self.frame)
        self.ConnectorDbox.setGeometry(QtCore.QRect(200, 150, 71, 21))
        self.ConnectorDbox.setObjectName("ConnectorDbox")
        self.ConnectorDbox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.UnitLabel1 = QtWidgets.QLabel(self.frame)
        self.UnitLabel1.setGeometry(QtCore.QRect(280, 60, 55, 16))
        self.UnitLabel1.setObjectName("UnitLabel1")

        self.UnitLabel4 = QtWidgets.QLabel(self.frame)
        self.UnitLabel4.setGeometry(QtCore.QRect(280, 150, 55, 16))
        self.UnitLabel4.setObjectName("UnitLabel4")

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(280, 180, 55, 16))
        self.label_5.setObjectName("label_5")

        self.Height = QtWidgets.QLabel(self.frame)
        self.Height.setGeometry(QtCore.QRect(10, 90, 201, 21))
        self.Height.setObjectName("Height")

        self.UnitLabel3 = QtWidgets.QLabel(self.frame)
        self.UnitLabel3.setGeometry(QtCore.QRect(280, 90, 55, 16))
        self.UnitLabel3.setObjectName("UnitLabel3")

        self.Heightbox = QtWidgets.QDoubleSpinBox(self.frame)
        self.Heightbox.setGeometry(QtCore.QRect(200, 90, 71, 21))
        self.Heightbox.setObjectName("Heightbox")
        self.Heightbox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.Diagram = QtWidgets.QLabel(Dialog)
        self.Diagram.setGeometry(QtCore.QRect(10, 10, 161, 371))
        self.Diagram.setText("")

        self.Diagram.setPixmap(QtGui.QPixmap("map.png"))
        self.Diagram.setScaledContents(True)
        self.Diagram.setObjectName("Diagram")

        self.GaugeDbox = QtWidgets.QDoubleSpinBox(Dialog)
        self.GaugeDbox.setGeometry(QtCore.QRect(380, 180, 71, 21))
        self.GaugeDbox.setObjectName("GaugeDbox")
        self.GaugeDbox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.GaugeD = QtWidgets.QLabel(Dialog)
        self.GaugeD.setGeometry(QtCore.QRect(190, 180, 191, 21))
        self.GaugeD.setObjectName("GaugeD")

        self.UnitLabel2 = QtWidgets.QLabel(Dialog)
        self.UnitLabel2.setGeometry(QtCore.QRect(460, 180, 55, 16))
        self.UnitLabel2.setObjectName("UnitLabel2")


        self.retranslateUi(Dialog)

        self.OkButton.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.GaugeLen.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">Gauge Length - </span><span style=\" font-size:9pt; font-style:italic;\">L</span><span style=\" font-size:9pt; font-style:italic; vertical-align:sub;\">o</span></p></body></html>"))
        self.NumEl.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">Minimum Element Size</span></p></body></html>"))
        self.ConnectorD.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">Connector Diameter - </span><span style=\" font-size:9pt; font-style:italic;\">d</span><span style=\" font-size:9pt; font-style:italic; vertical-align:sub;\">1 </span></p></body></html>"))
        self.UnitLabel1.setText(_translate("Dialog", "mm"))
        self.UnitLabel4.setText(_translate("Dialog", "mm"))
        self.label_5.setText(_translate("Dialog", "µm"))
        self.Height.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">Specimen Height -</span><span style=\" font-size:9pt; font-style:italic;\"> L</span><span style=\" font-size:9pt; font-style:italic; vertical-align:sub;\">t</span></p></body></html>"))
        self.UnitLabel3.setText(_translate("Dialog", "mm"))
        self.GaugeD.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">Gauge Diameter - </span><span style=\" font-size:9pt; font-style:italic;\">d</span><span style=\" font-size:9pt; font-style:italic; vertical-align:sub;\">0 </span></p></body></html>"))
        self.UnitLabel2.setText(_translate("Dialog", "mm"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())