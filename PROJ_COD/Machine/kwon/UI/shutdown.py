# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shutdown.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import folderopen, shutdown_rcc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 530)
        Form.setMinimumSize(QtCore.QSize(730, 530))
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setMouseTracking(False)
        Form.setStyleSheet("background-image: url(:/new/prefix1/bg.png);")
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(30, 210, 100, 100))
        self.toolButton_2.setMinimumSize(QtCore.QSize(100, 100))
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_2.setStyleSheet("image: url(:/new/prefix1/iconmonstr-virus-8.png);\n"
"border:0px;")
        self.toolButton_2.setText("")
        self.toolButton_2.setObjectName("toolButton_2")
        self.fileOPEN = QtWidgets.QToolButton(Form)
        self.fileOPEN.setGeometry(QtCore.QRect(30, 90, 100, 100))
        self.fileOPEN.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.fileOPEN.setFont(font)
        self.fileOPEN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileOPEN.setStyleSheet("image: url(:/new/prefix1/open.png);\n"
"border:0px;")
        self.fileOPEN.setText("")
        self.fileOPEN.setObjectName("fileOPEN")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(150, 70, 561, 441))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-image: url(:/new/prefix1/home.png);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.tabWidget.addTab(self.home, "")
        self.MD5 = QtWidgets.QWidget()
        palette = QtGui.QPalette()
        self.MD5.setPalette(palette)
        self.MD5.setStyleSheet("background-image: url(:/new/prefix1/tab.png);")
        self.MD5.setObjectName("MD5")
        self.tabWidget.addTab(self.MD5, "")
        self.VT = QtWidgets.QWidget()
        self.VT.setStyleSheet("background-image: url(:/new/prefix1/tab.png);")
        self.VT.setObjectName("VT")
        self.tabWidget.addTab(self.VT, "")
        self.MC = QtWidgets.QWidget()
        self.MC.setStyleSheet("background-image: url(:/new/prefix1/tab.png);")
        self.MC.setObjectName("MC")
        self.tabWidget.addTab(self.MC, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.fileOPEN.clicked.connect(self.clickBtn1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), _translate("Form", "HOME"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MD5), _translate("Form", "MD5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VT), _translate("Form", "VT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MC), _translate("Form", "MC"))

    def clickBtn1(self, Form):
        folderopen.clickBtn1()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

