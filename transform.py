from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import home, red, yellow, green

ui = ''
app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()

def mainUi():
    global ui
    ui = home.Ui_homeUI()
    ui.setupUi(mainWindow)
    ui.button_red.clicked.connect(redUi)
    ui.button_yellow.clicked.connect(yellowUi)
    ui.button_green.clicked.connect(greenUi)
    mainWindow.show()

def redUi():
    global ui
    ui = red.Ui_redUI()
    ui.setupUi(mainWindow)
    ui.buttonBack.clicked.connect(mainUi)
    mainWindow.show()

def yellowUi():
    global ui
    ui = yellow.Ui_yellowUI()
    ui.setupUi(mainWindow)
    ui.buttonBack.clicked.connect(mainUi)
    mainWindow.show()

def greenUi():
    global ui
    ui = green.Ui_greenUI()
    ui.setupUi(mainWindow)
    ui.buttonBack.clicked.connect(mainUi)
    mainWindow.show()

mainUi()
sys.exit(app.exec_())

