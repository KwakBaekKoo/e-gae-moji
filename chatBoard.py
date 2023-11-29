import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChatBoardWidget(QListWidget):

    def __init__(self, userName):
        super().__init__()
        self.userName = userName  
        self.setFixedWidth(300)
        self.addItem('Welcome and Enjoy!')

    def addMessage(self, message): # 서버로부터 메시지를 받아서 채팅창에 추가
        self.addItem('%s: %s' %(self.userName, message))
        QTimer.singleShot(0, lambda: self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())) # 스크롤을 제일 아래로 내리기
    