# ##MAIN PACKAGE IMPORTS
import math
import os
import sys
import pandas as pd
import numpy as np
import csv
# ## FROM OTHER PACKAGE INPUT FUNCTIONS
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel,QApplication, QMainWindow, QGridLayout, QWidget,\
    QTableWidget, QTableWidgetItem,QToolBar,QStatusBar,QAction,QMenuBar,QVBoxLayout
from PyQt5.QtCore import QSize, pyqtSignal, QObject
from DialogWindow1 import Ui_Dialog
from DialogWindow2 import Ui_Dialog2
from MainWindow import Ui_MainWindow
from run import Ui_Dialog3
from viewer import QImageViewer

# Connect Buttons to Relevant Functions for Mainwindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    @QtCore.pyqtSlot(float, float, float, float, int)
    def save(self, Val1, Val2, Val3, Val4, Val5):
        MainWindow.val1 = Val1
        MainWindow.val2 = Val2
        MainWindow.val3 = Val3
        MainWindow.val4 = Val4
        MainWindow.val5 = Val5

    @QtCore.pyqtSlot(float, float, float, float, float, float, float, float,
                     float, float, float, float, float, float, float, float)
    def parSave(self, par1, par2, par3, par4, par5, par6, par7, par8,
                par1m, par2m, par3m, par4m, par5m, par6m, par7m, par8m):
        MainWindow.P1 = par1
        MainWindow.P2 = par2
        MainWindow.P3 = par3
        MainWindow.P4 = par4
        MainWindow.P5 = par5
        MainWindow.P6 = par6
        MainWindow.P7 = par7
        MainWindow.P8 = par8

        MainWindow.P1m = par1m
        MainWindow.P2m = par2m
        MainWindow.P3m = par3m
        MainWindow.P4m = par4m
        MainWindow.P5m = par5m
        MainWindow.P6m = par6m
        MainWindow.P7m = par7m
        MainWindow.P8m = par8m

    def __init__(self):
        QMainWindow.__init__(self)

        self.setupUi(self)
        self.SpecGeoButton.clicked.connect(self.openWindow)
        self.ParameterButton.clicked.connect(self.openWindow2)
        self.FinishButton.clicked.connect(self.createDFParam)
        self.FinishButton.clicked.connect(self.createDF)
        self.ClearButton.clicked.connect(self.clear)
        self.RunButton.clicked.connect(self.openWindow3)
        self.ResultsButton.clicked.connect(self.openWindow4)

    # Function used to open DialogWindow1
    def openWindow(self):
        self.runValWindow = Dialog()
        self.runValWindow.submit.connect(self.updateVal)
        self.runValWindow.submitDiameter.connect(self.updateDiam)
        self.runValWindow.submitInt.connect(self.save)
        self.runValWindow.show()
        self.values.emit(self.ValTable.item(0,0))

    # Function used to open DialogWindow2
    def openWindow2(self):
        self.runParamWindow = Dialog2()
        self.runParamWindow.submitInt.connect(self.parSave)
        self.runParamWindow.submit.connect(self.updatePar)
        self.runParamWindow.show()

    # Function used to open DialogWindow3
    def openWindow3(self):
       self.runWindow = run(self.hiddenValueMain.value())
       self.runWindow.show()

    # Function used to open run Window - calculate CSA
    def openWindow4(self):
        self.window4 = QImageViewer()
        self.window4.show()

    # Create Dataframe from Parameter Table
    def createDFParam(self):
        col_count = self.ParamTable.columnCount()
        row_count = self.ParamTable.rowCount()
        index = ['P1','P2','P3','P4','P5','P6','P7','P8']
        headers = [str(self.ParamTable.horizontalHeaderItem(i).text()) for i in range(col_count)]
        df_list = []
        for row in range(row_count):
            df_list2 = []
            for col in range(col_count):
                table_item = self.ParamTable.item(row, col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            df_list.append(df_list2)

        df = pd.DataFrame(df_list, columns=headers,index=index)
        df.to_csv(r'C:\Users\piatk\PycharmProjects\ML_GUI\WEEK5\PARAMETERS.csv', index=True, header=True)

        return df

    # Create Dataframe from Value Table
    def createDF(self):
        col_count = self.ValTable.columnCount()
        row_count = self.ValTable.rowCount()
        headers = [str(self.ValTable.horizontalHeaderItem(i).text()) for i in range(col_count)]
        index = ['Gauge Diameter', 'Gauge Length', 'Specimen Height', 'Connector Diameter', 'Number of Elements']
        df_list = []
        for row in range(row_count):
            df_list2 = []
            for col in range(col_count):
                table_item = self.ValTable.item(row, col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            df_list.append(df_list2)
        df = pd.DataFrame(df_list, columns=headers, index=index)
        df.to_csv(r'C:\Users\piatk\PycharmProjects\ML_GUI\WEEK5\VALUES.csv', index=index, header=True)

        return df

    # Function usd to Clear data from tables
    def clear(self):
        self.ValTable.setItem(0, 0, QtWidgets.QTableWidgetItem("0.0"))
        self.ValTable.setItem(1, 0, QtWidgets.QTableWidgetItem("0.0"))
        self.ValTable.setItem(2, 0, QtWidgets.QTableWidgetItem("0.0"))
        self.ValTable.setItem(3, 0, QtWidgets.QTableWidgetItem("0.0"))
        self.ValTable.setItem(4, 0, QtWidgets.QTableWidgetItem("0"))

        self.ParamTable.setItem(0, 0, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(1, 0, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(2, 0, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(3, 0, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(4, 0, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(5, 0, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(6, 0, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(7, 0, QtWidgets.QTableWidgetItem("0.0"))

        self.ParamTable.setItem(0, 1, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(1, 1, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(2, 1, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(3, 1, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(4, 1, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(5, 1, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(6, 1, QtWidgets.QTableWidgetItem("0.0"))
        self.ParamTable.setItem(7, 1, QtWidgets.QTableWidgetItem("0.0"))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    @QtCore.pyqtSlot(str, str, str, str, str)
    def updateVal(self, int1, int2, int3, int4 ,int5):
        self.int1= int1
        self.int2 = int2
        self.int3 = int3
        self.int4 = int4
        self.int5 = int5

        self.ValTable.item(0,0).setText(int1)
        self.ValTable.item(1,0).setText(int2)
        self.ValTable.item(2,0).setText(int3)
        self.ValTable.item(3,0).setText(int4)
        self.ValTable.item(4,0).setText(int5)

    @QtCore.pyqtSlot(str, str, str, str, str, str, str, str,
                     str, str, str, str, str, str, str, str)
    def updatePar(self, par1, par2, par3, par4, par5, par6, par7, par8,
                  par1m, par2m, par3m, par4m, par5m, par6m, par7m, par8m):
        self.ParamTable.item(0,0).setText(par1)
        self.ParamTable.item(1,0).setText(par2)
        self.ParamTable.item(2,0).setText(par3)
        self.ParamTable.item(3,0).setText(par4)
        self.ParamTable.item(4,0).setText(par5)
        self.ParamTable.item(5,0).setText(par6)
        self.ParamTable.item(6,0).setText(par7)
        self.ParamTable.item(7,0).setText(par8)

        self.ParamTable.item(0, 1).setText(par1m)
        self.ParamTable.item(1, 1).setText(par2m)
        self.ParamTable.item(2, 1).setText(par3m)
        self.ParamTable.item(3, 1).setText(par4m)
        self.ParamTable.item(4, 1).setText(par5m)
        self.ParamTable.item(5, 1).setText(par6m)
        self.ParamTable.item(6, 1).setText(par7m)
        self.ParamTable.item(7, 1).setText(par8m)

    @QtCore.pyqtSlot(float)
    def updateDiam(self, int1):
        self.int1 = int1
        self.hiddenValueMain.setValue(int(int1))


    values = QtCore.pyqtSignal(int)
    val1 = 0.0
    val2 = 0.0
    val3 = 0.0
    val4 = 0.0
    val5 = 0

    P1 = 0.0
    P2 = 0.0
    P3 = 0.0
    P4 = 0.0
    P5 = 0.0
    P6 = 0.0
    P7 = 0.0
    P8 = 0.0

    P1m = 0.0
    P2m = 0.0
    P3m = 0.0
    P4m = 0.0
    P5m = 0.0
    P6m = 0.0
    P7m = 0.0
    P8m = 0.0

class Dialog(QtWidgets.QDialog, Ui_Dialog):

    submit = QtCore.pyqtSignal(str, str, str, str, str)
    submitDiameter = QtCore.pyqtSignal(float)
    submitInt = QtCore.pyqtSignal(float, float, float, float, int)

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.OkButton.clicked.connect(self.saveDiam)
        self.OkButton.clicked.connect(self.onSubmit)

        self.GaugeLenbox.setValue(MainWindow.val1)
        self.Heightbox.setValue(MainWindow.val2)
        self.GaugeDbox.setValue(MainWindow.val3)
        self.ConnectorDbox.setValue(MainWindow.val4)
        self.NumElbox.setValue(MainWindow.val5)


    def saveDiam(self):
        self.submitDiameter.emit(self.GaugeDbox.value())

    def onSubmit(self):
        self.submit.emit(str(self.GaugeLenbox.value()), str(self.Heightbox.value()), str(self.GaugeDbox.value()),
                str(self.ConnectorDbox.value()), str(self.NumElbox.value()))

        self.submitInt.emit(self.GaugeLenbox.value(), self.Heightbox.value(), self.GaugeDbox.value(),
                            self.ConnectorDbox.value(), self.NumElbox.value())

class Dialog2(QtWidgets.QDialog, Ui_Dialog2):
    submit = QtCore.pyqtSignal(str, str, str, str, str, str, str, str,
                               str, str, str, str, str, str, str, str)
    submitInt = QtCore.pyqtSignal(float, float, float, float, float, float, float, float,
                                  float, float, float, float, float, float, float, float)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.OkButton.clicked.connect(self.onSubmit)
        self.P1box.setValue(MainWindow.P1)
        self.P2box.setValue(MainWindow.P2)
        self.P3box.setValue(MainWindow.P3)
        self.P4box.setValue(MainWindow.P4)
        self.P5box.setValue(MainWindow.P5)
        self.P6box.setValue(MainWindow.P6)
        self.P7box.setValue(MainWindow.P7)
        self.P8box.setValue(MainWindow.P8)

        self.P1boxMax.setValue(MainWindow.P1m)
        self.P2boxMax.setValue(MainWindow.P2m)
        self.P3boxMax.setValue(MainWindow.P3m)
        self.P4boxMax.setValue(MainWindow.P4m)
        self.P5boxMax.setValue(MainWindow.P5m)
        self.P6boxMax.setValue(MainWindow.P6m)
        self.P7boxMax.setValue(MainWindow.P7m)
        self.P8boxMax.setValue(MainWindow.P8m)

    def onSubmit(self):
        self.submit.emit(str(self.P1box.value()), str(self.P2box.value()), str(self.P3box.value()), str(self.P4box.value()),
                         str(self.P5box.value()), str(self.P6box.value()), str(self.P7box.value()), str(self.P8box.value()),
                         str(self.P1boxMax.value()), str(self.P2boxMax.value()), str(self.P3boxMax.value()),str(self.P4boxMax.value()),
                         str(self.P5boxMax.value()), str(self.P6boxMax.value()), str(self.P7boxMax.value()),str(self.P8boxMax.value()))

        self.submitInt.emit(self.P1box.value(), self.P2box.value(), self.P3box.value(), self.P4box.value(),
                            self.P5box.value(), self.P6box.value(), self.P7box.value(), self.P8box.value(),
                            self.P1boxMax.value(), self.P2boxMax.value(), self.P3boxMax.value(), self.P4boxMax.value(),
                            self.P5boxMax.value(), self.P6boxMax.value(), self.P7boxMax.value(), self.P8boxMax.value()
                            )


class run(QtWidgets.QDialog, Ui_Dialog3):
    def __init__(self, diameter, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.hiddenLabel.setValue(diameter)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())