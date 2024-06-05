# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_maindBzWaM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PyQt5.QtCore import QTimer
from PySide2.QtGui import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from matplotlib.figure import Figure
import math
import numpy as np
from collections import deque
from PyQt5.QtCore import *
import subprocess
from datetime import datetime, timedelta
import matplotlib.dates as mdates
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
nameport = '/dev/ttyUSB0'
baudrate = 115200

class MainWindow(QMainWindow):
        def __init__(self):
                QMainWindow.__init__(self)
                self.timer = QTimer()
                self.resize(1000, 700)
                self.setMinimumSize(QSize(1000, 700))

                self.centralwidget = QWidget()
                self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
        "border-radius: 10px;")
                
                self.verticalLayout = QVBoxLayout(self.centralwidget)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)


                self.auto_mode = QPushButton("Auto Mode")
                self.auto_mode.clicked.connect(self.auto)
                self.auto_mode.setStyleSheet("background-color: lightblue; color: black;")
                self.auto_mode.setMinimumSize(75, 25)  # Adjust the values as needed
                self.auto_mode.setMaximumSize(125, 50)
                self.auto_mode.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.stop_button = QPushButton("Stop")
                self.stop_button.clicked.connect(self.stop)
                self.stop_button.setStyleSheet("background-color: lightblue; color: black;")
                self.stop_button.setMinimumSize(75, 25)  # Adjust the values as needed
                self.stop_button.setMaximumSize(125, 50)
                self.stop_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


                self.open_new_window_button = QPushButton("path")
                self.open_new_window_button.clicked.connect(self.open_new_window)
                self.open_new_window_button.setStyleSheet("background-color: lightblue; color: black;")
                self.open_new_window_button.setMinimumSize(75, 25)  # Adjust the values as needed
                self.open_new_window_button.setMaximumSize(125, 50)
                self.open_new_window_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.up_button = QPushButton("up")
                self.up_button.clicked.connect(self.moveup)
                self.up_button.setStyleSheet("background-color: lightblue; color: black;")
                self.up_button.setMinimumSize(75, 25)  # Adjust the values as needed
                self.up_button.setMaximumSize(125, 50)
                self.up_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.down_button = QPushButton("down")
                self.down_button.clicked.connect(self.movedown)
                self.down_button.setStyleSheet("background-color: lightblue; color: black;")
                self.down_button.setMinimumSize(75, 25)  # Adjust the values as needed
                self.down_button.setMaximumSize(125, 50)
                self.down_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.left_button = QPushButton("left")
                self.left_button.clicked.connect(self.moveleft)
                self.left_button.setStyleSheet("background-color: lightblue; color: black;")
                self.left_button.setMinimumSize(125, 25)  # Adjust the values as needed
                self.left_button.setMaximumSize(125, 50)
                self.left_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.empty_button = QPushButton()
                self.empty_button.setMinimumSize(50, 25)  # Adjust the values as needed
                self.empty_button.setMaximumSize(100, 50)
                self.empty_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.right_button = QPushButton("right")
                self.right_button.clicked.connect(self.moveright)
                self.right_button.setStyleSheet("background-color: lightblue; color: black;")
                self.right_button.setMinimumSize(125, 25)  # Adjust the values as needed
                self.right_button.setMaximumSize(125, 50)
                self.right_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.start_button = QPushButton("Start")
                self.start_button.clicked.connect(self.start)
                self.start_button.setStyleSheet("background-color: lightblue; color: black;")
                self.start_button.setMinimumSize(75, 25)  # Adjust the values as needed
                self.start_button.setMaximumSize(125, 50)
                self.start_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                
                self.high_speed = QLabel()
                self.high_speed.setText('Met un nombre entre 0 et 255')
                self.high_speed.setStyleSheet("background-color: lightblue; color: black;")
                self.high_speed.setMinimumSize(75, 25)  # Adjust the values as needed
                self.high_speed.setMaximumSize(200, 50)
                self.high_speed.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.high_speed.setAlignment(Qt.AlignCenter)

                self.line_toSend = QLineEdit()
                self.line_toSend.setMinimumSize(75, 25)  # Adjust the values as needed
                self.line_toSend.setMaximumSize(125, 50)
                self.line_toSend.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.line_toSend.setAlignment(Qt.AlignCenter)
                self.line_toSend.setAlignment(Qt.AlignCenter)

                self.btn_send = QPushButton()
                self.btn_send.setMinimumSize(75, 25)  # Adjust the values as needed
                self.btn_send.setMaximumSize(125, 50)
                self.btn_send.setText('SEND')
                self.btn_send.setStyleSheet("background-color: lightblue; color: black;")
                self.btn_send.clicked.connect(self.speed)  # Action associée à l'appui sur le bouton ( signal )
                self.btn_send.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################

                self.content_bar = QFrame(self.centralwidget)
                self.content_bar.setStyleSheet(u"background-color: none;")
                self.content_bar.setFrameShape(QFrame.StyledPanel)
                self.content_bar.setFrameShadow(QFrame.Raised)
                self.verticalLayout_4 = QVBoxLayout(self.content_bar)
                self.stackedWidget = QStackedWidget(self.content_bar)
                self.stackedWidget.setObjectName(u"stackedWidget")
                self.stackedWidget.setStyleSheet(u"background-color: none;")

                self.page_home = QWidget()

                self.verticalLayout_5 = QVBoxLayout(self.page_home)

                self.frame_content_home = QFrame(self.page_home)
                self.frame_content_home.setObjectName(u"frame_content_home")
                self.frame_content_home.setFrameShape(QFrame.StyledPanel)
                self.frame_content_home.setFrameShadow(QFrame.Raised)

                self.verticalLayout_9 = QVBoxLayout(self.frame_content_home)

