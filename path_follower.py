import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5 import QtCore
import numpy as np
import pyqtgraph as pg


nameport = '/dev/ttyUSB0'
baudrate = 115200
serial = 0

def moveup():
    serial.write("z".encode())

def movedown():
    serial.write("s".encode())

def moveright():
    serial.write("d".encode())

def moveleft():
    serial.write("q".encode())

def start():
    serial.write("m".encode())

def stop():
    serial.write("o".encode())

def low():
    serial.write("l".encode())

def high():
    serial.write("h".encode())

def auto():
    serial.write("a".encode())
    
def openSerialPort():
    global serial
    serial = QSerialPort()
    serial.setPortName(nameport)
    r = serial.open(QtCore.QIODevice.ReadWrite)
    if not r:
        print('Port open error')
    else:
        print('Port opened')
        serial.setBaudRate(baudrate)
        serial.setStopBits(QSerialPort.OneStop)
        serial.setParity(QSerialPort.NoParity)
        serial.setDataBits(QSerialPort.Data8)
        serial.setFlowControl(QSerialPort.NoFlowControl)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        self.last_x, self.last_y = None, None
        self.path = []  # List to store the path coordinates

    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return  # Ignore the first time.

        # Append the new coordinates to the path
        self.path.append((e.x(), e.y()))

        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

        # Print the path coordinates
        print("Path coordinates:", self.path)
        # Clear the path for the next drawing
        for i in range(len(self.path)-1):
                moveup()
                x = self.path[i][0]
                y = self.path[i][1]
                x_2 = self.path[i+1][0]
                y_2 = self.path[i+1][1]
                dx = x_2-x
                dy = y_2-y
                angle_radians = math.atan2(dy, dx)
                angle_degrees = math.degrees(angle_radians)
                print(angle_degrees)
        self.path = []

app = QtWidgets.QApplication(sys.argv)
openSerialPort()
#serial.readyRead.connect(readData)
window = MainWindow()
window.show()
app.exec_()

