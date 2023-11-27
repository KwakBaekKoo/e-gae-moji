import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class SendMessageWidget(QLineEdit):

    def __init__(self, send):
        super().__init__()
        self.setFixedWidth(300)
        self.send = send

    def keyPressEvent(self, e):
        # 엔터 누르면 서버로 메시지 전송
        if e.key() == Qt.Key_Return:
            print('send message to server')
            self.send(self.text())
            self.clear()
        else:
            super().keyPressEvent(e)
