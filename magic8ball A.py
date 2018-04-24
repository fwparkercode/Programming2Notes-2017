import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.message_list = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely","You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now","Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no","My sources say no", "Outlook not so good", "Very doubtful"]

        # Set my layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(10, 10, 400, 200)  # topleftx, toplefty, width, height
        self.title_font = QFont("Times", 30, QFont.Bold)


        # Create our widgets
        self.title = QLabel("Magic 8 Ball")
        self.grid.addWidget(self.title, 1, 1, 1, 2)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(self.title_font)

        self.ask_button = QPushButton("Ask me")
        self.grid.addWidget(self.ask_button, 2, 1, 1, 1)

        self.answer = QLabel("Answer")
        self.grid.addWidget(self.answer, 2,2,1,1)

        # signals and slots
        self.ask_button.clicked.connect(self.ask_me)

        self.show()
    def ask_me(self):
        self.answer.setText(self.message_list[random.randrange(len(self.message_list))])





if __name__ == "__main__":
    '''main program goes here'''
    app = QApplication(sys.argv)  # look this up
    gui = Window()
    sys.exit(app.exec())
