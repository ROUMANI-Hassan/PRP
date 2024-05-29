import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
import math
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

nameport = '/dev/ttyUSB0'
baudrate = 115200
serial = None
last_command = None
last_command_1 = None
add = 0

def moveup():
    serial.write("z".encode())
    print("Command: move up")

def movedown():
    serial.write("s".encode())
    print("Command: move down")

def moveright():
    serial.write("d".encode())
    print("Command: move right")

def moveleft():
    serial.write("q".encode())
    print("Command: move left")

def start():
    serial.write("m".encode())
    print("Command: start")

def stop():
    serial.write("o".encode())
    print("Command: stop")

def low():
    serial.write("l".encode())
    print("Command: low")

def high():
    serial.write("h".encode())
    print("Command: high")

def auto():
    serial.write("a".encode())
    print("Command: auto")

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

def mouseMoveEvent(e):
    global last_x, last_y, path
    if last_x is None:  # First event.
        last_x = e.x()
        last_y = e.y()
        return  # Ignore the first time.

    # Append the new coordinates to the path
    path.append((e.x(), e.y()))

    painter = QtGui.QPainter(label.pixmap())
    painter.drawLine(last_x, last_y, e.x(), e.y())
    painter.end()
    label.update()

    # Update the origin for next time.
    last_x = e.x()
    last_y = e.y()

def mouseReleaseEvent(e):
    global last_x, last_y, path, add, last_command  , last_command_1
    last_x = None
    last_y = None

    # Print the path coordinates
    print("Path coordinates:", path)
    add = 0  # Reset add for each new path
    for i in range(0, len(path) - 1, 5):
        
        x = path[i][0]
        y = path[i][1]
        x_2 = path[i + 1][0]
        y_2 = path[i + 1][1]
        dx = x_2 - x
        dy = y_2 - y
        angle_radians = math.atan2(dy, dx)
        angle_degrees = math.degrees(angle_radians)

        if angle_degrees == -90:
            
            if last_command_1 == "right":
                last_command_1 = "next_up"
            elif last_command_1 == "next_upr":
                last_command_1="up"
            elif last_command_1 == "left":
                last_command_1 = "next_up" 
            elif last_command_1 == "next_upl":
                last_command_1="up" 
            elif last_command_1 == "up":
                pass    
            else :
                last_command_1 = "up"
                add += 800
        elif angle_degrees >= 180:
            speed = 
            if last_command_1 == "up":
                last_command_1 = "next_right"
            elif last_command_1 == "next_right":
                last_command_1 = "right"
                add += 800
                
        elif angle_degrees == 0:
            if last_command_1 == "up":
                last_command_1 = "next_left"
            elif last_command_1 == "next_left":
                last_command_1 = "left"
                add += 800
                
        timer = 400 * (i // 5) + add
        QTimer.singleShot(timer, lambda i=i: handle_movement(i))  # Delayed movement
    

def handle_movement(i):
    global add, last_command
    x = path[i][0]
    y = path[i][1]
    x_2 = path[i + 1][0]
    y_2 = path[i + 1][1]
    dx = x_2 - x
    dy = y_2 - y
    angle_radians = math.atan2(dy, dx)
    angle_degrees = math.degrees(angle_radians)
    print(f"Handling movement {i}: angle {angle_degrees}, last_command {last_command}")

    if angle_degrees == -90:
        if last_command == "right":
            last_command = "next_upr"
            serial.write("t".encode())
            print("Command: right turn")
        elif last_command == "next_upr":
            last_command="up"
        elif last_command == "left":
            last_command = "next_upl"
            serial.write("e".encode())
            print("Command: left turn")
        elif last_command == "next_upl":
            last_command="up"
        elif last_command == "up":
            pass        
        else :
            moveup()
            last_command = "up"

    elif angle_degrees == 180:
        if last_command == "up":
            last_command = "next_right"
            serial.write("e".encode())
            print("Command: right turn")
        elif last_command == "next_right":
            moveup()
            last_command = "right"

    elif angle_degrees == 0:
        if last_command == "up":
            last_command = "next_left"
            serial.write("t".encode())
            print("Command: left turn")
        elif last_command == "next_left":
            moveup()
            last_command = "left"

    if i >= len(path)-5 :  # If this is the last movement
        QTimer.singleShot(400 * (i // 5) + add, lambda: serial.write("b".encode()))
        print("Command: stop (b)")
        last_command = None
        path.clear()  # Clear the path

app = QtWidgets.QApplication(sys.argv)

label = QtWidgets.QLabel()
canvas = QtGui.QPixmap(400, 300)
canvas.fill(Qt.white)
label.setPixmap(canvas)
last_x, last_y = None, None
path = []

openSerialPort()

label.mouseMoveEvent = mouseMoveEvent
label.mouseReleaseEvent = mouseReleaseEvent

label.show()
sys.exit(app.exec_())