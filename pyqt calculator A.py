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
        self.setGeometry(10, 10, 300, 500)

        # Widgets
        self.answer = QLabel("0")
        self.grid.addWidget(self.answer, 1, 1, 3, 1)

        self.button1 = QPushButton("1")
        self.grid.addWidget(self.button1, 2, 1, 1, 1)

        self.button2 = QPushButton("2")
        self.grid.addWidget(self.button2, 2, 2, 1, 1)

        self.button_add = QPushButton("+")
        self.grid.addWidget(self.button_add, 2, 3, 1, 1)

        self.button_equal = QPushButton("=")
        self.grid.addWidget(self.button_equal, 3, 1, 1, 1)


        # Signals and Slots
        self.button1.clicked.connect(lambda: self.concat("1 "))
        self.button2.clicked.connect(lambda: self.concat("2 "))
        self.button_add.clicked.connect(lambda: self.equation("+ "))
        self.button_equal.clicked.connect(self.equation_eval)
        self.button_equal.setObjectName("equal")

        # Style
        style_sheet = "calc_style.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())

        # Draw
        self.show()

    def concat(self, value):
        self.equation += value
        self.answer.setText(self.equation)
    def equation_eval(self):
        self.answer.setText(str(eval(self.equation)))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())