import sys
from PyQt5.QtWidgets import *

class ButtonBoxWidget(QVBoxLayout):

    def __init__(self, buttonClick, exitButtonClick, userPosition):
        super().__init__()       
        self.buttonClick = buttonClick
        self.exitButtonClick = exitButtonClick
        self.userPosition = userPosition
        self.initUI()
        
    def initUI(self):
        if self.userPosition == 'host':
            button = QPushButton('Start')
        else:
            button = QPushButton('이거 버튼 뭐로 하지')
        exitButton = QPushButton('Exit')

        button.clicked.connect(self.buttonClick)
        exitButton.clicked.connect(self.exitButtonClick)

        button.setFixedHeight(50)
        exitButton.setFixedHeight(50)

        self.addWidget(button)
        self.addWidget(exitButton)