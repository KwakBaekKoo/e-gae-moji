import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChatBoardWidget(QListWidget):

    def __init__(self):
        super().__init__()       
        self.setFixedWidth(300)

        self.addMessage('좋아 가보자 스네시 스네시 곽백구')

    def addMessage(self, message): # 서버로부터 메시지를 받아서 채팅창에 추가
        self.addItem(message)