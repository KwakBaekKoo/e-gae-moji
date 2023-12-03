from threading import Thread
import socket
import json
from PyQt5.QtCore import pyqtSignal, QObject

tcpClient = None

class ClientSocket(QObject):
    recv_signal = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__()
        self.isInitialized = False
        self.parent = parent
        self.recv_signal.connect(self.parent.updateMsg)

    def start(self, ip):
        clientThread = ClientThread(ip, self.receive)
        clientThread.start()
        self.isInitialized = True

    def sendMessage(self, user, message):
        parcel = {"op": "message", "user": user, "data": message}
        self.send(json.dumps(parcel))

    def send(self,msg):
        global tcpClient
        if tcpClient:
            tcpClient.send(msg.encode())

    def receive(self, msg):
        self.recv_signal.emit(msg)


class ClientThread(Thread):
    def __init__(self, ip,receive):
        Thread.__init__(self)
        self.ip = ip
        self.receive = receive

    def run(self):
        global tcpClient
        tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host, port = str(self.ip).split(":")
        tcpClient.connect((host, int(port)))

        while True:
            try:
                recv = tcpClient.recv(1024)
            except Exception as e:
                print('Recv() Error :', e)
                break
            else:
                msg = str(recv, encoding='utf-8')
                if msg:
                    self.receive(msg)
