import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class UserInfoLayout(QVBoxLayout):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addWidget(QLabel('Label 1'))        