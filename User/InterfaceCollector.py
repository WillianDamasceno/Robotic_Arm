from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
qtProgram = uic.loadUi("Interface.ui")

qtProgram.show()
app.exec()
