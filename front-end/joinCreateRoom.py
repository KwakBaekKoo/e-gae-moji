from PyQt5.QtWidgets import *


class JoinCreateRoom(QVBoxLayout):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout_create_room = QVBoxLayout()

        label_create_room = QLabel()
        label_create_room.setText("Server IP: ")
        layout_create_room.addWidget(label_create_room)

        button_create_room = QPushButton("Create")
        layout_create_room.addWidget(button_create_room)

        layout_join_room = QHBoxLayout()

        edit_join_room = QLineEdit()
        edit_join_room.setPlaceholderText("192.168.0.1:3000")
        edit_join_room.setMaximumWidth(600)

        layout_join_room.addWidget(edit_join_room)
        layout_join_room.addWidget(QPushButton('Join Room'))

        groupbox_create_room = QGroupBox("Create Room")
        groupbox_create_room.setLayout(layout_create_room)
        self.addWidget(groupbox_create_room)

        groupbox_join_room = QGroupBox("Join")
        groupbox_join_room.setLayout(layout_join_room)
        self.addWidget(groupbox_join_room)

        self.setSpacing(50)

