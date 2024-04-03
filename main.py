import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import QTimer
import argparse
import time
import struct
import binascii
import numpy as np
import matplotlib.pyplot as plt
from bluepy.btle import UUID, Peripheral, ADDR_TYPE_PUBLIC, DefaultDelegate


def askFordatas():
    global x_data, y_data, z_data , t , counter ,old_time,first
    bleiot.waitForNotifications(args.t)
    label_accx.setText(str(data_accx))
    label_accy.setText(str(data_accy))
    label_accz.setText(str(data_accz))
    if (len(x_data))>=10:
        x_data = x_data[1:10]
        x_data.append(data_accx)
    else:
        x_data.append(data_accx)
    if len(y_data)>=10:
        y_data = y_data[1:10]
        y_data.append(data_accy)
    else:
        y_data.append(data_accy)
    if len(z_data)>=10:
        z_data = z_data[1:10]
        z_data.append(data_accz)
    else:
        z_data.append(data_accz)
        # Clear the existing plot
        
    if len(t)>=10:
            t = t[1:10]
            counter += time.time() - old_time
            old_time=time.time()
            t.append(counter)
    else :	
            old_time = time.time()
            if first == 1 : 
                counter = 0
                t.append(counter)
                old_time=time.time()
                first = 0 
            else :
                counter += time.time() - old_time
                old_time=time.time()
                t.append(counter)
                
        
    ax.clear()
    ax.plot(t,x_data, label='AccX',color='red')
    ax.plot(t,y_data, label='AccY',color='blue')
    ax.plot(t,z_data, label='AccZ',color='green')
    ax.legend()
    canvas.draw()
    if loop:
        QTimer.singleShot(0, askFordatas)

def stop_loop():
    global loop
    loop = 0
def start_loop():
    global loop
    loop = 1
    askFordatas()

app = QApplication(sys.argv)

w = QWidget()
w.resize(300,300)
w.setWindowTitle("Copy Example")

graph_layout = QVBoxLayout(w)
fig, ax = plt.subplots()
canvas = fig.canvas
canvas.setFixedSize(1500, 900)
graph_layout.addWidget(canvas)
canvas.move(0,0)

label_accx1 = QLabel(w)
#label_accx1.setStyleSheet("border: 2px solid black; padding: 10px;")
label_accx1.move(1600,100)
label_accx1.setText("x:")
label_accx = QLabel(w)
label_accx.move(1630,100)
label_accx.setText("x")
label_accy1 = QLabel(w)
label_accy1.move(1600,200)
label_accy1.setText("y:")
label_accy = QLabel(w)
label_accy.move(1630,200)
label_accy.setText("y")
label_accz1 = QLabel(w)
label_accz1.move(1600,300)
label_accz1.setText("z:")
label_accz = QLabel(w)
label_accz.move(1630,300)
label_accz.setText("z")
btn = QPushButton(w)
btn.move(1600,400)
btn.setFixedSize(200,50)
btn.setText('Start')
btn.clicked.connect(start_loop)
btn_stop = QPushButton(w)
btn_stop.move(1600,500)
btn_stop.setFixedSize(200,50)
btn_stop.setText('Stop')
btn_stop.clicked.connect(stop_loop)



time.sleep(2.0)   

w.show()
sys.exit(app.exec_())