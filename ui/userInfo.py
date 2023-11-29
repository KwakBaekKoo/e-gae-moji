import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class UserInfoWidget(QVBoxLayout):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.initUI()

    def initUI(self):        
        userImage = UserImage()
        userName = QLabel(self.name)
        if self.name == 'Host':
            userName.setStyleSheet('color: blue')
        userName.setContentsMargins(0, 0, 0, 20)
            
        self.addLayout(userImage)
        self.addWidget(userName)

        self.setAlignment(userImage, Qt.AlignCenter)
        self.setAlignment(userName, Qt.AlignCenter)

class UserImage(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('assets/user.png')
        user_img = QLabel()
        user_img.setPixmap(pixmap)
        self.addWidget(user_img)
