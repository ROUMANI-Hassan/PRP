import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
import math
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

nameport = '/dev/ttyUSB0'
baudrate = 115200
serial = None

commands = []
points = []

distance_tolerance = 50
scaling_factor = 2

def moveup():
    commands.append("z")
    print("Command: move up")

def right_turn():
    commands.append("e")
    print("Command: right turn")

def left_turn():
    commands.append("t")
    print("Command: left turn")

def move_forward(steps):
    for _ in range(steps):
        commands.append("a")
    print(f"Command: move forward {steps} steps")

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

def mousePressEvent(e):
    global points
    x, y = e.x(), e.y()
    points.append((x, y))
    
    painter = QtGui.QPainter(label.pixmap())
    painter.setPen(QtCore.Qt.red)
    painter.drawEllipse(x - 2, y - 2, 4, 4)
    
    if len(points) > 1:
        painter.setPen(QtCore.Qt.blue)
        painter.drawLine(points[-2][0], points[-2][1], points[-1][0], points[-1][1])
        
    painter.end()
    label.update()
    
    print(f"Point added: ({x}, {y})")

def calculate_angle(p1, p2, p3):
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p2[0], p3[1] - p2[1])
    
    angle1 = math.atan2(v1[1], v1[0])
    angle2 = math.atan2(v2[1], v2[0])
    
    angle_degrees = math.degrees(angle2 - angle1)
    if angle_degrees < 0:
        angle_degrees += 360
    
    return angle_degrees

def calculate_distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    distance = math.sqrt(dx**2 + dy**2)
    return distance

def generateCommands(end_command='l'):
    global points, commands
    commands = ['p']

    if len(points) < 2:
        print("Not enough points to generate commands.")
        return

    for i in range(len(points) - 1):
        distance = calculate_distance(points[i], points[i + 1])
        steps = int((distance / distance_tolerance) * scaling_factor)
        move_forward(steps)
        
        if i < len(points) - 2:
            angle_degrees = calculate_angle(points[i], points[i+1], points[i+2])
            print(f"Angle between points {i}, {i+1}, {i+2}: {angle_degrees}")
            turns = int(round(angle_degrees / 30))
            
            if angle_degrees <= 180:
                for _ in range(turns):
                    right_turn()
            else:
                turns = int(round((360 - angle_degrees) / 30))
                for _ in range(turns):
                    left_turn()
    
    commands.append(end_command)
    sendCommands()

def sendCommands():
    global commands
    if commands:
        command = commands.pop(0)
        print(f"Sending command: {command}")
        if serial and serial.isOpen():
            serial.write(command.encode())
            print(f"Sent command: {command}")
        else:
            print(f"Serial port is not open or not available")
        if commands:
            QTimer.singleShot(800, sendCommands)
    else:
        print("All commands sent.")

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout(window)

label = QtWidgets.QLabel()
canvas = QtGui.QPixmap(400, 300)
canvas.fill(Qt.white)
label.setPixmap(canvas)
label.setFixedSize(400, 300)
layout.addWidget(label)

button_go = QtWidgets.QPushButton("Normal Mode")
button_go_r = QtWidgets.QPushButton("Patrol Mode")
button_stop = QtWidgets.QPushButton("Stop")

layout.addWidget(button_go)
layout.addWidget(button_go_r)
layout.addWidget(button_stop)

button_go.clicked.connect(lambda: generateCommands('l'))
button_go_r.clicked.connect(lambda: generateCommands('r'))
button_stop.clicked.connect(lambda: stop())

def stop():
    serial.write('o'.encode())
    global label, canvas, points
    if label is not None:
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        label.setPixmap(canvas)
        points = []
openSerialPort()

label.mousePressEvent = mousePressEvent

window.show()
sys.exit(app.exec_())