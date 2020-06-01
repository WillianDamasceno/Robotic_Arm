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
        self.movement1_button.clicked.connect(lambda: self.movementTextSender('a', '\nMovement 1'))

        self.movement2_button = self.findChild(QPushButton, 'Movement2')
        self.movement2_button.clicked.connect(lambda: self.movementTextSender('b', '\nMovement 2:'))

        self.movement3_button = self.findChild(QPushButton, 'Movement3')
        self.movement3_button.clicked.connect(lambda: self.movementTextSender('c', '\nMovement 3:'))

        self.movement4_button = self.findChild(QPushButton, 'Movement4')
        self.movement4_button.clicked.connect(lambda: self.movementTextSender('d', '\nMovement 4:'))

        self.movement5_button = self.findChild(QPushButton, 'Movement5')
        self.movement5_button.clicked.connect(lambda: self.movementTextSender('e', '\nMovement 5:'))

        self.movement6_button = self.findChild(QPushButton, 'Movement6')
        self.movement6_button.clicked.connect(lambda: self.movementTextSender('f', '\nMovement 6:'))
        # Botões pré programados finalizados

        # Definindo os botões de movimentos independentes
        self.toTheRight_button = self.findChild(QPushButton, 'Right')
        # self.toTheRight_button.setCheckable(True)
        # self.totheRight_button.toggle()
        self.toTheRight_button.clicked.connect(lambda: self.movementTextSender('g', '\nMoving to the right'))

        self.toTheLeft_button = self.findChild(QPushButton, 'Left')
        # self.toTheLeft_button.setCheckable(True)
        # self.toTheLeft_button.toggle()
        self.toTheLeft_button.clicked.connect(lambda: self.movementTextSender('h', '\nMoving to the left'))

        self.downS2_button = self.findChild(QPushButton, 'DownS2')
        # self.downS2_button.setCheckable(True)
        # self.downS2_button.toggle()
        self.downS2_button.clicked.connect(lambda: self.movementTextSender('i', '\nServo 2 going down:'))

        self.upS2_button = self.findChild(QPushButton, 'UpS2')
        # self.upS2_button.setCheckable(True)
        # self.upS2_button.toggle()
        self.upS2_button.clicked.connect(lambda: self.movementTextSender('j', '\nServo 2 going up:'))

        self.downS3_button = self.findChild(QPushButton, 'DownS3')
        # self.downS3_button.setCheckable(True)
        # self.downS3_button.toggle()
        self.downS3_button.clicked.connect(lambda: self.movementTextSender('k', '\nServo 3 going down:'))

        self.upS3_button = self.findChild(QPushButton, 'UpS3')
        # self.upS3_button.setCheckable(True)
        # self.upS3_button.toggle()
        self.upS3_button.clicked.connect(lambda: self.movementTextSender('l', '\nServo 3 going up:'))
        # Botões de movimentos independentes finalizados

        self.show()

    def movementTextSender(self, movementLetter, msg):
        print(msg)

        '''if self.movement1_button.isChecked():
            print("button pressed")
        else:
            print("button released")'''
        
        validation = len(arduino.readline())
        if validation == 11:
            arduino.write(bytes(movementLetter, 'utf-8'))
            print('\033[1;32mAvailable!\033[m')
        else:
            print('\033[1;31mUnavailable!\033[m')


arduino = serial.Serial('COM4', baudrate=9600, timeout=1)
sleep(3)

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

print('Testing')
