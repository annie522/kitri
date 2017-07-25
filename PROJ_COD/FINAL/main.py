import glob, sys, os
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QAbstractItemView
from datetime import datetime
import matplotlib.pyplot as plt

import PROJ_COD.FINAL.Get_File_Hash as getFileHash
import PROJ_COD.FINAL.Get_Machine_Percentage as fileMachine
import PROJ_COD.FINAL.Get_MongoDB_Connection as mongoDB
import PROJ_COD.FINAL.Get_VirusTotal as vt


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("main.ui", self)
        self.ui.setWindowTitle("EMDETECTOR")
        self.ui.setWindowIcon(QIcon(QPixmap("logo.png")))
        self.ui.show()
        Form.selectLog(self)
        self.ui.numberCountLabel.setPixmap(QPixmap("그림4.jpg"))
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(4, False)
        self.dialogTextBrowser = MyDialog(self)

        global fname
        fname = ""

    @pyqtSlot()
    def fileopenBtnClick(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "/")
        fname = os.path.abspath(fname[0])
        self.ui.selected_file.setText(fname)

    @pyqtSlot()
    def startFileDetectionBtnClick(self):
        fname = self.ui.selected_file.text()
        if fname[-3:] != "exe" or fname == "":
            self.dialogTextBrowser.exec_()
            self.ui.selected_file.setText("선택 파일 없음")
        else:
            todayTime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            self.ui.page2_dateLabel.setText(todayTime)
            fileBaseName = os.path.basename(fname)
            self.ui.page2_filenameLabel.setText(fileBaseName)
            fileDirName = os.path.dirname(fname)
            self.ui.page2_filepathLabel.setText(fileDirName)
            fileHash = getFileHash.getFileHash(fname)
            self.ui.page2_md5Label.setText(fileHash)

            md5Check = getFileHash.checkHashInDB(fname)
            if md5Check[0] == "YES":
                if md5Check[1] == "M":
                    self.ui.MD5HashLabel.setText("악성 코드")
                    self.ui.page2_similarLabel.setText("악성파일")
                    self.ui.page2_similarLabel.setText("100%")
                    self.ui.numberCountLabel.setPixmap(QPixmap("그림1.jpg"))
                elif md5Check[1] == "N":
                    self.ui.MD5HashLabel.setText("정상파일")
                    self.ui.page2_similarLabel.setText("정상파일")
                    self.ui.numberCountLabel.setPixmap(QPixmap("그림1.jpg"))
                    self.ui.page2_similarLabel.setText("0%")
                else:
                    pass
            elif md5Check[0] == "NO":
                # self.ui.page2_similarLabel.setText("??%")
                self.ui.MD5HashLabel.setText("미등록")
                self.ui.numberCountLabel.setPixmap(QPixmap("그림1.jpg"))
                # 바이러스 토탈 돌리기
                dic = vt.get_mal_kind(fname)
                print(dic)
                print(dic[0])
                try:
                    if dic[0] > 10:
                        self.ui.numCountLabel2.setText("악성 코드")
                        self.ui.numberCountLabel.setPixmap(QPixmap("그림2.jpg"))
                    else:
                        self.ui.numCountLabel2.setText("정상 파일")
                        self.ui.numberCountLabel.setPixmap(QPixmap("그림2.jpg"))
                except:
                    self.ui.numCountLabel2.setText("Error")
                    self.ui.numberCountLabel.setPixmap(QPixmap("그림2.jpg"))
                    print("[+] dic['positives'] DOES NOT EXIST.")
                    # self.up.numberCountLabel.setPiexmap("그림1.jpg")
                    ###############################
                # 머신러닝 돌리는 코드
                # 파일 경로 전송해줘야됨
                machineRslt = fileMachine.getFIleMachine(fname)
                if machineRslt == "NORMAL":
                    self.ui.page2_similarLabel.setText("정상파일")
                    self.ui.machineResultLabel.setText("정상파일")
                else:
                    self.ui.page2_similarLabel.setText("악성파일")
                    self.ui.machineResultLabel.setText("악성파일")
                self.ui.numberCountLabel.setPixmap(QPixmap("그림3.jpg"))
            else:
                print("Error !!!")
                ################################

            #########################################################################################
            # 검사시작 버튼 클릭시 tab2 세팅

            # self.ui.page2_similarLabel.setText("48%")

            print(self.ui.numCountLabel2.text())

            # #### 정상파일인경우 강제 세팅 (추후 수정)
            if self.ui.numCountLabel2.text() == "정상 파일":
                self.ui.delFileBtn.setEnabled(False)
                print("ddddd머지")
                self.ui.delFileBtn.setStyleSheet("background-color:lightgray;color: white;border:nono;")
            #### 악성파일인경우 강제 세팅 (추후 수정)
            else:
                self.ui.delFileBtn.setEnabled(True)
                print("트루루루룰루루루루루")
                self.ui.delFileBtn.setStyleSheet("background-color: #0F75BD;color: white;border:nono;")
            #### 진행 결과에 따라 하단 라벨 이미지 변경
            # numberCount = "0"
            # if numberCount == "1": changeImage = QPixmap("그림1.jpg")
            # elif numberCount == "2": changeImage = QPixmap("그림2.jpg")
            # elif numberCount == "3": changeImage = QPixmap("그림3.jpg")
            # elif numberCount == "0": changeImage = QPixmap("그림4.jpg")
            # self.ui.numberCountLabel.setPixmap(changeImage)

            #########################################################################################
            Form.selectLog(self)
            # 검사시작 버튼 클릭시 tab3에 보여줄 로그 데이터베이스에 INSERT
            logDB = mongoDB.DBConn("shutdown").log
            if logDB.count() == 10:
                logDB.remove()
            insertLogData = {}
            insertLogData.update({"date": todayTime, "filename": fname, "result": "normal", "state": "finished"})
            logDB.insert(insertLogData)

            self.tabWidget.setTabEnabled(1, True)
            self.tabWidget.setCurrentIndex(1)

    @pyqtSlot()
    def delBtnClick(self):
        filePath = self.ui.page2_filepathLabel.text() + self.ui.page2_filenameLabel.text()
        print(filePath)
        # os.remove(filePath)

    @pyqtSlot()
    def selectLog(self):
        #########################################################################################
        # 검사기록 로그를 불러옴
        logDB = mongoDB.DBConn("shutdown").log
        logDBCount = logDB.count()
        logData = logDB.find()
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
        logDB = mongoDB.DBConn("shutdown").log
        logDB.remove()
        for j in range(0, 11):
            for i in range(0, 4):
                self.ui.logTable.setItem(j, i, QTableWidgetItem(""))

    @pyqtSlot()
    def delFileBtnClick(self):
        try:
            selectedRow = self.ui.logTable.currentRow()
            filePath = self.ui.logTable.item(selectedRow, 1).text()
            filePath = str(filePath).strip()
            print("삭제 시도!!")
            os.remove(filePath)
            print(" 삭제 됫어야한다.")
            print(filePath)
        except:
            pass

    @pyqtSlot()
    def folderopenBtnClick(self):
        global dname
        dname = QFileDialog.getExistingDirectory(self, 'Open Folder', '\\')
        dname = os.path.abspath(dname)
        self.ui.selected_folder.setText(dname)
        totalNum = len(glob.glob(dname + "/*.exe"))
        self.ui.numTotal.setText(str(totalNum))

    @pyqtSlot()
    def startFolderDetectionBtnClick(self):
        self.ui.inputNormal.setText(self.ui.numNormal.text())
        self.ui.inputMalware.setText(self.ui.numMalware.text())

        flist = glob.glob(dname + "/*.exe")
        normalCount = 0
        malwareCount = 0
        for fname in flist:
            # 머신러닝 돌리는 코드
            # 파일 경로 전송해줘야됨
            print("[+] fname : ", fname)
            machineRslt = fileMachine.getFIleMachine(fname)
            print("{+}", machineRslt)
            if machineRslt == "NORMAL":
                normalCount += 1
            else:
                malwareCount += 1

        self.ui.detectedNormal.setText(str(normalCount))
        self.ui.detectedMalware.setText(str(malwareCount))
        a = int(self.ui.inputNormal.text())
        b = int(self.ui.detectedNormal.text())
        c = int(self.ui.detectedMalware.text())
        d = int(self.ui.inputMalware.text())
        try:
            detectionResult = (abs(a - b) / b) * 100
        except:
            detectionResult = (abs(d - c) / c) * 100
        self.ui.detectionResultLabel.setText(str(detectionResult) + "%")

        ## 결과값 그래프로 보여주기
        colors = ["pink", "skyblue"]
        title = "DETECTION RESULT"
        plt.title(title, fontsize=25)
        # label = ["NORMAL","MALWARE"]
        # ax = plt.axes(["MALWARE : 10", "NORMAL : 10"])
        # slice = [number1[0], number2[0]]
        # plt.pie(slice, startangle=90, labels=label)
        label = ["NORMAL", "MALWARE"]
        fracs = [b, c]

        print("HERE")
        plt.pie(fracs, labels=label, startangle=90, autopct='%1.1f%%', explode=(0, 0.1), colors=colors)

        chartImage = plt.gcf()
        chartImage.savefig("chartImage.jpg")
        self.ui.resultGraph.setPixmap(QPixmap("chartImage.jpg"))
        self.ui.resultGraph.setScaledContents(True)

        self.tabWidget.setTabEnabled(4, True)
        self.tabWidget.setCurrentIndex(4)


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.ui = uic.loadUi("alert.ui", self)
        self.ui.setWindowTitle("EMDETECTOR")
        self.ui.setWindowIcon(QIcon(QPixmap("logo.png")))
        self.ui.label.setText("EXE 파일을 선택해 주세요")

    @pyqtSlot()
    def selectNoBtn(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())