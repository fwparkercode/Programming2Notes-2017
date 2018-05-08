import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(10, 10, 300, 200)

        # Widgets
        self.title = QLabel("Hypotenuse Calculator:")
        self.grid.addWidget(self.title, 1, 1, 2, 1)
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignCenter)

        self.labelA = QLabel("Length of Side A:")
        self.grid.addWidget(self.labelA, 2, 1, 1, 1)

        self.labelB = QLabel("Length of Side B:")
        self.grid.addWidget(self.labelB, 3, 1, 1, 1)

        self.sideA = QLineEdit()
        self.grid.addWidget(self.sideA, 2, 2, 1, 1)

        self.sideB = QLineEdit()
        self.grid.addWidget(self.sideB, 3, 2, 1, 1)

        self.calc = QPushButton("Calculate")
        self.grid.addWidget(self.calc, 4, 1, 1, 1)

        self.answer = QLabel("0")
        self.grid.addWidget(self.answer, 4, 2, 1, 1)

        # Signals/Slots
        self.calc.clicked.connect(self.find_hyp)

        # Set Style
        self.set_style()

        # Draw
        self.show()

    def set_style(self):
        style_sheet = "pyqt calc B.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())

    def find_hyp(self):
        a = float(self.sideA.text())
        b = float(self.sideB.text())
        c = (a ** 2 + b ** 2) ** 0.5
        self.answer.setText(str(c))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())
