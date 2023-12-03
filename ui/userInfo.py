import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UserInfoWidget(QVBoxLayout):

    def __init__(self, user):
        super().__init__()
        self.name = user["name"]

        self.labelName = QLabel(self.name)
        self.labelScore = QLabel("0")

        self.initUI()

    def initUI(self):
        userImage = UserImage()

        if self.name == 'Host':
            self.labelName.setStyleSheet('color: blue')
        self.labelName.setContentsMargins(0, 0, 0, 0)
        self.labelScore.setContentsMargins(0, 0, 0, 0)

        self.addLayout(userImage)
        self.addWidget(self.labelName)
        self.addWidget(self.labelScore)

        self.setAlignment(userImage, Qt.AlignCenter)
        self.setAlignment(self.labelName, Qt.AlignCenter)
        self.setAlignment(self.labelScore, Qt.AlignCenter)



class UserImage(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('assets/user.png')
        user_img = QLabel()
        user_img.setPixmap(pixmap)
        self.addWidget(user_img)
