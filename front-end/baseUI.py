import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from userInfo import UserInfoLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hBox_gameBoard = QHBoxLayout() # 제일 바탕이 되는 레이아웃. vertical layout 두개로 구성됨.
        vBox_subGameBoard_1 = QVBoxLayout() # verical layout 1: 유저리스트와 그림판이 들어가는 레이아웃
        hBox_userList = QHBoxLayout() # 유저리스트. 최대 8명 정도가 적당해보이고, ready 표시나 점수가 같이 나오면 좋을 듯.
        hBox_paintingBoard = QHBoxLayout() # 그림판
        vBox_userInfo = QVBoxLayout()

        vBox_subGameBoard_2 = QVBoxLayout() # verical layout 2: 로고, 채팅창, 시작(준비)버튼, 나가기버튼이 있는 레이아웃
        hBox_brandLogo = QHBoxLayout()
        hBox_chatBoard = QHBoxLayout()
        hBox_start_or_exit = QHBoxLayout()

        hBox_userList.addLayout(UserInfoLayout())
        hBox_userList.addLayout(UserInfoLayout())
        hBox_userList.addLayout(UserInfoLayout())
        hBox_userList.addLayout(UserInfoLayout())
        hBox_userList.addLayout(UserInfoLayout())
        hBox_userList.addLayout(UserInfoLayout())
        hBox_userList.addLayout(UserInfoLayout())
        hBox_userList.addLayout(UserInfoLayout())

        vBox_subGameBoard_1.addLayout(hBox_userList)
        vBox_subGameBoard_1.addLayout(hBox_paintingBoard)

        vBox_subGameBoard_2.addLayout(hBox_brandLogo)
        vBox_subGameBoard_2.addLayout(hBox_chatBoard)
        vBox_subGameBoard_2.addLayout(hBox_start_or_exit)

        hBox_gameBoard.addLayout(vBox_subGameBoard_1)
        hBox_gameBoard.addLayout(vBox_subGameBoard_2)
        
        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)
        # hbox.addStretch(1)

        # vbox = QVBoxLayout()
        # vbox.addStretch(3)
        # vbox.addLayout(hbox)
        # vbox.addStretch(1)

        self.setLayout(hBox_gameBoard)
        self.resize(1400, 800)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
