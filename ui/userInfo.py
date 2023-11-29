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
            self.readyOrNot = QLabel('Host')
            self.readyOrNot.setStyleSheet('color: blue')
        else:
            self.readyOrNot = QLabel()
            self.setStatus(self.status)
            
        self.addWidget(userName)
        self.addLayout(userImage)
        self.addWidget(self.readyOrNot)

        self.setAlignment(userImage, Qt.AlignCenter)
        self.setAlignment(userName, Qt.AlignCenter)
        self.setAlignment(self.readyOrNot, Qt.AlignCenter)

    def setStatus(self, status):
        self.status = status
        self.readyOrNot.setText(self.status)
        if self.status == 'Ready':
            self.readyOrNot.setStyleSheet('color: green')
        else:
            self.readyOrNot.setStyleSheet('color: red')

class UserImage(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('assets/user.png')
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