import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
import math
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

nameport = 'com8'
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
    
def angle_between_points(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    v1 = (x2 - x1, y2 - y1)
    v2 = (x3 - x2, y3 - y2)
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    magnitude_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    cos_theta = dot_product / (magnitude_v1 * magnitude_v2)
    return math.degrees(math.acos(cos_theta))
def mouseReleaseEvent(e):
    global path, commands
    commands = []
    commands.append("p")  # Command to start painting
    print("Command: p")

    # Print the path coordinates
    print("Path coordinates:", path)

    for i in range(0, len(path) - 4, 5):  # Loop through the path with a step of 5
        avg_angle_sum = 0

        for j in range(i, i + 4):  # Calculate the sum of angles for the current segment
            x = path[j][0]
            y = path[j][1]
            x_2 = path[j + 1][0]
            y_2 = path[j + 1][1]
            dx = x_2 - x
            dy = y_2 - y
            angle_radians = math.atan2(dy, dx)
            angle_degrees = math.degrees(angle_radians)
            avg_angle_sum += angle_degrees

        average_angle = avg_angle_sum / 5  # Calculate the average angle for the segment
        print("Average angle:", average_angle)

        # Determine the appropriate commands based on the average angle
        if abs(average_angle) < 30:  # Straight line tolerance
            commands.extend("a")  # Move forward (send "a")
        else:
            if average_angle >= 0:  # Right turn
                commands.append("t")  # Rotate right
            else:  # Left turn
                commands.append("e")  # Rotate left

    commands.append("l")  # Command to stop painting
    print("All commands:", commands)
    send_commands()





def send_commands():
    global commands
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