import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *

def clickBtn1():
    # ------------------------------------------
    # -- Create window
    # ------------------------------------------
    myApp = QtWidgets.QApplication(sys.argv)                   # Create an PyQT4 application object.
    w = QtWidgets.QWidget()                                # Add menubar, need to use QMainWindow().
    w.setWindowTitle('Add FileDialog')
    w.resize(300, 240)

    # ------------------------------------------
    # -- Create a button in the window
    # ------------------------------------------
    myButton1 = QtWidgets.QPushButton('Open Image', w)
    myButton1.move(20,80)

    # ------------------------------------------
    # -- Create file dialog
    # ------------------------------------------
    filename = QtWidgets.QFileDialog.getOpenFileName(w, 'Open File', '/')
    print (filename)

    # print file contents
    with open(filename, 'r') as f:
        print(f.read())


    # ------------------------------------------
    # -- Show the window and run the app
    # ------------------------------------------
    w.show()
    myApp.exec_()
ㅇㅇㅇㅇㅇ