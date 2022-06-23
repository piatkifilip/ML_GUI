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
        self.pushButton_5.clicked.connect(self.export(filepath=os.getcwd(),
                                                      filename='NAME1.csv',
                                                      header=self.tableWidget.getVerticalHeaderLabels(), index=))
        self.pushButton_5.clicked.connect(self.export(filepath=os.getcwd(),
                                                      filename='NAME2.csv',
                                                      header=self.tableWidget.verticalOffset(),
                                                      index=))

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

    def export(self, filepath=os.getcwd(), filename=None, header=None, index=None):
        # ##COMBINE THE FILE PATH AND FILE NAME AND OPEN IN WRITE MODE
        with open(os.path.join(filepath, filename), mode= 'w') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(header)
            for row in range(1, self.tableWidget.rowCount()):
                rowlist=[]
                # ##APPEND THE INDEX VALUE TO THE ROW
                rowlist.append(index[row])
                for col in range(1, self.tableWidget.columnCount()):
                    # ##APPEND COLUMN DATA TO ROW
                    rowlist.append(self.tableWidget.item(row, col))
            # ##WRITE ROW LIST TO CSV
            writer.writerow(rowlist)
            # ##CLOSE THE FILE
            file.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Ui_Dialog()
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())