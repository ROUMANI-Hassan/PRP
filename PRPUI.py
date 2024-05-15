import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtSerialPort import QSerialPort
from PyQt5 import QtCore
import pyqtgraph as pg

nameport = '/dev/ttyUSB0'
baudrate = 115200
serial = QSerialPort()
def readData():
    global serial
    data = serial.readAll()
    data_str = str(data, encoding='utf-8')  # Convert QByteArray to string
    data_values = data_str.split(',')       # Split string into individual values

    if len(data_values) >= 2:
        updatePlot(data_values)
serial.readyRead.connect(readData)
def moveup():
    global last_state
    serial.write("z".encode())
    last_state = "z"

def movedown():
    global last_state
    serial.write("s".encode())
    last_state = "s"

def moveright():
    global last_state
    serial.write("d".encode())
    last_state = "d"

def moveleft():
    global last_state
    serial.write("q".encode())
    last_state = "q"

def start():
    serial.write("m".encode())

def low():
    serial.write("l".encode())

def high():
    serial.write("h".encode())

def auto():
    serial.write("a".encode())

def keyPressEvent(event):
    key = event.key()
    if key == QtCore.Qt.Key_Y:
        moveup()
    elif key == QtCore.Qt.Key_H:
        movedown()
    elif key == QtCore.Qt.Key_G:
        moveleft()
    elif key == QtCore.Qt.Key_J:
        moveright()
    elif key == QtCore.Qt.Key_B:
        start()
    elif key == QtCore.Qt.Key_L:
        low()
    elif key == QtCore.Qt.Key_M:
        high()
    elif key == QtCore.Qt.Key_A:
        auto()

app = QApplication(sys.argv)
prp_ui = QWidget()
prp_ui.setWindowTitle("Projet Pluridisciplinaire")

if not serial.setPortName(nameport):
    print('Port open error')
else:
    print('Port opened')
    serial.setBaudRate(baudrate)
    serial.setStopBits(QSerialPort.OneStop)
    serial.setParity(QSerialPort.NoParity)
    serial.setDataBits(QSerialPort.Data8)
    serial.setFlowControl(QSerialPort.NoFlowControl)
    serial.open(QtCore.QIODevice.ReadWrite)

# Plot Initialization
graphWidget = pg.PlotWidget()
graphWidget.setFixedSize(1500, 1000)
curve = graphWidget.plot(pen='y')  # Assuming you want a yellow curve

graph_layout = QVBoxLayout(prp_ui)
graph_layout.addWidget(graphWidget)



def updatePlot(data_values):
    # Parse data and update plot
    x = float(data_values[0])  # Assuming the first value is x
    y = float(data_values[1])  # Assuming the second value is y
    
    # Update plot with new data point
    curve.setData([x], [y])

timer = QtCore.QTimer()
timer.timeout.connect(readData)
timer.start(50)  # Adjust this value based on your data update rate

# Button Creation
start_button = QPushButton(prp_ui)
start_button.setText("Start")
start_button.move(1700, 200)
start_button.setFixedSize(200, 50)
start_button.clicked.connect(start)

# Other buttons...

prp_ui.show()
sys.exit(app.exec_())
