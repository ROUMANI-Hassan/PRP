import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout , QGridLayout
from PyQt5.QtCore import QTimer
import numpy as np
import matplotlib.pyplot as plt
import time



app = QApplication(sys.argv)
prp_ui = QWidget()
prp_ui.setWindowTitle("Projet Pluridisciplinaire")



graph_layout = QVBoxLayout(prp_ui)
figure , axe = plt.subplots()
canvas = figure.canvas
graph_layout.addWidget(canvas)


start_button = QPushButton(prp_ui)
start_button.setText("Start")
start_button.setFixedSize(200,50)
move_up = QPushButton(prp_ui)
move_up.setText("UP")
move_up.move(1500,1500)
move_up.setFixedSize(200,50)
move_up.move(1500,1800)
move_down = QPushButton(prp_ui)
move_down.setText("DOWN")
move_down.setFixedSize(200,50)
move_right = QPushButton(prp_ui)
move_right.setText("RIGHT")
move_right.setFixedSize(200,50)
move_left = QPushButton(prp_ui)
move_left.setText("LEFT")
move_left.setFixedSize(200,50)

prp_ui.show()
sys.exit(app.exec_())