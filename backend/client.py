from threading import Thread
import socket
from PyQt5.QtCore import pyqtSignal, QObject

tcpClient = None


class ClientSocket(QObject):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def start(self, ip):
        clientThread = ClientThread(ip)
        clientThread.start()

    def send(self,msg):
        global tcpClient
        if tcpClient:
            tcpClient.send(msg.encode())


class ClientThread(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip

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
                    print('[RECV]:', msg)

    # data = tcpClient.recv(BUFFER_SIZE)
    # print(data.decode("utf-8"))
    # tcpClient.close()
