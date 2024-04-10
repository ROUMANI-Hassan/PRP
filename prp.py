import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5 import QtCore
import numpy as np
import matplotlib.pyplot as plt
import time

nameport='/dev/ttyUSB0'
baudrate=115200


def moveup():
	serial.write("z".encode())
def movedown():
	serial.write("s".encode())
def moveright():
	serial.write("d".encode())
def moveleft():
	serial.write("q".encode())
def start():
	serial.write("l".encode())
def keyPressEvent(event):
    key = event.key()
    if key == QtCore.Qt.Key_Up:
        moveup()
    elif key == QtCore.Qt.Key_Down:
        movedown()
    elif key == QtCore.Qt.Key_Left:
        moveleft()
    elif key == QtCore.Qt.Key_Right:
        moveright()
    elif key == QtCore.Qt.Key_Space:
        start()
app = QApplication(sys.argv)
prp_ui = QWidget()
prp_ui.setWindowTitle("Projet Pluridisciplinaire")
serial = QSerialPort()
serial.setPortName(nameport)
r = serial.open(QtCore.QIODevice.ReadWrite)
if not r:
        print('Port open error')
else:
        print('Port opened')
        serial.setBaudRate(baudrate)
        serial.setStopBits(1)
        serial.setParity(0) # no parity
        serial.setDataBits(8)
        serial.setFlowControl(0)

serial.write("test".encode())
graph_layout = QVBoxLayout(prp_ui)
figure , axe = plt.subplots()
canvas = figure.canvas
graph_layout.addWidget(canvas)
canvas.setFixedSize(1500, 1000)

start_button = QPushButton(prp_ui)
start_button.setText("Start")
start_button.setFixedSize(200,50)
start_button.clicked.connect(start)

move_up = QPushButton(prp_ui)
move_up.setText("UP")
move_up.move(1700,400)
move_up.setFixedSize(100,50)
move_up.clicked.connect(moveup)

move_down = QPushButton(prp_ui)
move_down.setText("DOWN")
move_down.setFixedSize(100,50)
move_down.move(1700,600)
move_down.clicked.connect(movedown)

move_right = QPushButton(prp_ui)
move_right.setText("RIGHT")
move_right.setFixedSize(100,50)
move_right.move(1800,500)
move_right.clicked.connect(moveright)

move_left = QPushButton(prp_ui)
move_left.setText("LEFT")
move_left.setFixedSize(100,50)
move_left.move(1600,500)
move_left.clicked.connect(moveleft)

prp_ui.keyPressEvent = keyPressEvent
prp_ui.show()
sys.exit(app.exec_())
