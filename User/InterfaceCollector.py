"""
Para converter .py para .exe:

    Com tela preta:
    cmd: pyintaller -F fileName.py

    Sem tela preta:
    cmd: pyinstaller --windowed -F fileName.py

    Com icon, basta escrever o seguinte antes de -F:
    -i "iconName.ico"

Para converter .ui para .py:
    cmd: pyuic5 -x fileName.ui -o fileName.py

"""

from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtGui import QIcon

from time import sleep
import serial
import sys
import os


def validationChacker():
    if len(arduino.readline()) == 11:
        print('\033[1;32mAvailable!\033[m')
        return True
    else:
        print('\033[1;31mUnavailable!\033[m')
        return False


def movementTextSender(letter='', msg=''):
    print(msg)
    if validationChacker():
        movementLetter = bytes(letter, 'utf-8')
        arduino.write(movementLetter)
        sleep(0.0001) # test
        arduino.write('unavailable')# test


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(f"{os.path.dirname(os.path.realpath(__file__))}\\UserInterface.ui", self)

        # Configurando a interface
        self.setWindowTitle('Robotic Arm')
        self.resize(500, 270)
        # self.setWindowIcon(QIcon("static\\logo.ico"))

        # Definindo os botões de movimentos pré programados
        self.movement1_button = self.findChild(QPushButton, 'Movement1')
        self.movement1_button.clicked.connect(self.movement1)

        self.movement2_button = self.findChild(QPushButton, 'Movement2')
        self.movement2_button.clicked.connect(self.movement2)

        self.movement3_button = self.findChild(QPushButton, 'Movement3')
        self.movement3_button.clicked.connect(self.movement3)

        self.movement4_button = self.findChild(QPushButton, 'Movement4')
        self.movement4_button.clicked.connect(self.movement4)

        self.movement5_button = self.findChild(QPushButton, 'Movement5')
        self.movement5_button.clicked.connect(self.movement5)

        self.movement6_button = self.findChild(QPushButton, 'Movement6')
        self.movement6_button.clicked.connect(self.movement6)
        # Botões pré programados finalizados

        # Definindo os botões de movimentos independentes
        self.toTheRight_button = self.findChild(QPushButton, 'Right')
        self.toTheRight_button.clicked.connect(self.toTheRight)

        self.toTheLeft_button = self.findChild(QPushButton, 'Left')
        self.toTheLeft_button.clicked.connect(self.toTheLeft)
        # Botões de movimentos independentes finalizados

        self.show()

    # Definindo as funções de cada botão de movimento pré programado
    def movement1(self):
        movementTextSender('a', '\nMovement 1:')
    
    def movement2(self):
        movementTextSender('b', '\nMovement 2:')
    
    def movement3(self):
        movementTextSender('c', '\nMovement 3:')
    
    def movement4(self):
        movementTextSender('d', '\nMovement 4:')
    
    def movement5(self):
        movementTextSender('e', '\nMovement 5:')
    
    def movement6(self):
        movementTextSender('f','\nMovement 6:')
    # Definições das funções finalizadas

    # Definindo as funções de cada botão de movimento independente
    def toTheRight(self):
        movementTextSender('g', '\nMoving to the right')
    
    def toTheLeft(self):
        movementTextSender('h', '\nMoving to the left')
    # Definições das funções finalizadas


arduino = serial.Serial('COM4', baudrate=9600, timeout=1)
sleep(3)

app = QApplication(sys.argv)
UIWindow = UI()
sys.exit(app.exec_())
