from PyQt5 import QtCore, QtGui, QtWidgets
from DialogWindow import Ui_Dialog
import csv
import pandas as pd

class Ui_MainWindow(object):

    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def addRow(self):
        rowPos = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPos)

    def export(self):
        with open('data.csv', mode= 'w') as stream:
            writer = csv.writer(stream, lineterminator='\n')
            for row in range(self.tableWidget.rowCount()):
                rowdata = []
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item is not None:

                        rowdata.append(item.text())
                    else:
                        rowdata.append('')

                writer.writerow(rowdata)

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(160, 170, 621, 320))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["Diameter", "Gauge Length", "Height", "P1", "P2", "P3","P4"])

        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.clicked.connect(self.export)
        self.buttonSave.setGeometry(QtCore.QRect(690, 510, 90, 30))


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 170, 121, 341))
        self.label.setMaximumSize(QtCore.QSize(300, 350))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../OneDrive/Desktop/map.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")


        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.pushButton = QtWidgets.QPushButton(self.layoutWidget, clicked=lambda: self.openWindow())
        self.pushButton.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget, clicked=lambda: self.openWindow())
        self.pushButton_2.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_2.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_3.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_4.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_4.setObjectName("pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem4)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.addRow())
        self.pushButton_6.setGeometry(QtCore.QRect(580, 510, 90, 30))
        self.pushButton_6.setObjectName("pushButton_6")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(170, 510, 401, 30))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonSave.setText(_translate("MainWindow", "Finish"))
        self.pushButton.setText(_translate("MainWindow", "Material \n"
" Dimensions"))
        self.pushButton_2.setText(_translate("MainWindow", "Material \n"
" Properties"))
        self.pushButton_3.setText(_translate("MainWindow", "Other"))
        self.pushButton_4.setText(_translate("MainWindow", "View \n"
" Results"))
        self.pushButton_6.setText(_translate("MainWindow", "New Set"))
