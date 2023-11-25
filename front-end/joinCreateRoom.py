from PyQt5.QtWidgets import *


class JoinCreateRoom(QVBoxLayout):

    def __init__(self, onStartServer):
        super().__init__()


        self.onStartServer = onStartServer
        self.server_ip = ""

        self.initUI()

    def initUI(self):
        layout_create_room = QVBoxLayout()

        label_create_room = QLabel()
        label_create_room.setText("Server IP: {}".format(self.server_ip))
        layout_create_room.addWidget(label_create_room)

        button_create_room = QPushButton("Create")
        layout_create_room.addWidget(button_create_room)

        layout_join_room = QHBoxLayout()

        edit_join_room = QLineEdit()
        edit_join_room.setPlaceholderText("192.168.0.1:3000")

        layout_join_room.addWidget(edit_join_room)
        layout_join_room.addWidget(QPushButton('Join'))

        groupbox_create_room = QGroupBox("Create Room")
        groupbox_create_room.setLayout(layout_create_room)
        groupbox_create_room.setFixedWidth(300)
        self.addWidget(groupbox_create_room)

        groupbox_join_room = QGroupBox("Join Room")
        groupbox_join_room.setLayout(layout_join_room)
        groupbox_join_room.setFixedWidth(300)
        self.addWidget(groupbox_join_room)

    def onClickCreateServer(self):
        self.server_ip = self.onStartServer()

