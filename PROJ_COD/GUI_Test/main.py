import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QFileDialog
#import kitri.PROJ_COD.GUI_Test.detectionMain as detectionMain

import kitri.PROJ_COD.GUI_Test.fileopen as fo

fname = ""

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("main.ui", self)
        self.ui.show()

    @pyqtSlot()
    def fileopenBtnClick(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "/")
        fname = fname[0]
        self.ui.selected_file.setText(fname[0])


    @pyqtSlot()
    def startFileDetectionBtnClick(self):
        print("11111111111111111111111111")
        # detectionMain.detectionMain(fname)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())