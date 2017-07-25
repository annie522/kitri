import glob, sys, os
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap, QIcon, QGuiApplication
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QAbstractItemView, QLabel
from datetime import datetime
import time
import matplotlib.pyplot as plt
import PROJ_COD.FINAL.Get_File_Hash as getFileHash
import PROJ_COD.FINAL.Get_Machine_Percentage as fileMachine
import PROJ_COD.FINAL.Get_MongoDB_Connection as mongoDB
import PROJ_COD.FINAL.Get_VirusTotal as vt
import threading, requests, time




class Form(QtWidgets.QDialog):
    # GUI 기본 설정
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        # GUI 창 생성
        self.ui = uic.loadUi("main.ui", self)
        self.ui.setWindowTitle("EMDETECTOR")
        self.ui.setWindowIcon(QIcon(QPixmap("logo.png")))
        self.ui.show()
        # tab1 이미지 세팅
        self.ui.numberCountLabel.setPixmap(QPixmap("Proc01Not.jpg"))
        # tab1, tab4 비활성화
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(4, False)
        # tab3 테이블 데이터 보여주기
        Form.selectLog(self)

        self.ui.loadingImg.hide()


    # 로딩 애니메이션
    def loadingAnimation(self):
        for tt in range(1,2):
            for i in range(1, 13):
                self.ui.loadingImg.setPixmap(QPixmap("Animation\\image"+str(i)+".png"))
                time.sleep(0.2)
                self.ui.loadingImg.repaint()


    ## 클릭 기능부분 ####################################################################
    # tab0 파일선택버튼 클릭
    @pyqtSlot()
    def fileopenBtnClick(self):
        global fname
        fname = ""

        fname = QFileDialog.getOpenFileName(self, 'Open file', "/")
        fname = os.path.abspath(fname[0])
        self.ui.selected_file.setText(fname)
        fname = self.ui.selected_file.text()
        if fname[-3:] != "exe" or fname == "":
            self.ui.selected_file.setText("선택 파일 없음")
            self.ui.tab0ProcessLabel.setText("파일을 다시 선택하세요")
            fname = ""
        else:
            self.ui.tab0ProcessLabel.setText("검사시작 버튼을 클릭하세요")

    # tab0 검사시작버튼 클릭
    @pyqtSlot()
    def startFileDetectionBtnClick(self):
        QGuiApplication.setOverrideCursor(Qt.WaitCursor)
        self.ui.loadingImg.show()
        Form.loadingAnimation(self)
        print(fname)
        # tab1에 내용 세팅
        todayTime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        self.ui.page2_dateLabel.setText(todayTime)
        fileBaseName = os.path.basename(fname)
        self.ui.page2_filenameLabel.setText(fileBaseName)
        fileDirName = os.path.dirname(fname)
        self.ui.page2_filepathLabel.setText(fileDirName)
        fileHash = getFileHash.getFileHash(fname)
        self.ui.page2_md5Label.setText(fileHash)


        # 입력받은 파일의 해시값을 데이터베이스와 비교
        self.ui.numberCountLabel.setPixmap(QPixmap("Proc02Hash.jpg"))
        md5Check = getFileHash.checkHashInDB(fname)
        if md5Check[0] == "YES":
            if md5Check[1] == "M":
                self.ui.MD5HashLabel.setText("악성파일")
                self.ui.page2_similarLabel.setText("악성파일")
            elif md5Check[1] == "N":
                self.ui.MD5HashLabel.setText("정상파일")
                self.ui.page2_similarLabel.setText("정상파일")
        elif md5Check[0] == "NO":
            self.ui.numberCountLabel.setPixmap(QPixmap("Proc03VTotal.jpg"))
            self.ui.MD5HashLabel.setText("해시값 미등록 파일")
            # 바이러스 토탈 돌리기
            dic = vt.get_mal_kind(fname)
            try:
                if dic[0] > 4:
                    self.ui.VTResultLabel.setText(dic[0]+"밴더 탐지")
                    self.ui.numberCountLabel.setPixmap(QPixmap("Proc04Machine.jpg"))
                    # 머신러닝
                    machineRslt = fileMachine.getFIleMachine(fname)
                    if machineRslt == "NORMAL":
                        self.ui.page2_similarLabel.setText("정상파일")
                        self.ui.machineResultLabel.setText("정상파일")
                    else:
                        self.ui.page2_similarLabel.setText("악성파일")
                        self.ui.machineResultLabel.setText("악성파일")
                else:
                    self.ui.VTResultLabel.setText("정상파일")
                    self.ui.page2_similarLabel.setText("정상파일")
            except:
                self.ui.VTResultLabel.setText("ERROR")
                self.ui.page2_similarLabel.setText("ERROR")
        else:
            self.ui.VTResultLabel.setText("ERROR")
            self.ui.page2_similarLabel.setText("ERROR")


        # 파일삭제버튼 활성화/비활성화
        if self.ui.page2_similarLabel.text() == "악성파일":
            self.ui.delFileBtn.setEnabled(True)
            self.ui.delFileBtn.setStyleSheet("background-color: #0F75BD;color: white;border:nono;")
        else:
            self.ui.delFileBtn.setEnabled(False)
            self.ui.delFileBtn.setStyleSheet("background-color:lightgray;color: white;border:nono;")


        # 검사시작 버튼 클릭시 tab3에 보여줄 로그 데이터베이스에 INSERT
        logDB = mongoDB.DBConn("shutdown").log
        if logDB.count() == 10:
            logDB.remove()
        insertLogData = {}
        insertLogData.update({"date": todayTime, "hash":getFileHash.getFileHash(fname) ,"filename": fname, "result": "normal", "state": "finished"})
        logDB.insert(insertLogData)
        Form.selectLog(self)

        self.tabWidget.setTabEnabled(1, True)
        self.tabWidget.setCurrentIndex(1)

        self.ui.loadingImg.hide()
        self.ui.loadingImg.repaint()
        QGuiApplication.restoreOverrideCursor()



    @pyqtSlot()
    def delBtnClick(self):
        filePath = self.ui.page2_filepathLabel.text() + self.ui.page2_filenameLabel.text()
        os.remove(filePath)
        # 버튼 비활성화
        self.ui.delFileBtn.setEnabled(True)
        self.ui.delFileBtn.setStyleSheet("background-color: #0F75BD;color: white;border:nono;")
        # 로그디비에 삭제기록 업데이트
        fileHash = getFileHash.getFileHash(filePath)
        logDB = mongoDB.DBConn("shutdown").log
        logDB.update({"hash":fileHash},{"state":"REMOVED"})


    @pyqtSlot()
    def selectLog(self):
        # 검사기록 로그를 불러옴
        logDB = mongoDB.DBConn("shutdown").log
        logDBCount = logDB.count()
        self.ui.logTable.setRowCount(logDBCount)
        logData = logDB.find({},{"hash":0})
        # 불러온 기록 테이블에 보여주기
        num = 0
        j = 0
        for item in logData:
            item = str(item).split(",")
            item[1] = item[1].replace("'date': '", "").replace("'", "")
            item[2] = item[2].replace("'filename': '", "").replace("'", "").replace("\\\\", "\\")
            item[3] = item[3].replace("'result': '", "").replace("'", "")
            item[4] = item[4].replace("'state': '", "").replace("'}", "")
            showData = []
            showData.append(item[1])
            showData.append(item[2])
            showData.append(item[3])
            showData.append(item[4])
            for i in range(0, 4):
                self.ui.logTable.setItem(j, i, QTableWidgetItem(showData[i]))
                self.ui.logTable.item(j, i).setTextAlignment(Qt.AlignCenter)
            j += 1
        # 테이블 CSS 설정
        self.ui.logTable.horizontalHeader().setStretchLastSection(True)
        self.ui.logTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.logTable.setColumnWidth(0, 150)
        self.ui.logTable.setColumnWidth(1, 300)
        self.ui.logTable.setSelectionBehavior(1)


    @pyqtSlot()
    def saveLogBtnClick(self):
        # 로그 기록 텍스트 파일로 저장
        logDB = mongoDB.DBConn("shutdown").log
        logData = logDB.find({}, {'_id': 0})
        logDBCount = logDB.count()
        for item in logData:
            inputData = str(item).replace("{", "").replace("}", "")
            f = open("log.txt", 'w')
            for i in range(1, logDBCount + 1):
                data = "NUMBER{} --> {}\n".format(i, inputData)
                f.write(data)
            f.close()

    @pyqtSlot()
    def delLogBtnClick(self):
        # 로그 전체기록 삭제하기
        logDB = mongoDB.DBConn("shutdown").log
        logDB.remove()
        Form.selectLog(self)
        self.ui.logTable.repaint()

    @pyqtSlot()
    def delFileBtnClick(self):
        # 로그 테이블에서 기록 선택 후 파일 삭제
        try:
            selectedRow = self.ui.logTable.currentRow()
            filePath = self.ui.logTable.item(selectedRow, 1).text()
            filePath = str(filePath).strip()
            # 로그디비에 삭제
            logDB = mongoDB.DBConn("shutdown").log
            logDB.remove({"filename": filePath})
            os.remove(filePath)
        except:
            pass
        Form.selectLog(self)
        self.ui.logTable.repaint()




    @pyqtSlot()
    def folderopenBtnClick(self):
        global dname
        dname = ""

        dname = QFileDialog.getExistingDirectory(self, 'Open Folder', '\\')
        dname = os.path.abspath(dname)
        self.ui.selected_folder.setText(dname)
        totalNum = len(glob.glob(dname + "/*.exe"))
        self.ui.numTotal.setText(str(totalNum))




    @pyqtSlot()
    def startFolderDetectionBtnClick(self):
        QGuiApplication.setOverrideCursor(Qt.WaitCursor)
        count1 = int(self.ui.numNormal.text()) + int(self.ui.numMalware.text())
        count2 = int(self.ui.numTotal.text())
        if count1 != count2:
            self.ui.tab4ProcessLabel.setText("숫자를 다시 입력하세요")
        else:
            self.ui.loadingImg.show()
            Form.loadingAnimation(self)

            self.ui.inputNormal.setText(self.ui.numNormal.text())
            self.ui.inputMalware.setText(self.ui.numMalware.text())

            flist = glob.glob(dname + "/*.exe")
            normalCount = 0
            malwareCount = 0
            # 바이러스 토탈 돌리기
            for fname in flist:
                dic = vt.get_mal_kind(fname)
                if dic[0] > 4:
                    machineRslt = fileMachine.getFIleMachine(fname)
                    if machineRslt == "NORMAL":
                        normalCount += 1
                    else:
                        malwareCount += 1
                else:
                    normalCount += 1

            self.ui.detectedNormal.setText(str(normalCount))
            self.ui.detectedMalware.setText(str(malwareCount))

            a = int(self.ui.inputNormal.text())
            b = int(self.ui.detectedNormal.text())
            c = int(self.ui.detectedMalware.text())
            d = int(self.ui.inputMalware.text())
            # # 오탐율 계산
            # try:
            #     detectionResult = (abs(a - b) / b) * 100
            # except:
            #     detectionResult = (abs(d - c) / c) * 100
            # 탐지율 계산
            try:
                detectionResult = 100.0-((abs(a - b) / b) * 100)
            except:
                detectionResult = 100.0-((abs(d - c) / c) * 100)
            self.ui.detectionResultLabel.setText(str(detectionResult) + "%")

            ## 결과값 그래프로 보여주기
            colors = ["pink", "skyblue"]
            title = "DETECTION RESULT"
            plt.title(title, fontsize=25)
            label = ["NORMAL", "MALWARE"]
            fracs = [b, c]
            plt.pie(fracs, labels=label, startangle=90, autopct='%1.1f%%', explode=(0, 0.1), colors=colors)

            chartImage = plt.gcf()
            chartImage.savefig("chartImage.jpg")
            self.ui.resultGraph.setPixmap(QPixmap("chartImage.jpg"))
            self.ui.resultGraph.setScaledContents(True)

            self.tabWidget.setTabEnabled(4, True)
            self.tabWidget.setCurrentIndex(4)

            self.ui.loadingImg.hide()
            self.ui.loadingImg.repaint()

            QGuiApplication.restoreOverrideCursor()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())