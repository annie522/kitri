import sys
from PyQt5 import QtWidgets

def select_file_window():
    myApp = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle('Add FileDialog')
    w.resize(300, 240)
    myButton1 = QtWidgets.QPushButton('Open Image', w)
    myButton1.move(20,80)
    filename = QtWidgets.QFileDialog.getOpenFileName(w, 'Open File', '/')
    print (filename[0])
    w.show()
    myApp.exec_()
    return filename[0]