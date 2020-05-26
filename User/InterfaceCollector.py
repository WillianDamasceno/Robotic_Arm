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


def validationChacker():
    validation = open('User\\movement.txt', 'r')

    if validation.readline() == 'available':
        validation.seek(0)
        validation.close()
        print('\033[1;32mAvailable!\033[m')
        return True

    else:
        validation.seek(0)
        validation.close()
        print('\033[1;31mUnavailable!\033[m')
        return False


def movementTextSender(text=''):
    
    if validationChacker():
        validation = open('User\\movement.txt', 'w')
        validation.write('unavailable')
        validation.close()

        movementLetter = bytes(text, 'utf-8')
        arduino.write(movementLetter)


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("User\\UserInterface.ui", self)

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
        print('\nMovement 1:')
        movementTextSender('a')
    
    def movement2(self):
        print('\nMovement 2:')
        movementTextSender('b')
    
    def movement3(self):
        print('\nMovement 3:')
        movementTextSender('c')
    
    def movement4(self):
        print('\nMovement 4:')
        movementTextSender('d')
    
    def movement5(self):
        print('\nMovement 5:')
        movementTextSender('e')
    
    def movement6(self):
        print('\nMovement 6:')
        movementTextSender('f')
    # Definições das funções finalizadas

    # Definindo as funções de cada botão de movimento independente
    def toTheRight(self):
        print('\nMoving to the right')
        movementTextSender('g')
    
    def toTheLeft(self):
        print('\nMoving to the left')
        movementTextSender('h')
    # Definições das funções finalizadas


arduinoConnection = False
arduino = serial.Serial('COM4', baudrate=9600, timeout=1)

validation = open('User\\movement.txt', 'w')
validation.write('available')
validation.close()

sleep(3)

app = QApplication(sys.argv)
UIWindow = UI()
sys.exit(app.exec_())
