import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SendMessageWidget(QLineEdit):

    def __init__(self):
        super().__init__()
        self.setFixedWidth(300)

    def keyPressEvent(self, e):
        #엔터 누르면 서버로 메시지 전송
        if e.key() == Qt.Key_Return:
            print('send message to server')
            self.clear()
        else:
            super().keyPressEvent(e)

