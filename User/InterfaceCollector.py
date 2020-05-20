from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"User\UserInterface.ui", self)

        self.movement1_button = self.findChild(QPushButton, "Movement1")
        self.movement1_button.clicked.connect(self.movement1)

        self.movement2_button = self.findChild(QPushButton, "Movement2")
        self.movement2_button.clicked.connect(self.movement2)

        self.movement3_button = self.findChild(QPushButton, "Movement3")
        self.movement3_button.clicked.connect(self.movement3)

        self.movement4_button = self.findChild(QPushButton, "Movement4")
        self.movement4_button.clicked.connect(self.movement4)

        self.movement5_button = self.findChild(QPushButton, "Movement5")
        self.movement5_button.clicked.connect(self.movement5)

        self.movement6_button = self.findChild(QPushButton, "Movement6")
        self.movement6_button.clicked.connect(self.movement6)

        self.show()
    
    def movement1(self):

        print("Movement 1")
        chosenMovement = open(r'User\movement.txt', 'w')
        chosenMovement.write('a')
        chosenMovement.close()
    
    def movement2(self):
        print("Movement 2")
        chosenMovement = open(r'User\movement.txt', 'w')
        chosenMovement.write('b')
        chosenMovement.close()
    
    def movement3(self):
        print("Movement 3")
        chosenMovement = open(r'User\movement.txt', 'w')
        chosenMovement.write('c')
        chosenMovement.close()
    
    def movement4(self):
        print("Movement 4")
        chosenMovement = open(r'User\movement.txt', 'w')
        chosenMovement.write('d')
        chosenMovement.close()
    
    def movement5(self):
        print("Movement 5")
        chosenMovement = open(r'User\movement.txt', 'w')
        chosenMovement.write('e')
        chosenMovement.close()
    
    def movement6(self):
        print("Movement 6")
        chosenMovement = open(r'User\movement.txt', 'w')
        chosenMovement.write('f')
        chosenMovement.close()
    

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
