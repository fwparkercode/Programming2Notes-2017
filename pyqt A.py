import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create our Layout
        grid = QGridLayout()
        self.setLayout(grid)
        self.setGeometry(100, 10, 300, 500) # topleftx, toplefty, width, height

        # Create our widgets

        label = QLabel("Hello World", self)
        grid.addWidget(label, 1, 1, 1, 1)  # row, col, span_row, span_col

        label2 = QLabel("I don't know", self)
        grid.addWidget(label2, 2, 1, 1, 2)
        label2.setAlignment(Qt.AlignCenter)

        label3 = QLabel("Label 3", self)
        grid.addWidget(label3, 1, 2, 1, 1)

        btn1 = QPushButton("Push Me", self)
        grid.addWidget(btn1, 3, 1, 1, 1)

        label_btn1 = QLabel("Not Pushed", self)
        label_btn1.setText("Unpushed")
        grid.addWidget(label_btn1, 3, 2, 1, 1)

        lcd = QLCDNumber(self)
        grid.addWidget(lcd, 4, 1, 1, 2)

        sld = QSlider(Qt.Horizontal, self)
        grid.addWidget(sld, 5, 1, 1, 2)




        # Slots and Signals
        # Signals are sent when an event occurs.
        # Slot is a place for the signal to go


        # draw our gui
        self.show()


if __name__ == "__main__":
    '''main program goes here'''
    app = QApplication(sys.argv)  # look this up
    gui = Window()
    sys.exit(app.exec())