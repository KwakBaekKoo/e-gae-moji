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
from backend import client, server, opManager
import socket

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.userPosition = 'host? guest?'

        self.server = server.ServerSocket(self)
        self.ip = socket.gethostbyname(socket.gethostname())
        self.userName = ""
        self.port = 4001

        self.client = client.ClientSocket(self)

        self.joinCreateRoom = JoinCreateRoom(lambda: self.server.start(self.ip, self.port),
                                             lambda ip: self.client.start(ip))

        self.opManager = opManager.OpManager(self.onUserList, self.onChat, self.onDraw, self.onCorrectAnswer,
                                             self.onUpdateProfile)

        self.paintingBoard = PaintingBoardWidget(self.sendDrawingToServer)

        self.initUI()

    def initUI(self):
        self.hBox_gameBoard = QHBoxLayout()  # 제일 바탕이 되는 레이아웃. vertical layout 두개로 구성됨
        self.vBox_subGameBoard_1 = QVBoxLayout()  # verical layout 1: 유저리스트와 그림판이 들어가는 레이아웃
        self.vBox_subGameBoard_2 = QVBoxLayout()  # verical layout 2: 로고, 채팅창, 시작(준비)버튼, 나가기버튼이 있는 레이아웃
        self.vBox_subGameBoard_1.setAlignment(Qt.AlignBottom)
        self.vBox_subGameBoard_2.setAlignment(Qt.AlignTop)

        self.container_userList = QWidget()
        self.container_userList.setFixedHeight(175)
        self.vBox_subGameBoard_1.addWidget(self.container_userList)
        self.hBox_userList = QHBoxLayout()

        self.vBox_subGameBoard_1.addWidget(self.paintingBoard)

        logo = QLabel()
        logo.setPixmap(QPixmap('assets/logo.png'))
        self.vBox_subGameBoard_2.addWidget(logo)
        self.vBox_subGameBoard_2.addLayout(self.joinCreateRoom)
        self.chatBoard = ChatBoardWidget()
        self.vBox_subGameBoard_2.addWidget(self.chatBoard)
        self.vBox_subGameBoard_2.addWidget(SendMessageWidget(self.sendMsg))
        self.vBox_subGameBoard_2.addLayout(
            ButtonBoxWidget(self.buttonClick, self.exitButtonClick, self.userPosition))

        self.hBox_gameBoard.addLayout(self.vBox_subGameBoard_1)
        self.hBox_gameBoard.addLayout(self.vBox_subGameBoard_2)

        self.setLayout(self.hBox_gameBoard)
        self.resize(1400, 800)
        self.show()

    def buttonClick(self):
        # 무슨 버튼으로 하징
        print('버튼 클릭')

    def sendMsg(self, msg):
        if self.server.isInitialized:
            self.server.sendMessage(self.userName, msg)
        if self.client.isInitialized:
            self.client.sendMessage(self.userName, msg)

    def exitButtonClick(self):
        # 서버와 연결 끊고 창 닫기
        del self.server
        del self.client
        sys.exit()

    def startServer(self, ip):
        self.joinCreateRoom.onServerCreated(ip)

    def updateMsg(self, msg):
        self.opManager.parse(msg)

    def onUpdateProfile(self, name):
        self.userName = name

    def onUserList(self, users):
        userList = [UserInfoWidget(i) for i in list(users)]

        for user in userList:
            self.hBox_userList.addLayout(user)

        self.container_userList.setLayout(self.hBox_userList)

    def onCorrectAnswer(self, user):
        print("Correct Answer", user, end=" ")

    def onChat(self, user, msg):
        self.chatBoard.addMessage(user, msg)

    def sendDrawingToServer(self, data):
        if self.server.isInitialized:
            self.server.drawMessage(self.userName, data)
        if self.client.isInitialized:
            self.server.drawMessage(self.userName, data)

    def onDraw(self, data):
        self.paintingBoard.drawFromServer(data)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
