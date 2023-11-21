import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class UserInfoWidget(QVBoxLayout):

    def __init__(self, name, position, status):
        super().__init__()
        self.name = name
        self.position = position
        self.status = status
        self.initUI()

    def initUI(self):        
        userImage = UserImage()
        userName = QLabel(self.name)
        userName.setContentsMargins(0, 20, 0, 0)

        if self.position == 'host':
            readyOrNot = QLabel('Host')
            readyOrNot.setStyleSheet('color: blue')
        else:
            readyOrNot = ReadyOrNot(self.status)
            
        self.addWidget(userName)
        self.addLayout(userImage)
        self.addWidget(readyOrNot)

        self.setAlignment(userImage, Qt.AlignCenter)
        self.setAlignment(userName, Qt.AlignCenter)
        self.setAlignment(readyOrNot, Qt.AlignCenter)

class UserImage(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('front-end/assets/user.png')
        user_img = QLabel()
        user_img.setPixmap(pixmap)
        self.addWidget(user_img)
        
class ReadyOrNot(QLabel):

    def __init__(self, status):
        super().__init__()
        self.status = status
        self.initUI()

    def initUI(self):
        if self.status == 'Ready':
            self.setText('Ready')
            self.setStyleSheet('color: green')
        else:
            self.setText('Not Ready')
            self.setStyleSheet('color: red')
            self.font().setPointSize(20)