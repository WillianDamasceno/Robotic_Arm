from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
import sys
import os

def validationChacker():
    checker = open(r'User\movement.txt', 'r')
    
    if checker.read() == 'available':
        return True
    else:
        return False
    
    checker.close()


def movementTextSender(text=''):
    chosenMovement = open(r'User\movement.txt', 'w')
    chosenMovement.write(text)
    chosenMovement.close()


def buttonListener(movementLetter=''):
    optionAvailable = validationChacker()

    if optionAvailable:
        movementTextSender(movementLetter)
        os.startfile(r'Arm\ArmController.py')

        print('\033[1;32mAvailable!\033[m')

    else:
        print('\033[1;31mUnavailable!\033[m')


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"User\UserInterface.ui", self)

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

        ################################################################

        # Definindo os botões de movimentos independentes
        self.toTheRight_button = self.findChild(QPushButton, 'Right')
        self.toTheRight_button.clicked.connect(self.toTheRight)

        self.toTheLeft_button = self.findChild(QPushButton, 'Left')
        self.toTheLeft_button.clicked.connect(self.toTheLeft)
        # Botões de movimentos independentes finalizados

        self.show()
    
    ################################################################

    # Definindo as funções de cada botão de movimento pré programado
    def movement1(self):
        print('\nMovement 1:')
        buttonListener('a')
    
    def movement2(self):
        print('\nMovement 2:')
        buttonListener('b')
    
    def movement3(self):
        print('\nMovement 3:')
        buttonListener('c')
    
    def movement4(self):
        print('\nMovement 4:')
        buttonListener('d')
    
    def movement5(self):
        print('\nMovement 5:')
        buttonListener('e')
    
    def movement6(self):
        print('\nMovement 6:')
        buttonListener('f')
    # Definições das funções finalizadas

    ##############################################################

    # Definindo as funções de cada botão de movimento independente
    def toTheRight(self):
        optionAvailable = validationChacker()

        if optionAvailable:
            print('Moving to the right')
            
            movementTextSender('Untitled')

            os.startfile(r'Arm\ArmController.py')
        else:
            print('\033[1;31mUnavailable!\033[m')
    
    def toTheLeft(self):
        optionAvailable = validationChacker()

        if optionAvailable:
            print('Moving to the left')
            
            movementTextSender('Untitled')

            os.startfile(r'Arm\ArmController.py')
        else:
            print('\033[1;31mUnavailable!\033[m')
    # Definições das funções finalizadas


movementTextSender('available')

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
