from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import sys
from DialogWindow import Ui_Dialog
from MainWindow import Ui_MainWindow
import pandas as pd
import csv

class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, text, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton_5.clicked.connect(self.export)
        self.pushButton_5.clicked.connect(self.export2)

    def passdata(self):
        item = self.tableWidget.item(0,0)
        item2 = self.tableWidget.item(1,0)
        item3 = self.tableWidget.item(2,0)

        item.setText(str(self.ui.doubleSpinBox_5.value()))
        item2.setText(str(self.ui.doubleSpinBox_2.value()))
        item3.setText(str(self.ui.doubleSpinBox_3.value()))

        self.window.hide()

    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.buttonBox.clicked.connect(self.passdata)
        self.window.show()

    def export(self):
        header = ["Min", "Max"]
        with open('PARAMETERS.csv', mode= 'w') as stream:
            writer = csv.writer(stream, lineterminator='\n')
            writer.writerow(header)
            for row in range(3,self.tableWidget.rowCount()):
                rowdata = []
                for column in range(1,self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item is not None:

                        rowdata.append(item.text())
                    else:
                        rowdata.append('')

                writer.writerow(rowdata)
    def export2(self):
        header = ["Diameter", "Gauge Length", "Height"]
        with open('DIMENSIONS.csv',mode = 'w') as stream:
            writer = csv.writer(stream, lineterminator='\n')
            writer.writerow(header)
            for row in range(0, self.tableWidget.rowCount()-4):
                rowdata = []
                for column in range(0, self.tableWidget.columnCount()-2):
                    item = self.tableWidget.item(row, column)
                    if item is not None:

                        rowdata.append(item.text())
                    else:
                        rowdata.append('')

                writer.writerow(rowdata)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Ui_Dialog()
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())