import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton

app = QApplication(sys.argv)

label = QLabel("label")
button = QPushButton("button")

def buttonClickCallback():
    print("clicked button")

button.clicked.connect(buttonClickCallback)
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

mainWindow = QWidget()
mainWindow.setLayout(layout)
mainWindow.show()

sys.exit(app.exec())