import sys
from PyQt5.QtWidgets import *

class ButtonBoxWidget(QVBoxLayout):

    def __init__(self, readyButtonClick, exitButtonClick, userPosition):
        super().__init__()       
        self.readyButtonClick = readyButtonClick
        self.exitButtonClick = exitButtonClick
        self.userPosition = userPosition
        self.initUI()
        
    def initUI(self):
        if self.userPosition == 'host':
            readyButton = QPushButton('Start')
        else:
            readyButton = QPushButton('Ready')
        exitButton = QPushButton('Exit')

        readyButton.clicked.connect(self.readyButtonClick)
        exitButton.clicked.connect(self.exitButtonClick)

        readyButton.setFixedHeight(50)
        exitButton.setFixedHeight(50)

        self.addWidget(readyButton)
        self.addWidget(exitButton)