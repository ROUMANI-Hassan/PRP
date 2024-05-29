# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_maindBzWaM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import os
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import subprocess

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                
                if MainWindow.objectName():
                        MainWindow.setObjectName(u"MainWindow")
                self.nameport = '/dev/ttyUSB0'
                self.baudrate = 115200
                self.serial = 0
                self.publicx = 0
                self.timer = QTimer()

                MainWindow.resize(1000, 700)
                MainWindow.setMinimumSize(QSize(1000, 700))

                
                

                self.centralwidget = QWidget(MainWindow)
                self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
        "border-radius: 10px;")
                
                self.verticalLayout = QVBoxLayout(self.centralwidget)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
               
 ###################################################################################################### 
 ###################################################################################################### 
 ###################################################################################################### 
 ###################################################################################################### 
 ###################################################################################################### 
 ###################################################################################################### 
 ###################################################################################################### 
 ######################################################################################################       


                self.auto_mode = QPushButton("Auto Mode")
                self.auto_mode.clicked.connect(self.auto)
                self.auto_mode.setStyleSheet("background-color: black; color: white;")
                self.auto_mode.setMinimumSize(75, 25)  # Adjust the values as needed
                self.auto_mode.setMaximumSize(125, 50)
                self.auto_mode.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.stop_button = QPushButton("Stop")
                self.stop_button.clicked.connect(self.stop)
                self.stop_button.setStyleSheet("background-color: black; color: white;")
                self.stop_button.setMinimumSize(75, 25)  # Adjust the values as needed
                self.stop_button.setMaximumSize(125, 50)
                self.stop_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


                self.open_new_window_button = QPushButton("path")
                self.open_new_window_button.clicked.connect(self.open_new_window)
                self.open_new_window_button.setStyleSheet("background-color: black; color: white;")
                self.open_new_window_button.setMinimumSize(75, 25)  # Adjust the values as needed
                self.open_new_window_button.setMaximumSize(125, 50)
                self.open_new_window_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.up_button = QPushButton("up")
                self.up_button.clicked.connect(self.moveup)
                self.up_button.setStyleSheet("background-color: black; color: white;")
                self.up_button.setMinimumSize(75, 25)  # Adjust the values as needed
                self.up_button.setMaximumSize(125, 50)
                self.up_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.down_button = QPushButton("down")
                self.down_button.clicked.connect(self.movedown)
                self.down_button.setStyleSheet("background-color: black; color: white;")
                self.down_button.setMinimumSize(75, 25)  # Adjust the values as needed
                self.down_button.setMaximumSize(125, 50)
                self.down_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.left_button = QPushButton("left")
                self.left_button.clicked.connect(self.moveleft)
                self.left_button.setStyleSheet("background-color: black; color: white;")
                self.left_button.setMinimumSize(125, 25)  # Adjust the values as needed
                self.left_button.setMaximumSize(125, 50)
                self.left_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.empty_button = QPushButton()
                self.empty_button.setMinimumSize(50, 25)  # Adjust the values as needed
                self.empty_button.setMaximumSize(100, 50)
                self.empty_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.right_button = QPushButton("right")
                self.right_button.clicked.connect(self.moveright)
                self.right_button.setStyleSheet("background-color: black; color: white;")
                self.right_button.setMinimumSize(125, 25)  # Adjust the values as needed
                self.right_button.setMaximumSize(125, 50)
                self.right_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.start_button = QPushButton("Start")
                self.start_button.clicked.connect(self.start)
                self.start_button.setStyleSheet("background-color: black; color: white;")
                self.start_button.setMinimumSize(75, 25)  # Adjust the values as needed
                self.start_button.setMaximumSize(125, 50)
                self.start_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                
                self.high_speed = QLabel()
                self.high_speed.setText('Message à Envoyer :')
                self.high_speed.setMinimumSize(75, 25)  # Adjust the values as needed
                self.high_speed.setMaximumSize(125, 50)
                self.high_speed.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.line_toSend = QLineEdit()
                self.btn_send = QPushButton()
                self.btn_send.setMinimumSize(75, 25)  # Adjust the values as needed
                self.btn_send.setMaximumSize(125, 50)
                self.btn_send.setText('Send Message')
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

                self.frame_infos = QFrame(self.frame_content_home)
                self.frame_infos.setObjectName(u"frame_infos")
                self.frame_infos.setFrameShape(QFrame.StyledPanel)
                self.frame_infos.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_4 = QHBoxLayout(self.frame_infos)

                self.frame_infos2 = QFrame(self.frame_content_home)
                self.frame_infos2.setFrameShape(QFrame.StyledPanel)
                self.frame_infos2.setFrameShadow(QFrame.Raised)


                self.frame_circle_1 = QFrame(self.frame_infos)
                self.frame_circle_1.setMinimumSize(QSize(250, 250))
                self.frame_circle_1.setMaximumSize(QSize(250, 250))
                self.frame_circle_1.setStyleSheet(u"QFrame{\n"
        "	border: 5px solid rgb(60, 231, 195);\n"
        "	border-radius: 125px;\n"
        "}\n"
        "QFrame:hover {\n"
        "	border: 5px solid rgb(105, 95, 148);\n"
        "}")
                font = QFont()
                font.setFamily(u"Roboto")
                font.setPointSize(11)

                font2 = QFont()
                font2.setFamily(u"Roboto Thin")
                font2.setPointSize(20)

                font3 = QFont()
                font3.setFamily(u"Roboto Thin")
                font3.setPointSize(60)

                self.frame_circle_1.setFrameShape(QFrame.StyledPanel)
                self.frame_circle_1.setFrameShadow(QFrame.Raised)
                self.verticalLayout_6 = QVBoxLayout(self.frame_circle_1)
                self.verticalLayout_6.setSpacing(10)
                self.label = QLabel(self.frame_circle_1)
                self.label.setFont(font)
                self.label.setStyleSheet(u"border: none;\n"
        "color: rgb(60, 231, 195);")
                self.label.setAlignment(Qt.AlignCenter)

                self.verticalLayout_6.addWidget(self.label)

                self.label_3 = QLabel(self.frame_circle_1)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet(u"border: none;\n"
        " color: rgb(128, 102, 168);")
                self.label_3.setAlignment(Qt.AlignCenter)

                self.verticalLayout_6.addWidget(self.label_3)

                self.label_2 = QLabel(self.frame_circle_1)
                self.label_2.setFont(font2)
                self.label_2.setStyleSheet(u"border: none;\n"
        "color: rgb(220,220,220);")
                self.label_2.setAlignment(Qt.AlignCenter)

                self.verticalLayout_6.addWidget(self.label_2)

                self.horizontalLayout_4.addWidget(self.frame_circle_1)

                self.frame_circle_2 = QFrame(self.frame_infos)
                self.frame_circle_2.setMinimumSize(QSize(250, 250))
                self.frame_circle_2.setMaximumSize(QSize(250, 250))
                self.frame_circle_2.setStyleSheet(u"QFrame{\n"
        "	border: 5px solid rgb(60, 231, 195);\n"
        "	border-radius: 125px;\n"
        "}\n"
        "QFrame:hover {\n"
        "	border: 5px solid rgb(105, 95, 148);\n"
        "}")
                self.frame_circle_2.setFrameShape(QFrame.StyledPanel)
                self.frame_circle_2.setFrameShadow(QFrame.Raised)
                self.verticalLayout_7 = QVBoxLayout(self.frame_circle_2)
                self.verticalLayout_7.setSpacing(10)
                self.label_5 = QLabel(self.frame_circle_2)
                self.label_5.setFont(font2)
                self.label_5.setStyleSheet(u"border: none;\n"
        "color: rgb(60, 231, 195);")
                self.label_5.setAlignment(Qt.AlignCenter)

                self.verticalLayout_7.addWidget(self.label_5)

                self.label_6 = QLabel(self.frame_circle_2)
                self.label_6.setFont(font3)
                self.label_6.setStyleSheet(u"border: none;\n"
        "color: rgb(220,220,220);")
                self.label_6.setAlignment(Qt.AlignCenter)

                self.verticalLayout_7.addWidget(self.label_6)

                self.label_8 = QLabel(self.frame_circle_2)
                self.label_8.setFont(font2)
                self.label_8.setStyleSheet(u"border: none;\n"
        "color: rgb(60, 231, 195);")
                self.label_8.setAlignment(Qt.AlignCenter)

                self.verticalLayout_7.addWidget(self.label_8)


                self.horizontalLayout_4.addWidget(self.frame_circle_2)

                self.frame_circle_3 = QFrame(self.frame_infos)
                self.frame_circle_3.setMinimumSize(QSize(250, 250))
                self.frame_circle_3.setMaximumSize(QSize(250, 250))
                self.frame_circle_3.setStyleSheet(u"QFrame{\n"
        "	border: 5px solid rgb(60, 231, 195);\n"
        "	border-radius: 125px;\n"
        "}\n"
        "QFrame:hover {\n"
        "	border: 5px solid rgb(105, 95, 148);\n"
        "}")
                self.frame_circle_3.setFrameShape(QFrame.StyledPanel)
                self.frame_circle_3.setFrameShadow(QFrame.Raised)
                self.verticalLayout_8 = QVBoxLayout(self.frame_circle_3)
                self.verticalLayout_8.setSpacing(10)
                self.verticalLayout_8.setObjectName(u"verticalLayout_8")
                self.label_9 = QLabel(self.frame_circle_3)
                self.label_9.setObjectName(u"label_9")
                self.label_9.setFont(font)
                self.label_9.setStyleSheet(u"border: none;\n"
        "color: rgb(60, 231, 195);")
                self.label_9.setAlignment(Qt.AlignCenter)

                self.verticalLayout_8.addWidget(self.label_9)

                self.label_10 = QLabel(self.frame_circle_3)
                self.label_10.setObjectName(u"label_10")
                self.label_10.setFont(font3)
                self.label_10.setStyleSheet(u"border: none;\n"
        "color: rgb(220,220,220);")
                self.label_10.setAlignment(Qt.AlignCenter)

                self.verticalLayout_8.addWidget(self.label_10)

                self.label_11 = QLabel(self.frame_circle_3)
                self.label_11.setObjectName(u"label_11")
                self.label_11.setFont(font2)
                self.label_11.setStyleSheet(u"border: none;\n"
        " color: rgb(128, 102, 168);")
                self.label_11.setAlignment(Qt.AlignCenter)

                self.verticalLayout_8.addWidget(self.label_11)

                self.horizontalLayout_4.addWidget(self.frame_circle_3)
                self.verticalLayout_9.addWidget(self.frame_infos)

                self.frame_texts = QFrame(self.frame_content_home)
                self.frame_texts.setMinimumSize(QSize(800, 0))
                self.frame_texts.setMaximumSize(QSize(16777215, 200))
                self.frame_texts.setFrameShape(QFrame.StyledPanel)
                self.frame_texts.setFrameShadow(QFrame.Raised)

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

                self.verticalLayout_p = QVBoxLayout()
                self.verticalLayout_p.setAlignment(Qt.AlignRight)
                self.verticalLayout_p.addWidget(self.high_speed)
                self.verticalLayout_p.addWidget(self.line_toSend)
                self.verticalLayout_p.addWidget(self.btn_send)

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

                self.horizontalLayout_p10 = QHBoxLayout(self.frame_texts)
                self.horizontalLayout_p10.setAlignment(Qt.AlignHCenter)
                self.horizontalLayout_p10.addLayout(self.verticalLayout_p3)
                self.horizontalLayout_p10.addLayout(self.verticalLayout_10)
                self.horizontalLayout_p10.addLayout(self.verticalLayout_M)


                self.verticalLayout_9.addWidget(self.frame_texts, 0, Qt.AlignHCenter)


                self.verticalLayout_5.addWidget(self.frame_content_home)

                self.verticalLayout_4.addWidget(self.page_home)

                self.verticalLayout.addWidget(self.content_bar)

                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)

                self.stackedWidget.setCurrentIndex(0)

                
                QMetaObject.connectSlotsByName(MainWindow)

        def open_new_window(self):
                self.serial.close()
                subprocess.run(['python','importsys2.py'])
                       
        ############################################################################################
        def readData(self):
                data = self.serial.readAll()
                data_str = str(data, encoding='utf-8')  #
                data_values = data_str.split(',')
                self.updatePlot(data_str)
        def updatePlot(self, data_str):
                self.x = 0
                #self.label_6.setText(data_str)
        def openSerialPort(self):
                global serial
                self.serial = QSerialPort()
                self.serial.setPortName(self.nameport)
                r = self.serial.open(QtCore.QIODevice.ReadWrite)
                if not r:
                        print('Port open error')
                else:
                        print('Port opened')
                        self.serial.setBaudRate(self.baudrate)
                        self.serial.setStopBits(QSerialPort.OneStop)
                        self.serial.setParity(QSerialPort.NoParity)
                        self.serial.setDataBits(QSerialPort.Data8)
                        self.serial.setFlowControl(QSerialPort.NoFlowControl)
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
                self.serial.readyRead.connect(self.readData)

        def stop(self):
                self.openSerialPort()
                self.serial.write("o".encode())
                QTimer.singleShot(1000, self.serial.close) 
                
        def start_timer(self, value):
                self.timer.stop()
                self.timer.setSingleShot(True)
                self.timer.timeout.connect(lambda: self.speed(value))
                self.timer.start(1000)  # Adjust this value as needed

        def speed(self,value):
                 #padded_value = str(value).zfill(3)
                self.serial.write("v".encode())
                text_to_send =  self.line_toSend.text()
                text_to_send =text_to_send.zfill(3)
                QTimer.singleShot(20, lambda:self.serial.write(text_to_send[0].encode())) 
                QTimer.singleShot(40, lambda:self.serial.write(text_to_send[1].encode())) 
                QTimer.singleShot(60, lambda:self.serial.write(text_to_send[2].encode())) 
                

        def auto(self):
                self.serial.write("a".encode())
                
        def retranslateUi(self, MainWindow):
                self.label.setText(QCoreApplication.translate("MainWindow", u"POSITION", None))
                #self.label_3.setText(QCoreApplication.translate("MainWindow", u"s", None))
                self.label_2.setText(QCoreApplication.translate("MainWindow", u"cm", None))
                self.label_5.setText(QCoreApplication.translate("MainWindow", u"VITESSE", None))                #self.label_7.setText(QCoreApplication.translate("MainWindow", u"RTX 2080 Ti", None))
                self.label_8.setText(QCoreApplication.translate("MainWindow", u"cm/s", None))
                self.label_9.setText(QCoreApplication.translate("MainWindow", u"Vitesse2", None))
                #self.label_10.setText(QCoreApplication.translate("MainWindow", u"8GB", None))
                self.label_11.setText(QCoreApplication.translate("MainWindow", u"tour/sec", None))

                
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    sys.exit(app.exec_())
