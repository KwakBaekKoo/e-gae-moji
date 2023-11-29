import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui.userInfo import UserInfoWidget
from ui.paintingBoard import PaintingBoardWidget
from ui.chatBoard import ChatBoardWidget
from ui.buttons import ButtonBoxWidget
from ui.sendMessage import SendMessageWidget
from ui.joinCreateRoom import JoinCreateRoom
from backend import client, server
import socket

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.userName = '홍길동'
        self.userPosition = 'guset'

        if self.userPosition == 'host':
            self.userState = 'Host'
        else:
            self.userState = 'Not Ready'

        self.server = server.ServerSocket(self)
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 4001

        self.client = client.ClientSocket(self)

        self.joinCreateRoom = JoinCreateRoom(lambda: self.server.start(self.ip, self.port),
                                             lambda ip: self.client.start(ip))

        self.initUI()

    def initUI(self):
        self.hBox_gameBoard = QHBoxLayout()  # 제일 바탕이 되는 레이아웃. vertical layout 두개로 구성됨
        self.vBox_subGameBoard_1 = QVBoxLayout()  # verical layout 1: 유저리스트와 그림판이 들어가는 레이아웃
        self.vBox_subGameBoard_2 = QVBoxLayout()  # verical layout 2: 로고, 채팅창, 시작(준비)버튼, 나가기버튼이 있는 레이아웃
        self.vBox_subGameBoard_1.setAlignment(Qt.AlignBottom)
        self.vBox_subGameBoard_2.setAlignment(Qt.AlignTop)

        self.hBox_userList = QHBoxLayout()  # 유저정보를 나열하기 위한 레이아웃
        self.vBox_subGameBoard_1.addLayout(self.hBox_userList)

        # 3명 들어왔다고 가정
        userList = [UserInfoWidget('구형모', 'host', 'Ready'), UserInfoWidget('곽다윗', 'guest', 'Ready'),
                    UserInfoWidget('백현식', 'guest', 'Ready')]
        self.hBox_userList.addLayout(UserInfoWidget(self.userName, self.userPosition, self.userState))  # 내정보 먼저 추가
        # 나머지 유저들의 정보 추가
        for user in userList:
            self.hBox_userList.addLayout(user)

        self.vBox_subGameBoard_1.addWidget(PaintingBoardWidget())

        logo = QLabel()
        logo.setPixmap(QPixmap('assets/logo.png'))
        self.vBox_subGameBoard_2.addWidget(logo)
        self.vBox_subGameBoard_2.addLayout(self.joinCreateRoom)
        self.chatBoard = ChatBoardWidget(self.userName)
        self.vBox_subGameBoard_2.addWidget(self.chatBoard)
        self.vBox_subGameBoard_2.addWidget(SendMessageWidget(self.sendMsg))
        self.vBox_subGameBoard_2.addLayout(
            ButtonBoxWidget(self.readyButtonClick, self.exitButtonClick, self.userPosition))

        self.hBox_gameBoard.addLayout(self.vBox_subGameBoard_1)
        self.hBox_gameBoard.addLayout(self.vBox_subGameBoard_2)

        self.setLayout(self.hBox_gameBoard)
        self.resize(1400, 800)
        self.show()

    def readyButtonClick(self):
        if self.userState == 'Ready':
            self.userState = 'Not Ready'
            self.hBox_userList.itemAt(0).setStatus('Not Ready')
        else:
            self.userState = 'Ready'
            self.hBox_userList.itemAt(0).setStatus('Ready')
        # 서버에게 준비완료 메시지 보내기

    def sendMsg(self, msg):
        if self.server.isInitialized:
            self.chatBoard.addMessage(msg)
            self.server.send(msg)
        if self.client.isInitialized:
            self.client.send(msg)

    def exitButtonClick(self):
        # 서버와 연결 끊고 창 닫기
        print('게임종료')

    def startServer(self, ip):
        self.joinCreateRoom.onServerCreated(ip)

    def updateClient(self, addr, isConnect=False):
        print("update client:", addr, end=" ")
        None

    def updateMsg(self, msg):
        print("update msg:", msg, end=" ")
        self.chatBoard.addMessage(msg)
        None



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
