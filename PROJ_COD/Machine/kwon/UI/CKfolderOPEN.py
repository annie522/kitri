import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from test import *


class XWindow(MainWindow, QtGui, MainWindow.Ui_MainWindow):
	def __init__(self):
		MainWindow.__init__(self)
		self.setupUi(self)

		self.initData()

		self.













		QtGui.QtWidgets.__init__(self,parent)
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		
	def slot1folderOPEN(self):
		self.QFileDialog.getOpenFileName(self, 'Open File', 'c:/')
		return

app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()

app.exec_()