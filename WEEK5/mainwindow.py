# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 580)
        MainWindow.setMinimumSize(QtCore.QSize(800, 580))
        MainWindow.setMaximumSize(QtCore.QSize(800, 580))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        # Create Value Table
        self.ValTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ValTable.setGeometry(QtCore.QRect(20, 240, 361, 221))
        self.ValTable.setObjectName("ValTable")
        self.ValTable.setColumnCount(1)
        self.ValTable.setRowCount(5)

        # Set Font and Font Size for relevant Headers etc
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ValTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ValTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ValTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ValTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ValTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ValTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ValTable.setItem(0, 0, item)
        self.FinishButton = QtWidgets.QPushButton(self.centralwidget)
        self.FinishButton.setGeometry(QtCore.QRect(690, 490, 90, 30))
        self.FinishButton.setObjectName("FinishButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.ButtonLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.ButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonLayout.setObjectName("ButtonLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ButtonLayout.addItem(spacerItem)

        # Define Specimen Geometry Button - Used to open DialogWindow1
        self.SpecGeoButton = QtWidgets.QPushButton(self.layoutWidget)
        self.SpecGeoButton.setMinimumSize(QtCore.QSize(90, 90))
        self.SpecGeoButton.setMaximumSize(QtCore.QSize(90, 90))
        self.SpecGeoButton.setObjectName("SpecGeoButton")
        self.ButtonLayout.addWidget(self.SpecGeoButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ButtonLayout.addItem(spacerItem1)


        # Define Parameter Button - Used to open paramater DialogWindow2
        self.ParameterButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ParameterButton.setMinimumSize(QtCore.QSize(90, 90))
        self.ParameterButton.setMaximumSize(QtCore.QSize(90, 90))
        self.ParameterButton.setObjectName("ParameterButton")
        self.ButtonLayout.addWidget(self.ParameterButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ButtonLayout.addItem(spacerItem2)

        # Define 'Other' Button - Large button on top right - Currently no use
        self.RunButton = QtWidgets.QPushButton(self.layoutWidget)
        self.RunButton.setMinimumSize(QtCore.QSize(90, 90))
        self.RunButton.setMaximumSize(QtCore.QSize(90, 90))
        self.RunButton.setObjectName("RunButton")
        self.ButtonLayout.addWidget(self.RunButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ButtonLayout.addItem(spacerItem3)

        # Define 'Results' Button - Large button on top Right - Currently no use
        self.ResultsButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ResultsButton.setMinimumSize(QtCore.QSize(90, 90))
        self.ResultsButton.setMaximumSize(QtCore.QSize(90, 90))
        self.ResultsButton.setObjectName("ResultsButton")
        self.ButtonLayout.addWidget(self.ResultsButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ButtonLayout.addItem(spacerItem4)

        # Clear button - Used to wipe all data from the Tables
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(590, 490, 90, 30))
        self.ClearButton.setObjectName("ClearButton")

        # Progress bar - Currently has no function other than visual
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 490, 401, 30))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        # Create Parameter Table
        self.ParamTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ParamTable.setGeometry(QtCore.QRect(430, 240, 341, 221))
        self.ParamTable.setObjectName("ParamTable")
        self.ParamTable.setColumnCount(2)
        self.ParamTable.setRowCount(8)

        # Set Font and Font Size for relevant Headers etc
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ParamTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ParamTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ParamTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ParamTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ParamTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ParamTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ParamTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.ParamTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ParamTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.ParamTable.setHorizontalHeaderItem(1, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 180, 761, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        #Status and MenuBar - Currently have no use - Might implement features in the future
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Define values so they can be passed from DialogWindow1 into table
        val1 = QtWidgets.QTableWidgetItem()
        self.ValTable.setItem(0,0,val1)
        val2 = QtWidgets.QTableWidgetItem()
        self.ValTable.setItem(1, 0, val2)
        val3 = QtWidgets.QTableWidgetItem()
        self.ValTable.setItem(2, 0, val3)
        val4 = QtWidgets.QTableWidgetItem()
        self.ValTable.setItem(3, 0, val4)
        val5 = QtWidgets.QTableWidgetItem()
        self.ValTable.setItem(4, 0, val5)

        # Define values so they can be passed from DialogWindow2 into table
        P1valmin = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(0,0,P1valmin)
        P2valmin = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(1, 0, P2valmin)
        P3valmin = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(2, 0, P3valmin)
        P4valmin = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(3, 0, P4valmin)
        P5valmin = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(4, 0, P5valmin)
        P6valmin = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(5, 0, P6valmin)
        P7valmin = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(6, 0, P7valmin)
        P8valmin = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(7, 0, P8valmin)

        P1valmax = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(0, 1, P1valmax)
        P2valmax = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(1, 1, P2valmax)
        P3valmax = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(2, 1, P3valmax)
        P4valmax = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(3, 1, P4valmax)
        P5valmax = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(4, 1, P5valmax)
        P6valmax = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(5, 1, P6valmax)
        P7valmax = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(6, 1, P7valmax)
        P8valmax = QtWidgets.QTableWidgetItem()
        self.ParamTable.setItem(7, 1, P8valmax)

        # Create hidden spinbox to store value of diameter as int

        self.hiddenValueMain = QtWidgets.QSpinBox(self.centralwidget)
        self.hiddenValueMain.move(10,10)
        self.hiddenValueMain.setHidden(False)
        self.hiddenValueMain.setValue(5)

        # Adding Icons

        self.SpecGeoButton.setIcon(QtGui.QIcon('height.png'))
        self.SpecGeoButton.setIconSize(QSize(30,40))

        self.ParameterButton.setIcon(QtGui.QIcon('bounding-box.png'))
        self.ParameterButton.setIconSize(QSize(30, 40))

        self.ResultsButton.setIcon(QtGui.QIcon('research.png'))
        self.ResultsButton.setIconSize(QSize(25,40))

        self.RunButton.setIcon(QtGui.QIcon('input.png'))
        self.RunButton.setIconSize(QSize(30,40))

        self.SpecLabel = QtWidgets.QLabel(self.centralwidget)
        self.SpecLabel.move(115, 90)
        self.SpecLabel.setText('Specimen\nGeometry')

        self.ParameterLabel = QtWidgets.QLabel(self.centralwidget)
        self.ParameterLabel.move(285, 90)
        self.ParameterLabel.setText('Parameter\n  Bounds')

        self.runLabel = QtWidgets.QLabel(self.centralwidget)
        self.runLabel.move(460,90)
        self.runLabel.setText('Calculate')

        self.resultsLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultsLabel.move(640,90)
        self.resultsLabel.setText(' View \nResults')


    # Function used to create titles/names
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.ValTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Gauge Diameter - mm"))
        item = self.ValTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Gauge Length - mm"))
        item = self.ValTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Specimen Height - mm"))
        item = self.ValTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Connector Diamater - mm"))
        item = self.ValTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Number of Elements - µm"))
        item = self.ValTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Value"))
        __sortingEnabled = self.ValTable.isSortingEnabled()
        self.ValTable.setSortingEnabled(False)
        self.ValTable.setSortingEnabled(__sortingEnabled)
        self.FinishButton.setText(_translate("MainWindow", "Finish"))


        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        item = self.ParamTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "P1"))
        item = self.ParamTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "P2"))
        item = self.ParamTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "P3"))
        item = self.ParamTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "P4"))
        item = self.ParamTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "P5"))
        item = self.ParamTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "P6"))
        item = self.ParamTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "P7"))
        item = self.ParamTable.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "P8"))
        item = self.ParamTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Min"))
        item = self.ParamTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Max"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Selected Variables</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

