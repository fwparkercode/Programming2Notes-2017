import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.equation = ""

        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(10,10,300,500)

        # Widgets
        self.display = QLabel("0")
        self.grid.addWidget(self.display, 1, 1, 1, 3)

        self.button1 = QPushButton("1")
        self.grid.addWidget(self.button1, 2, 1, 1, 1)

        self.button2 = QPushButton("2")
        self.grid.addWidget(self.button2, 2, 2, 1, 1)

        self.button_add = QPushButton("+")
        self.grid.addWidget(self.button_add, 2, 3, 1, 1)

        self.button_equal = QPushButton("=")
        self.grid.addWidget(self.button_equal, 3, 3, 1, 1)

        # Signals and Slots
        self.button1.clicked.connect(lambda: self.concat("1"))
        self.button2.clicked.connect(lambda: self.concat("2"))
        self.button_add.clicked.connect(lambda: self.concat("+"))
        self.button_equal.clicked.connect(self.equal)

        # Style

        # Draw
        self.show()
    def concat(self, val):
        self.equation += val
        self.display.setText(self.equation)
    def equal(self):
        self.equation = str(eval(self.equation))
        self.display.setText(self.equation)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())