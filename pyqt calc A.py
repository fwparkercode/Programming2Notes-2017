import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the app layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(100, 100, 300, 200)


        # Make Widgets
        self.title = QLabel("Hypotenuse Calculator: ")
        self.title.setObjectName("title")
        self.grid.addWidget(self.title, 1, 1, 1, 1)

        self.image = QLabel("")
        self.grid.addWidget(self.image, 1, 2, 1, 1)

        pixmap = QPixmap('hypotenuse.png')
        pixmap = pixmap.scaledToWidth(180)
        self.image.setPixmap(pixmap)


        self.side1_label = QLabel("Length of side 1: ")
        self.grid.addWidget(self.side1_label, 2, 1, 1, 1)

        self.side1_value = QSpinBox()
        self.grid.addWidget(self.side1_value, 2, 2, 1, 1)

        self.side2_label = QLabel("Length of side 2: ")
        self.grid.addWidget(self.side2_label, 3, 1, 1, 1)

        self.side2_value = QSpinBox()
        self.grid.addWidget(self.side2_value, 3, 2, 1, 1)

        self.calc_button = QPushButton("Calculate")
        self.grid.addWidget(self.calc_button, 4, 1, 1, 1)

        self.answer_value = QLabel("0")
        self.grid.addWidget(self.answer_value, 4, 2, 1, 1)

        # Signals and slots
        self.calc_button.clicked.connect(self.calc_hypotenuse)
        self.set_style()
        self.show()

    def set_style(self):
        style_sheet = "pyqtstyleA.css"
        with open(style_sheet, "r") as f:
            self.setStyleSheet(f.read())

    def calc_hypotenuse(self):
        side1 = float(self.side1_value.text())
        side2 = float(self.side2_value.text())
        hyp = (side1 ** 2 + side2 ** 2) ** 0.5
        self.answer_value.setText(str(hyp))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())