from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from time import sleep
import sys, os

def bar():
    class MyCustomWidget(QWidget):

        def __init__(self, parent=None):
            super(MyCustomWidget, self).__init__(parent)
            layout = QVBoxLayout(self)

            # Create a progress bar and a button and add them to the main layout
            self.progressBar = QProgressBar(self)
            self.progressBar.setRange(0,1)
            layout.addWidget(self.progressBar)
            button = QPushButton("Start", self)
            layout.addWidget(button)
            button2 = QPushButton("Close", self)
            layout.addWidget(button2)

            button.clicked.connect(self.onStart)
            button2.clicked.connect(self.close)

            self.myLongTask = TaskThread()
            self.myLongTask.taskFinished.connect(self.onFinished)

        def onStart(self):
            self.progressBar.setRange(0,0)
            self.myLongTask.start()

        def onFinished(self):
            # Stop the pulsation
            self.progressBar.setRange(0,4)
            self.progressBar.setValue(1)


    class TaskThread(QtCore.QThread):
        taskFinished = QtCore.pyqtSignal()
        def run(self):
            os.system('sudo apt-get install leafpad')
            self.taskFinished.emit()

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MyCustomWidget()
        window.resize(640, 480)
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    bar()