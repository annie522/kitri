# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shutdown_test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 530)
        Form.setMinimumSize(QtCore.QSize(730, 530))
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setMouseTracking(False)
        Form.setStyleSheet("background-image: url(:/new/prefix1/bg.png);")
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(180, 90, 100, 100))
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

        self.retranslateUi(Form)
        self.fileOPEN.clicked.connect(Form.clickBtn1)
        self.toolButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

import shutdown_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

