from PyQt5 import QtCore, QtGui, QtWidgets
import test_rcc
import open

class SuccessList(QWidget, QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("shutdown.ui", self)
        self.ui.show()

        def clickBtn1(self):
            open.openFolder()

            import folderopen, test_rcc

            def clickBtn1(self):
                open.openFolder()