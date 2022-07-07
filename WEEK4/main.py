# ##MAIN PACKAGE IMPORTS
import os
import sys
import pandas as pd
import csv
# ## FROM OTHER PACKAGE INPUT FUNCTIONS
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from DialogWindow import Ui_Dialog
from mainwindow import Ui_MainWindow

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
        with open(os.path.join(os.getcwd(), 'PARAMETERS.csv'), mode= 'w') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(['header1', 'header1'])
            index = ['index1', 'index2', 'index3']
            for row in range(1, self.tableWidget.rowCount()):
                rowlist=[]
                rowlist.append(index[row])
                for col in range(1, self.tableWidget.columnCount()):
                    rowlist.append(self.tableWidget.item(row, col))
                writer.writerow(rowlist)
        file.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Ui_Dialog()
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())