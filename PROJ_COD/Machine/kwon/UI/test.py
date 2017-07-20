# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import test_rcc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 412)
        MainWindow.setStyleSheet("background-image: url(:/new/prefix1/bg.png);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralWidget)
        self.toolButton.setMaximumSize(QtCore.QSize(100, 100))
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet("background-image: url(:/new/prefix1/open.png);\n"
"border-color: rgb(58, 58, 58);")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout.addWidget(self.toolButton)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 732, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.menuBar.setFont(font)
        self.menuBar.setStyleSheet("")
        self.menuBar.setObjectName("menuBar")
        self.menuFILE = QtWidgets.QMenu(self.menuBar)
        self.menuFILE.setObjectName("menuFILE")
        self.menuEDIT = QtWidgets.QMenu(self.menuBar)
        self.menuEDIT.setObjectName("menuEDIT")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOPEN = QtWidgets.QAction(MainWindow)
        self.actionOPEN.setObjectName("actionOPEN")
        self.menuFILE.addAction(self.actionOPEN)
        self.menuBar.addAction(self.menuFILE.menuAction())
        self.menuBar.addAction(self.menuEDIT.menuAction())
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFILE.setTitle(_translate("MainWindow", "FILE"))
        self.menuEDIT.setTitle(_translate("MainWindow", "EDIT"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOPEN.setText(_translate("MainWindow", "OPEN"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

