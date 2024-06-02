import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
import math
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

nameport = 'COM15'
baudrate = 115200
serial = None
last_command = None
last_command_1 = None
add = 0
last_angle = 0
commands = []  # List to store commands
timedelay = 0
def moveup():
    commands.append("z")
    print("Command: move up")

def movedown():
    commands.append("s")
    print("Command: move down")

def moveright():
    commands.append("d")
    print("Command: move right")

def moveleft():
    commands.append("q")
    print("Command: move left")

def start():
    commands.append("m")
    print("Command: start")

def stop():
    commands.append("o")
    print("Command: stop")

def low():
    commands.append("l")
    print("Command: low")

def high():
    commands.append("h")
    print("Command: high")

def auto():
    commands.append("a")
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

def handle_angle_neg_90(angle_degrees):
    global last_command, last_angle
    if last_command == "right":
        last_command = "next_upr"
        angle = abs(angle_degrees - last_angle)
        delay = str(int(1050 * angle / 90)).zfill(4)
        commands.append("t")
        commands.extend(list(delay))
        print("Command: right turn")
    elif last_command == "left":
        last_command = "next_upl"
        angle = abs(angle_degrees - last_angle)
        delay = str(int(1050 * angle / 90)).zfill(4)
        commands.append("e")
        commands.extend(list(delay))
        print("Command: left turn")
    else:
        commands.append("a")
        last_command = "up"
    last_angle = angle_degrees

def handle_angle_neg_90_to_neg_180_or_180(angle_degrees):
    global last_command, last_angle
    if last_command == "up":
        last_command = "next_right"
        angle = abs(angle_degrees - last_angle)
        delay = str(int(1050 * angle / 90)).zfill(4)
        commands.append("t")
        commands.extend(list(delay))
        print("Command: right turn")
    elif last_command == "next_right":
        commands.append("a")
        last_command = "right"
    last_angle = angle_degrees

def handle_angle_0_to_neg_90(angle_degrees):
    global last_command, last_angle
    if last_command == "up":
        last_command = "next_left"
        angle = abs(angle_degrees - last_angle)
        delay = str(int(1050 * angle / 90)).zfill(4)
        commands.append("e")
        commands.extend(list(delay))
        print("Command: left turn")
    elif last_command == "next_left":
        commands.append("a")
        last_command = "left"
    last_angle = angle_degrees

def mouseReleaseEvent(e):
    global last_x, last_y, path, add, last_command, last_command_1, commands, last_angle ,timedelay
    commands = []
    timedelay = 0
    last_angle = 0
    last_x = None
    last_y = None
    commands.append("p")
    print("Command: p")
    # Print the path coordinates
    print("Path coordinates:", path)
    add = 0  # Reset add for each new path

    for i in range(0, len(path) - 5, 5):
        x = path[i][0]
        y = path[i][1]
        x_2 = path[i + 5][0]
        y_2 = path[i + 5][1]
        dx = x_2 - x
        dy = y_2 - y
        angle_radians = math.atan2(dy, dx)
        angle_degrees = math.degrees(angle_radians)

        if angle_degrees == -90:
            handle_angle_neg_90(angle_degrees)
        elif -180 <= angle_degrees <= -90 or angle_degrees == 180:
            handle_angle_neg_90_to_neg_180_or_180(angle_degrees)
        elif 0 >= angle_degrees > -90:
            handle_angle_0_to_neg_90(angle_degrees)

    commands.append("l")  # Add "l" at the end
    print("All commands:", commands)
    send_commands()

def send_commands():

    global timedelay
    if commands:
        command = commands.pop(0)
        print(f"Sending command: {command}")
        if serial and serial.isOpen():
            serial.write(command.encode())
            print(f"Sent command: {command}")
        else:
            print(f"Serial port is not open or not available")
        
        QTimer.singleShot(1000, send_commands)  # Call send_commands() after 100 ms


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
