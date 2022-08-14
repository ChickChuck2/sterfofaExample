from asyncio import Task
import os
from random import Random
import sys
from threading import Thread
from time import sleep, time
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
import math
from IPython.display import Audio

windowWidth = 620
windowHeight = 400
class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Aceitação'
        self.left = 10
        self.top = 10
        self.setObjectName("window")
        self.width = windowWidth
        self.height = windowHeight
        lines = ""
        with open("style.css") as f:
            lines = f.read()
        self.style = lines
        self.setStyleSheet(self.style)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        title = QLabel("Quer namorar amigo?", self)
        title.move(50, 10)
        title.setFont(QFont('Times', 40))
        
        button = QPushButton('Sim', self)
        button.setGeometry(0,0,70,30)
        button.setToolTip('Vai lá… Pode clicar, não morde')
        button.move(100,70)
        button.clicked.connect(self.simAction)

        button1 = QPushButton("NÃO", self)
        button1.setGeometry(0,0,70,30)
        button1.height = 100
        button1.move(190,70)
        button1.clicked.connect(self.naoAction)
        self.show()
        self.thread(button1)

    @pyqtSlot()
    def simAction(self):
        print("Sim , eu aceito")
    @pyqtSlot()
    def naoAction(self):
        print("NÃO!!!!!")
    
    def thread(self, btn: QPushButton):
        t1=Thread(target=lambda: self.Operation(btn))
        t1.start()

    def Operation(self, btn: QPushButton):
        while(True):
            if(self.isHidden()):
                break
            sleep(0.05)
            cursor = self.mapFromGlobal(QtGui.QCursor.pos())
            btnPos = btn.pos()
            #print(f"CURSOR: {cursor}")
            #print(f"BUTTON: {btn.pos()}")
            iscloseX = math.isclose(cursor.x(), btnPos.x() + 50, abs_tol= 70)
            iscloseY = math.isclose(cursor.y(), btnPos.y() - 10, abs_tol= 50)
            if(iscloseX and iscloseY):
                randw = Random()
                btn.move(randw.randint(a=0, b=windowWidth - 10), randw.randint(a=0, b=windowHeight - 10))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
