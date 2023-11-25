from PyQt5.QtWidgets import *


class JoinCreateRoom(QVBoxLayout):

    def __init__(self, onStartServer, onJoinRoom):
        super().__init__()

        self.onStartServer = onStartServer
        self.onJoinRoom = onJoinRoom
        self.server_ip = ""

        self.labelCreateRoom = None
        self.editJoinRoom = None

        self.initUI()

    def initUI(self):
        layoutCreateRoom = QVBoxLayout()

        self.labelCreateRoom = QLabel()
        self.labelCreateRoom.setText("Server IP: {}".format(self.server_ip))
        layoutCreateRoom.addWidget(self.labelCreateRoom)

        btnCreateRoom = QPushButton("Create")
        btnCreateRoom.clicked.connect(self.onStartServer)
        layoutCreateRoom.addWidget(btnCreateRoom)

        layoutJoinRoom = QHBoxLayout()

        self.editJoinRoom = QLineEdit()
        self.editJoinRoom.setPlaceholderText("192.168.0.1:3000")
        layoutJoinRoom.addWidget(self.editJoinRoom)

        btnJoinRoom = QPushButton("join")
        btnJoinRoom.clicked.connect(self.onCickJoin)
        layoutJoinRoom.addWidget(btnJoinRoom)

        groupboxCreateRoom = QGroupBox("Create Room")
        groupboxCreateRoom.setLayout(layoutCreateRoom)
        groupboxCreateRoom.setFixedWidth(300)
        self.addWidget(groupboxCreateRoom)

        groupboxJoinRoom = QGroupBox("Join Room")
        groupboxJoinRoom.setLayout(layoutJoinRoom)
        groupboxJoinRoom.setFixedWidth(300)
        self.addWidget(groupboxJoinRoom)

    def onCickJoin(self):
        if self.editJoinRoom != "":
            self.onJoinRoom(self.editJoinRoom.text())

    def onClickCreateServer(self):
        self.server_ip = self.onStartServer()
        print("Server IP: {}".format(self.server_ip))

    def onServerCreated(self, ip):
        self.labelCreateRoom.setText("Server IP: {}".format(ip))
