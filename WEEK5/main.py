# ##MAIN PACKAGE IMPORTS
import os
import sys
import pandas as pd
import csv
# ## FROM OTHER PACKAGE INPUT FUNCTIONS
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem,QToolBar,QStatusBar,QAction
from PyQt5.QtCore import QSize, Qt
from DialogWindow1 import Ui_Dialog
from DialogWindow2 import Ui_Dialog2
from MainWindow import Ui_MainWindow

class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, text, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

# Connect Buttons to Relevant Functions for Mainwindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.SpecGeoButton.clicked.connect(self.openWindow)
        self.ParameterButton.clicked.connect(self.openWindow2)
        self.FinishButton.clicked.connect(self.createDFParam)
        self.FinishButton.clicked.connect(self.createDF)
        self.ClearButton.clicked.connect(self.clear)

    # Function used to pass data from DialogWindow1 to ValueTable
    def passdata(self):
        val1 = self.ValTable.item(0,0)
        val2 = self.ValTable.item(1,0)
        val3 = self.ValTable.item(2,0)
        val4 = self.ValTable.item(3,0)
        val5 = self.ValTable.item(4,0)

        val1.setText(str(self.ui.GaugeLenbox.value()))
        val2.setText(str(self.ui.GaugeDbox.value()))
        val3.setText(str(self.ui.Heightbox.value()))
        val4.setText(str(self.ui.ConnectorDbox.value()))
        val5.setText(str(self.ui.NumElbox.value()))

        self.window.hide()

    # Function used to pass data from DialogWindow2 to ParameterTable
    def passdataParam(self):

        P1valmin = self.ParamTable.item(0,0)
        P2valmin = self.ParamTable.item(1, 0)
        P3valmin = self.ParamTable.item(2, 0)
        P4valmin = self.ParamTable.item(3, 0)
        P5valmin = self.ParamTable.item(4, 0)
        P6valmin = self.ParamTable.item(5, 0)
        P7valmin = self.ParamTable.item(6, 0)
        P8valmin = self.ParamTable.item(7, 0)

        P1valmin.setText(str(self.ui2.P1box.value()))
        P2valmin.setText(str(self.ui2.P2box.value()))
        P3valmin.setText(str(self.ui2.P3box.value()))
        P4valmin.setText(str(self.ui2.P4box.value()))
        P5valmin.setText(str(self.ui2.P5box.value()))
        P6valmin.setText(str(self.ui2.P6box.value()))
        P7valmin.setText(str(self.ui2.P7box.value()))
        P8valmin.setText(str(self.ui2.P8box.value()))

        P1valmax = self.ParamTable.item(0, 1)
        P2valmax = self.ParamTable.item(1, 1)
        P3valmax = self.ParamTable.item(2, 1)
        P4valmax = self.ParamTable.item(3, 1)
        P5valmax = self.ParamTable.item(4, 1)
        P6valmax = self.ParamTable.item(5, 1)
        P7valmax = self.ParamTable.item(6, 1)
        P8valmax = self.ParamTable.item(7, 1)

        P1valmax.setText(str(self.ui2.P1box.value()))
        P2valmax.setText(str(self.ui2.P2box.value()))
        P3valmax.setText(str(self.ui2.P3box.value()))
        P4valmax.setText(str(self.ui2.P4box.value()))
        P5valmax.setText(str(self.ui2.P5box.value()))
        P6valmax.setText(str(self.ui2.P6box.value()))
        P7valmax.setText(str(self.ui2.P7box.value()))
        P8valmax.setText(str(self.ui2.P8box.value()))

    # Function used to open DialogWindow1
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.OkButton.clicked.connect(self.passdata)
        self.window.show()

    # Function used to open DialogWindow2
    def openWindow2(self):
        self.window2 = QtWidgets.QDialog()
        self.ui2 = Ui_Dialog2()
        self.ui2.setupUi(self.window2)
        self.ui2.OkButton.clicked.connect(self.passdataParam)
        self.window2.show()

    # Create Dataframe from Parameter Table
    def createDFParam(self):
        col_count = self.ParamTable.columnCount()
        row_count = self.ParamTable.rowCount()
        headers = [str(self.ParamTable.horizontalHeaderItem(i).text()) for i in range(col_count)]
        df_list = []
        for row in range(row_count):
            df_list2 = []
            for col in range(col_count):
                table_item = self.ParamTable.item(row, col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            df_list.append(df_list2)

        df = pd.DataFrame(df_list, columns=headers)
        df.to_csv(r'C:\Users\piatk\PycharmProjects\ML_GUI\WEEK5\PARAMETERS.csv', index=True, header=True)

        return df

    # Create Dataframe from Value Table
    def createDF(self):
        col_count = self.ValTable.columnCount()
        row_count = self.ValTable.rowCount()
        headers = [str(self.ValTable.horizontalHeaderItem(i).text()) for i in range(col_count)]
        df_list = []
        for row in range(row_count):
            df_list2 = []
            for col in range(col_count):
                table_item = self.ValTable.item(row, col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            df_list.append(df_list2)

        df = pd.DataFrame(df_list, columns=headers)
        df.to_csv(r'C:\Users\piatk\PycharmProjects\ML_GUI\WEEK5\VALUES.csv', index=True, header=True)

        return df

    # Function usd to Clear data from tables
    def clear(self):
        self.ValTable.clearContents()
        self.ParamTable.clearContents()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Ui_Dialog()
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())