##################################BUTTONS#####################################################
                self.horizontalLayout_P = QHBoxLayout()
                self.horizontalLayout_P.setAlignment(Qt.AlignCenter)
                self.horizontalLayout_P.addWidget(self.left_button)
                self.horizontalLayout_P.addWidget(self.empty_button)
                self.horizontalLayout_P.addWidget(self.right_button)

                self.verticalLayout_p10k = QHBoxLayout()
                self.verticalLayout_p10k.addWidget(self.open_new_window_button)

                self.horizontalLayout_P1 = QHBoxLayout()
                self.horizontalLayout_P1.setAlignment(Qt.AlignCenter)
                self.horizontalLayout_P1.addWidget(self.up_button)
                
                self.horizontalLayout_P2 = QHBoxLayout()
                self.horizontalLayout_P2.setAlignment(Qt.AlignCenter)
                self.horizontalLayout_P2.addWidget(self.down_button)

                self.verticalLayout_p3 = QVBoxLayout()
                self.verticalLayout_p3.setAlignment(Qt.AlignLeft)
                self.verticalLayout_p3.addWidget(self.start_button)
                self.verticalLayout_p3.addWidget(self.stop_button)

                self.horizontalLayout_P4 = QHBoxLayout()
                self.horizontalLayout_P4.setAlignment(Qt.AlignCenter)
                self.horizontalLayout_P4.addWidget(self.auto_mode)

                self.horizontalhi1 = QHBoxLayout()
                self.horizontalhi1.addWidget(self.high_speed)
                self.horizontalhi1.setAlignment(Qt.AlignCenter)

                self.horizontalhi = QVBoxLayout()
                self.horizontalhi.addWidget(self.line_toSend)
                self.horizontalhi.addWidget(self.btn_send)
                self.horizontalhi.setAlignment(Qt.AlignCenter)

                self.verticalLayout_p = QVBoxLayout()
                self.verticalLayout_p.setAlignment(Qt.AlignRight)
                self.verticalLayout_p.addLayout(self.horizontalhi1)
                self.verticalLayout_p.addLayout(self.horizontalhi)

                self.verticalLayout_M = QVBoxLayout()
                self.verticalLayout_M.setAlignment(Qt.AlignRight)
                self.verticalLayout_M.addLayout(self.verticalLayout_p)

                self.verticalLayout_10 = QVBoxLayout()
                self.verticalLayout_10.setAlignment(Qt.AlignCenter)
                self.verticalLayout_10.addLayout(self.horizontalLayout_P1)
                self.verticalLayout_10.addLayout(self.horizontalLayout_P)
                self.verticalLayout_10.addLayout(self.horizontalLayout_P2)
                self.verticalLayout_10.addLayout(self.horizontalLayout_P4)
                self.verticalLayout_10.addLayout(self.verticalLayout_p10k)

                self.horizontalLayout_p10 = QHBoxLayout()
                self.horizontalLayout_p10.setAlignment(Qt.AlignHCenter)
                self.horizontalLayout_p10.addLayout(self.verticalLayout_p3)
                self.horizontalLayout_p10.addLayout(self.verticalLayout_10)
                self.horizontalLayout_p10.addLayout(self.verticalLayout_M)

                
                self.figure = Figure()
                self.axes = self.figure.add_subplot(111)
                self.canvas = FigureCanvas(self.figure)
                self.figure.patch.set_facecolor('lightblue')
                self.toolbar = NavigationToolbar2QT(self.canvas)
                self.toolbar.setStyleSheet("background-color: lightblue;")
                self.horizontal = QVBoxLayout()
                self.horizontal.setAlignment(Qt.AlignCenter)
                self.horizontal.addWidget(self.canvas)
                self.horizontal.addWidget(self.toolbar)
                self.verticalLayout_9.addLayout(self.horizontal)
                self.verticalLayout_9.addLayout(self.horizontalLayout_p10)


                self.verticalLayout_5.addWidget(self.frame_content_home)

                self.verticalLayout_4.addWidget(self.page_home)

                self.verticalLayout.addWidget(self.content_bar)

                self.setCentralWidget(self.centralwidget)

                self.stackedWidget.setCurrentIndex(0)
                
                self.serial = QSerialPort()
                self.openSerialPort()
                self.serial.readyRead.connect(self.update_data)

                self.data_sets = deque(maxlen=60) 
                self.update_plot()
        def openSerialPort(self):
                        self.serial.setPortName(nameport)
                        r = self.serial.open(QtCore.QIODevice.ReadWrite)
                        if not r:
                                print('Port open error')
                        else:
                                print('Port opened')
                                self.serial.setBaudRate(baudrate)
                                self.serial.setStopBits(1)
                                self.serial.setParity(0) # no parity
                                self.serial.setDataBits(8)
                                self.serial.setFlowControl(0)

        def open_new_window(self):
                self.serial.close()
                subprocess.run(['python','path.py'])
                       
        ############################################################################################
        def update_data(self):
                data = str(self.serial.readAll())
                print(data)
                data =data[2::]
                data = data[:-1]
                print(data)
                data_list = [int(x) for x in data.split(' ')]
                print(data_list)
                self.plot_data(data_list)
                
                 
        def plot_data(self, data):
                current_time = datetime.now()
                self.data_sets.append((current_time, data[0],data[1]))
                self.update_plot()

        def update_plot(self):
                self.axes.clear()
        
                x_values = []
                y_values = []
                y1_values = []
                if self.data_sets:
                        for timestamp, data ,data1 in self.data_sets:
                                x_values.append(timestamp)
                                y_values.append(((data)))
                                y1_values.append(((data1)))
                                print(data)
                        print(len(x_values))
                        print(len(y_values))
                        self.axes.plot(x_values, y_values, marker='o')
                        self.axes.plot(x_values, y1_values, marker='x')
                        self.axes.set_ylabel('Y Value')
                        self.axes.set_title('Input Plot')
                        self.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
                        current_time = datetime.now()
                        min_time = current_time - timedelta(seconds=10)
                        max_time = current_time
                        self.axes.set_xlim(min_time, max_time)
                        
                else:
                        self.axes.plot(0, 0, marker='o')
                self.canvas.draw()
                

############################################################################################
        def moveup(self):
                self.serial.write("z".encode())

        def movedown(self):
                self.serial.write("s".encode())

        def moveright(self):
                self.serial.write("d".encode())

        def moveleft(self):
                self.serial.write("q".encode())

        def start(self):
                self.openSerialPort()
        def stop(self):
                self.openSerialPort()
                self.serial.write("o".encode())
                QTimer.singleShot(1000, self.serial.close)
        def speed(self):
                 #padded_value = str(value).zfill(3)
                self.serial.write("v".encode())
                text_to_send =  self.line_toSend.text()
                text_to_send =text_to_send.zfill(3)
                QTimer.singleShot(100, lambda:self.serial.write(text_to_send[0].encode())) 
                QTimer.singleShot(200, lambda:self.serial.write(text_to_send[1].encode())) 
                QTimer.singleShot(300,lambda:self.serial.write(text_to_send[2].encode())) 
        def auto(self):
                self.serial.write("j".encode())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    window.show()
    sys.exit(app.exec_())