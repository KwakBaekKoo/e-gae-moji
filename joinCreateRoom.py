from PyQt5.QtWidgets import *


class JoinCreateRoom(QVBoxLayout):

    def __init__(self, onStartServer):
        super().__init__()

        self.onStartServer = onStartServer
        self.server_ip = ""

        self.labelCreateRoom = None

        self.initUI()

    def initUI(self):
        layoutCreateRoom = QVBoxLayout()

        self.labelCreateRoom = QLabel()
        self.labelCreateRoom.setText("Server IP: {}".format(self.server_ip))
        layoutCreateRoom.addWidget(self.labelCreateRoom)

        button_create_room = QPushButton("Create")
        button_create_room.clicked.connect(self.onStartServer)
        layoutCreateRoom.addWidget(button_create_room)

        layoutJoinRoom = QHBoxLayout()

        editJoinRoom = QLineEdit()
        editJoinRoom.setPlaceholderText("192.168.0.1:3000")

        layoutJoinRoom.addWidget(editJoinRoom)
        layoutJoinRoom.addWidget(QPushButton('Join'))

        groupboxCreateRoom = QGroupBox("Create Room")
        groupboxCreateRoom.setLayout(layoutCreateRoom)
        groupboxCreateRoom.setFixedWidth(300)
        self.addWidget(groupboxCreateRoom)

        groupboxJoinRoom = QGroupBox("Join Room")
        groupboxJoinRoom.setLayout(layoutJoinRoom)
        groupboxJoinRoom.setFixedWidth(300)
        self.addWidget(groupboxJoinRoom)

    def onClickCreateServer(self):
        self.server_ip = self.onStartServer()
        print("Server IP: {}".format(self.server_ip))

    def onServerCreated(self, ip):
        self.labelCreateRoom.setText("Server IP: {}".format(ip))

