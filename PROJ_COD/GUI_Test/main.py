import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QFileDialog, QTableWidgetItem, QAbstractItemView, QTableWidget
import PROJ_COD.GUI_Test.detectionMain as detectionMain
from datetime import datetime
import os
import PROJ_COD.GUI_Test.Get_File_Hash as getFileHash
import PROJ_COD.MongoDB_Connection as mongoDB
import PROJ_COD.Machine.kim.Con_Virustotal as vt
import PROJ_COD.GUI_Test.fileopen as fo

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("main.ui",self)
        self.ui.show()
        Form.selectLog(self)
        self.ui.numberCountLabel.setPixmap(QPixmap("그림4.jpg"))

    @pyqtSlot()
    def fileopenBtnClick(self):
        global fname
        fname = QFileDialog.getOpenFileName(self, 'Open file', "/")
        fname = os.path.abspath(fname[0])
        self.ui.selected_file.setText(fname)


    @pyqtSlot()
    def startFileDetectionBtnClick(self):
        todayTime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        self.ui.page2_dateLabel.setText(todayTime)
        fileBaseName = os.path.basename(fname)
        self.ui.page2_filenameLabel.setText(fileBaseName)
        fileDirName = os.path.dirname(fname)
        self.ui.page2_filepathLabel.setText(fileDirName)
        fileHash = getFileHash.getFileHash(fname)
        self.ui.page2_md5Label.setText(fileHash)

        md5Check = getFileHash.checkHashInDB(fname)
        print(type(md5Check))
        print(md5Check)
        if md5Check[0] == "YES":
            if md5Check[1] == "M":
                print("Malware!!!!")
                self.ui.MD5HashLabel.setText("악성 코드")
                self.ui.page2_similarLabel.setText("100%")
                self.ui.numberCountLabel.setPixmap(QPixmap("그림1.jpg"))
            elif md5Check[1] == "N":
                print("Nomal File!!!!!!")
                self.ui.MD5HashLabel.setText("정상 파일")
                self.ui.page2_similarLabel.setText("0%")
                self.ui.numberCountLabel.setPixmap(QPixmap("그림1.jpg"))
            else:
                print("Error11111111111111111")
            print("YESTSE")
        elif md5Check[0] == "NO":
            self.ui.page2_similarLabel.setText("1000%")
            self.ui.MD5HashLabel.setText("미등록")
            self.ui.numberCountLabel.setPixmap(QPixmap("그림1.jpg"))


            ################################

            main = vt.Virustotal()
            dic = main.rscReport(md5Check)
            try:
                if dic['positives'] > 10:
                    for key, value in dic['scans'].items():
                        if value['result'] != None:
                            ss=dic['positives'], value['result'], dic['md5']
                            self.ui.numCountLabel2.setText("악성 코드")
                            self.ui.numberCountLabel.setPixmap(QPixmap("그림2.jpg"))

                else:
                    self.ui.numCountLabel2.setText("정상 파일")
                    self.ui.numberCountLabel.setPixmap(QPixmap("그림2.jpg"))
            except:
                self.ui.numCountLabel2.setText("Error")
                self.ui.numberCountLabel.setPixmap(QPixmap("그림2.jpg"))
                print("[+] dic['positives'] DOES NOT EXIST.")
            ################################
            rrr= vt.get_mal_kind(fname)
            print(rrr)
            #self.up.numberCountLabel.setPiexmap("그림1.jpg")
        else:
            print("Error !!!")

        #########################################################################################
        # 검사시작 버튼 클릭시 tab2 세팅

        # self.ui.page2_similarLabel.setText("48%")
        # #### 정상파일인경우 강제 세팅 (추후 수정)
        if self.ui.page2_similarLabel.text() == "0%":
            self.ui.delFileBtn.setEnabled(False)
            self.ui.delFileBtn.setStyleSheet("background-color:lightgray;color: white;border:nono;")
        #### 악성파일인경우 강제 세팅 (추후 수정)
        else:
            self.ui.delFileBtn.setEnabled(True)
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
        insertLogData.update({"date": todayTime, "filename":fname, "result":"normal","state":"finished"})
        logDB.insert(insertLogData)



    @pyqtSlot()
    def selectLog(self):
        print("[+] selectLog")
        #########################################################################################
        # 검사기록 로그를 불러옴
        logDB = mongoDB.DBConn("shutdown").log
        logDBCount = logDB.count()
        logData = logDB.find()
        # 불러온 기록 테이블에 보여주기
        num = 0
        j = 0
        for item in logData:
            print(item)
            item = str(item).split(",")
            item[1] = item[1].replace("'date': '", "").replace("'", "")
            item[2] = item[2].replace("'filename': '", "").replace("'", "").replace("\\\\","\\")
            item[3] = item[3].replace("'result': '", "").replace("'", "")
            item[4] = item[4].replace("'state': '", "").replace("'}", "")
            showData = []
            showData.append(item[1])
            showData.append(item[2])
            showData.append(item[3])
            showData.append(item[4])
            print("showData : ",showData)
            print("logDBCount : ", logDBCount)
            for i in range(0, 4):
                print("j : ", j, "   i : ",i, "showData : ", showData[i])
                self.ui.logTable.setItem(j, i, QTableWidgetItem(showData[i]))
                self.ui.logTable.item(j, i).setTextAlignment(Qt.AlignCenter)
            j += 1
        # 테이블 CSS 설정
        self.ui.logTable.horizontalHeader().setStretchLastSection(True)
        self.ui.logTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.logTable.setColumnWidth(0, 150)
        self.ui.logTable.setColumnWidth(1,300)
        self.ui.logTable.setSelectionBehavior(1)

    @pyqtSlot()
    def saveLogBtnClick(self):
        logDB = mongoDB.DBConn("shutdown").log
        logData = logDB.find({},{'_id':0})
        logDBCount = logDB.count()
        for item in logData:
            inputData = str(item).replace("{","").replace("}","")
            print("inputData : " , inputData)
            f = open("log.txt", 'w')
            for i in range(1, logDBCount+1):
                data = "NUMBER{} --> {}\n".format(i, inputData)
                f.write(data)
            f.close()

    @pyqtSlot()
    def delLogBtnClick(self):
        logDB = mongoDB.DBConn("shutdown").log
        logDB.remove()
        for j in range(0,11):
            for i in range(0, 4):
                self.ui.logTable.setItem(j, i,QTableWidgetItem(""))

    @pyqtSlot()
    def delFileBtnClick(self):
        try:
            selectedRow = self.ui.logTable.currentRow()
            filePath = self.ui.logTable.item(selectedRow,1).text()
            filePath = str(filePath).strip()
            print(filePath)
            os.remove(filePath)
            print("111111111111111")
        except:
            pass

    @pyqtSlot()
    def selectYesBtn(self):
        print("11111111111")

    @pyqtSlot()
    def selectNoBtn(self):
        print("11111111111")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())