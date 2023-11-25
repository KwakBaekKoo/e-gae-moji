import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from userInfo import UserInfoWidget
from paintingBoard import PaintingBoardWidget
from chatBoard import ChatBoardWidget
from buttons import ButtonBoxWidget
from sendMessage import SendMessageWidget
from joinCreateRoom import JoinCreateRoom
from server import server
import socket


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.userName = '홍길동'
        self.userPosition = 'host'

        if self.userPosition != 'host':
            self.userState = 'Not Ready'
        else:
            self.userState = 'Host'

        self.server = server.ServerSocket(self)
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 3000

        self.initUI()

    def initUI(self):
        hBox_gameBoard = QHBoxLayout()  # 제일 바탕이 되는 레이아웃. vertical layout 두개로 구성됨.
        vBox_subGameBoard_1 = QVBoxLayout()  # verical layout 1: 유저리스트와 그림판이 들어가는 레이아웃
        vBox_subGameBoard_1.setAlignment(Qt.AlignBottom)
        vBox_subGameBoard_2 = QVBoxLayout()  # verical layout 2: 로고, 채팅창, 시작(준비)버튼, 나가기버튼이 있는 레이아웃
        vBox_subGameBoard_2.setAlignment(Qt.AlignTop)

        hBox_userList = QHBoxLayout()

        # 3명 들어왔다고 가정
        userList = [UserInfoWidget('구형모', 'guest', 'Ready'), UserInfoWidget('곽다윗', 'guest', 'Ready'),
                    UserInfoWidget('백현식', 'guest', 'Ready')]
        for user in userList:
            hBox_userList.addLayout(user)
        hBox_userList.addLayout(UserInfoWidget(self.userName, self.userPosition, self.userState))

        vBox_subGameBoard_1.addLayout(hBox_userList)
        vBox_subGameBoard_1.addWidget(PaintingBoardWidget())

        logo = QLabel()
        logo.setPixmap(QPixmap('assets/logo.png'))
        vBox_subGameBoard_2.addWidget(logo)
        vBox_subGameBoard_2.addLayout(JoinCreateRoom(lambda: self.server.start(self.ip, self.port)))
        vBox_subGameBoard_2.addWidget(ChatBoardWidget())
        vBox_subGameBoard_2.addWidget(SendMessageWidget())
        vBox_subGameBoard_2.addLayout(ButtonBoxWidget(self.readyButtonClick, self.exitButtonClick, self.userPosition))

        hBox_gameBoard.addLayout(vBox_subGameBoard_1)
        hBox_gameBoard.addLayout(vBox_subGameBoard_2)

        self.setLayout(hBox_gameBoard)
        self.resize(1400, 800)
        self.show()

    def readyButtonClick(self):
        if self.userState == 'Ready':
            self.userState = 'Not Ready'
        else:
            self.userState = 'Ready'

        print(self.userState)
        # 바뀐 정보에 따라 화면 갱신
        # self.update() ???? 뭐로 해야할지 모르겠음

    def exitButtonClick(self):
        print('게임종료')

    def updateClient(self, addr, isConnect=False):
        print("update client:", addr, end=" ")
        None

    def updateMsg(self, msg):
        print("update msg:", msg, end=" ")
        None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
