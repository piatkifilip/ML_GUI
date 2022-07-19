from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenuBar

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(286, 361)



        self.OkButton = QtWidgets.QDialogButtonBox(Dialog)
        self.OkButton.setGeometry(QtCore.QRect(40, 320, 201, 31))
        self.OkButton.setOrientation(QtCore.Qt.Horizontal)
        self.OkButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.OkButton.setObjectName("OkButton")

        self.P1box = QtWidgets.QDoubleSpinBox(Dialog)
        self.P1box.setGeometry(QtCore.QRect(70, 70, 62, 22))
        self.P1box.setObjectName("P1box")
        self.P1box.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))
        self.P1boxMax = QtWidgets.QDoubleSpinBox(Dialog)
        self.P1boxMax.setGeometry(QtCore.QRect(170, 70, 62, 22))
        self.P1boxMax.setObjectName("P1boxMax")
        self.P1boxMax.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.P2box = QtWidgets.QDoubleSpinBox(Dialog)
        self.P2box.setGeometry(QtCore.QRect(70, 100, 62, 22))
        self.P2box.setObjectName("P2box")
        self.P2box.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))
        self.P2boxMax = QtWidgets.QDoubleSpinBox(Dialog)
        self.P2boxMax.setGeometry(QtCore.QRect(170, 100, 62, 22))
        self.P2boxMax.setObjectName("P2boxMax")
        self.P2boxMax.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.P3box = QtWidgets.QDoubleSpinBox(Dialog)
        self.P3box.setGeometry(QtCore.QRect(70, 130, 62, 22))
        self.P3box.setObjectName("P3box")
        self.P3box.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))
        self.P3boxMax = QtWidgets.QDoubleSpinBox(Dialog)
        self.P3boxMax.setGeometry(QtCore.QRect(170, 130, 62, 22))
        self.P3boxMax.setObjectName("P3box_2")
        self.P3boxMax.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.P4box = QtWidgets.QDoubleSpinBox(Dialog)
        self.P4box.setGeometry(QtCore.QRect(70, 160, 62, 22))
        self.P4box.setObjectName("P4box")
        self.P4box.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))
        self.P4boxMax = QtWidgets.QDoubleSpinBox(Dialog)
        self.P4boxMax.setGeometry(QtCore.QRect(170, 160, 62, 22))
        self.P4boxMax.setObjectName("P4boxMax")
        self.P4boxMax.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.P6boxMax= QtWidgets.QDoubleSpinBox(Dialog)
        self.P6boxMax.setGeometry(QtCore.QRect(170, 219, 62, 22))
        self.P6boxMax.setObjectName("P6Max")
        self.P6boxMax.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.P7box = QtWidgets.QDoubleSpinBox(Dialog)
        self.P7box.setGeometry(QtCore.QRect(70, 249, 62, 22))
        self.P7box.setObjectName("P7box")
        self.P7box.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.P5box = QtWidgets.QDoubleSpinBox(Dialog)
        self.P5box.setGeometry(QtCore.QRect(70, 189, 62, 22))
        self.P5box.setObjectName("P5box")
        self.P5box.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.P8boxMax = QtWidgets.QDoubleSpinBox(Dialog)
        self.P8boxMax.setGeometry(QtCore.QRect(170, 279, 62, 22))
        self.P8boxMax.setObjectName("P8boxMax")
        self.P8boxMax.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.P5boxMax = QtWidgets.QDoubleSpinBox(Dialog)
        self.P5boxMax.setGeometry(QtCore.QRect(170, 189, 62, 22))
        self.P5boxMax.setObjectName("P5boxMax")
        self.P5boxMax.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.P8box = QtWidgets.QDoubleSpinBox(Dialog)
        self.P8box.setGeometry(QtCore.QRect(70, 279, 62, 22))
        self.P8box.setObjectName("P8box")
        self.P8box.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.P7boxMax = QtWidgets.QDoubleSpinBox(Dialog)
        self.P7boxMax.setGeometry(QtCore.QRect(170, 249, 62, 22))
        self.P7boxMax.setObjectName("P7boxMax")
        self.P7boxMax.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.P6box = QtWidgets.QDoubleSpinBox(Dialog)
        self.P6box.setGeometry(QtCore.QRect(70, 220, 62, 21))
        self.P6box.setObjectName("P6box")
        self.P6box.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Ireland))

        self.Min = QtWidgets.QLabel(Dialog)
        self.Min.setGeometry(QtCore.QRect(80, 40, 41, 21))
        self.Min.setObjectName("Min")


        self.Max = QtWidgets.QLabel(Dialog)
        self.Max.setGeometry(QtCore.QRect(180, 40, 41, 21))
        self.Max.setObjectName("Max")

        self.P1txt = QtWidgets.QLabel(Dialog)
        self.P1txt.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.P1txt.setObjectName("P1txt")
        self.P2txt = QtWidgets.QLabel(Dialog)
        self.P2txt.setGeometry(QtCore.QRect(10, 100, 41, 21))
        self.P2txt.setObjectName("P2txt")
        self.P3txt = QtWidgets.QLabel(Dialog)
        self.P3txt.setGeometry(QtCore.QRect(10, 130, 41, 21))
        self.P3txt.setObjectName("P3txt")
        self.P4txt = QtWidgets.QLabel(Dialog)
        self.P4txt.setGeometry(QtCore.QRect(10, 160, 41, 21))
        self.P4txt.setObjectName("P4txt")
        self.P5txt = QtWidgets.QLabel(Dialog)
        self.P5txt.setGeometry(QtCore.QRect(10, 190, 41, 21))
        self.P5txt.setObjectName("P5txt")
        self.P8txt = QtWidgets.QLabel(Dialog)
        self.P8txt.setGeometry(QtCore.QRect(10, 280, 70, 21))
        self.P8txt.setObjectName("P8txt")
        self.P7txt = QtWidgets.QLabel(Dialog)
        self.P7txt.setGeometry(QtCore.QRect(10, 250, 41, 21))
        self.P7txt.setObjectName("P7txt")
        self.P6txt = QtWidgets.QLabel(Dialog)
        self.P6txt.setGeometry(QtCore.QRect(10, 220, 41, 21))
        self.P6txt.setObjectName("P6txt")

        self.retranslateUi(Dialog)
        self.OkButton.accepted.connect(Dialog.accept)
        self.OkButton.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Creating a menu bar

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Min.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">Min</span></p></body></html>"))
        self.Max.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">Max</span></p></body></html>"))
        self.P1txt.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">  </span><span style=\" font-size:11pt;\">  q</span><span style=\" font-size:9pt; vertical-align:sub;\">1</span></p></body></html>"))
        self.P2txt.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">  </span><span style=\" font-size:11pt;\">  q</span><span style=\" font-size:9pt; vertical-align:sub;\">2</span></p></body></html>"))
        self.P3txt.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">  </span><span style=\" font-size:11pt;\">  q</span><span style=\" font-size:9pt; vertical-align:sub;\">3</span></p></body></html>"))
        self.P4txt.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">  </span><span style=\" font-size:11pt;\">  q</span><span style=\" font-size:9pt; vertical-align:sub;\">4</span></p></body></html>"))
        self.P5txt.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">  </span><span style=\" font-size:11pt;\">  q</span><span style=\" font-size:9pt; vertical-align:sub;\">5</span></p></body></html>"))
        self.P6txt.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">  </span><span style=\" font-size:11pt;\">  q</span><span style=\" font-size:9pt; vertical-align:sub;\">6</span></p></body></html>"))
        self.P7txt.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">  </span><span style=\" font-size:11pt;\">  q</span><span style=\" font-size:9pt; vertical-align:sub;\">7</span></p></body></html>"))
        self.P8txt.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">  </span><span style=\" font-size:11pt;\">m</span><span style=\" font-size:9pt; vertical-align:sub;\">kN/mm</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

