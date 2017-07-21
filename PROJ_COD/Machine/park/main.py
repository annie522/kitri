# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yjyj.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import fileopen

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 530)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 139, 711, 381))
        self.tabWidget.setMinimumSize(QtCore.QSize(711, 361))
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setStyleSheet("")
        self.tab1.setObjectName("tab1")
        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(80, 80, 460, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("border: 1px solid rgb(58, 58, 58);\n"
"border-top-left-radius:5px;\n"
"border-bottom-left-radius: 5px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.fileOPEN = QtWidgets.QToolButton(self.tab1)
        self.fileOPEN.setGeometry(QtCore.QRect(540, 80, 90, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.fileOPEN.setFont(font)
        self.fileOPEN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileOPEN.setStyleSheet("border: 1px solid rgb(58, 58, 58);\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius: 5px;\n"
"background-color: rgb(223, 223, 223);")
        self.fileOPEN.setObjectName("fileOPEN")
        self.toolButton = QtWidgets.QToolButton(self.tab1)
        self.toolButton.setGeometry(QtCore.QRect(280, 220, 150, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton.setFont(font)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet("background-color: rgb(25, 59, 255);\n"
"color: rgb(223, 223, 223);")
        self.toolButton.setObjectName("toolButton")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tab2.setPalette(palette)
        self.tab2.setStyleSheet("")
        self.tab2.setObjectName("tab2")
        self.toolButton_2 = QtWidgets.QToolButton(self.tab2)
        self.toolButton_2.setGeometry(QtCore.QRect(300, 290, 100, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_2.setStyleSheet("background-color: rgb(25, 59, 255);\n"
"color: rgb(223, 223, 223);")
        self.toolButton_2.setObjectName("toolButton_2")
        self.listView = QtWidgets.QListView(self.tab2)
        self.listView.setGeometry(QtCore.QRect(10, 10, 681, 121))
        self.listView.setObjectName("listView")
        self.label_3 = QtWidgets.QLabel(self.tab2)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 61, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 61, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.tab2)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 61, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab2)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 61, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab2)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.graph = QtWidgets.QWidget(self.tab2)
        self.graph.setGeometry(QtCore.QRect(10, 140, 681, 141))
        self.graph.setObjectName("graph")
        self.label_9 = QtWidgets.QLabel(self.tab2)
        self.label_9.setGeometry(QtCore.QRect(90, 20, 361, 16))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_19 = QtWidgets.QLabel(self.tab2)
        self.label_19.setGeometry(QtCore.QRect(90, 40, 361, 16))
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab2)
        self.label_20.setGeometry(QtCore.QRect(90, 60, 361, 16))
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab2)
        self.label_21.setGeometry(QtCore.QRect(90, 80, 361, 16))
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab2)
        self.label_22.setGeometry(QtCore.QRect(90, 100, 361, 16))
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setStyleSheet("")
        self.tab3.setObjectName("tab3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab3)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 701, 251))
        self.tableWidget.setStyleSheet("border : 0px;")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.toolButton_4 = QtWidgets.QToolButton(self.tab3)
        self.toolButton_4.setGeometry(QtCore.QRect(180, 290, 100, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_4.setStyleSheet("background-color: rgb(25, 59, 255);\n"
"color: rgb(223, 223, 223);")
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.tab3)
        self.toolButton_5.setGeometry(QtCore.QRect(290, 290, 131, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_5.setFont(font)
        self.toolButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_5.setStyleSheet("background-color: rgb(25, 59, 255);\n"
"color: rgb(223, 223, 223);")
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.tab3)
        self.toolButton_6.setGeometry(QtCore.QRect(430, 290, 100, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_6.setFont(font)
        self.toolButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_6.setStyleSheet("background-color: rgb(25, 59, 255);\n"
"color: rgb(223, 223, 223);")
        self.toolButton_6.setObjectName("toolButton_6")
        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setStyleSheet("")
        self.tab4.setObjectName("tab4")
        self.folderOPEN = QtWidgets.QToolButton(self.tab4)
        self.folderOPEN.setGeometry(QtCore.QRect(540, 40, 90, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.folderOPEN.setFont(font)
        self.folderOPEN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.folderOPEN.setStyleSheet("border: 1px solid rgb(58, 58, 58);\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius: 5px;\n"
"background-color: rgb(223, 223, 223);")
        self.folderOPEN.setObjectName("folderOPEN")
        self.label_10 = QtWidgets.QLabel(self.tab4)
        self.label_10.setGeometry(QtCore.QRect(80, 40, 460, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("border: 1px solid rgb(58, 58, 58);\n"
"border-top-left-radius:5px;\n"
"border-bottom-left-radius: 5px;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab4)
        self.label_11.setGeometry(QtCore.QRect(250, 100, 61, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab4)
        self.label_12.setGeometry(QtCore.QRect(250, 130, 61, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit = QtWidgets.QLineEdit(self.tab4)
        self.lineEdit.setGeometry(QtCore.QRect(320, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab4)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 130, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.tab4)
        self.toolButton_3.setGeometry(QtCore.QRect(280, 220, 150, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_3.setStyleSheet("background-color: rgb(25, 59, 255);\n"
"color: rgb(223, 223, 223);")
        self.toolButton_3.setObjectName("toolButton_3")
        self.tabWidget.addTab(self.tab4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.graph2 = QtWidgets.QWidget(self.tab)
        self.graph2.setGeometry(QtCore.QRect(10, 20, 351, 311))
        self.graph2.setObjectName("graph2")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(370, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(25, 59, 255);\n"
"color: rgb(223, 223, 223);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(390, 110, 61, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(390, 80, 61, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(470, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(580, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(460, 80, 91, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(570, 80, 91, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(570, 110, 91, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(460, 110, 91, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(430, 220, 61, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(25, 59, 255);\n"
"color: rgb(223, 223, 223);\n"
"border-top-left-radius:5px;\n"
"border-bottom-left-radius: 5px;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(490, 220, 141, 51))
        self.lineEdit_7.setStyleSheet("border: 1px solid rgb(58, 58, 58);\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius: 5px;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.tabWidget.addTab(self.tab, "")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 711, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 고딕 Std B")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 75 30pt \"Adobe 고딕 Std B\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(160, 70, 421, 61))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.fileOPEN.clicked.connect(self.clickBtn1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "선택 파일 없음"))
        self.fileOPEN.setText(_translate("Form", "파일 선택"))
        self.toolButton.setText(_translate("Form", "검사시작 !"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Form", "파일선택"))
        self.toolButton_2.setText(_translate("Form", "파일 삭제"))
        self.label_3.setText(_translate("Form", "파일 이름 :"))
        self.label_4.setText(_translate("Form", "파일 경로 :"))
        self.label_6.setText(_translate("Form", "분석 날짜 :"))
        self.label_7.setText(_translate("Form", "MD5       :"))
        self.label_8.setText(_translate("Form", "유사도     :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Form", "탐지결과"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "날짜"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "파일경로"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "상태"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "분석결과"))
        self.toolButton_4.setText(_translate("Form", "로그 삭제"))
        self.toolButton_5.setText(_translate("Form", "선택파일 삭제"))
        self.toolButton_6.setText(_translate("Form", "로그 저장"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("Form", "진단로그"))
        self.folderOPEN.setText(_translate("Form", "폴더 선택"))
        self.label_10.setText(_translate("Form", "선택 폴더 없음"))
        self.label_11.setText(_translate("Form", "정상 파일 :"))
        self.label_12.setText(_translate("Form", "악성 파일 :"))
        self.toolButton_3.setText(_translate("Form", "검사시작 !"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), _translate("Form", "탐지통계"))
        self.label_13.setText(_translate("Form", "탐지 확률 검사"))
        self.label_14.setText(_translate("Form", "악성 파일"))
        self.label_15.setText(_translate("Form", "정상 파일"))
        self.label_16.setText(_translate("Form", "입력 된 파일"))
        self.label_17.setText(_translate("Form", "탐지 된 파일"))
        self.label_18.setText(_translate("Form", "오탐율"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "통계확인"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>MalwareMachine<span style=\" color:#193bff;\">Detector</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\"><div style=\'line-height:50%;\'>Malware Machine Detector는 의심스러운 파일을 분석하고</span></p><p align=\"center\"><span style=\" font-size:10pt;\">악성코드를 머신러닝기반으로 탐지할수있는 서비스 입니다</span></div></p></body></html>"))

    def clickBtn1(self, Form):
        fileopen.clickBtn1()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

