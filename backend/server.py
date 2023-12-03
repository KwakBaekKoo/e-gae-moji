import json
from threading import Thread
from socket import *
from PyQt5.QtCore import pyqtSignal, QObject
import random
import time


class ServerSocket(QObject):
    recv_signal = pyqtSignal(str)
    start_signal = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__()
        self.isInitialized = False
        self.t = None
        self.server = None
        self.parent = parent
        self.bListen = False
        self.clients = []
        self.userProfiles = []
        self.threads = []
        self.answers = ["고양이", "사과", "자동차","오리"]
        self.currentAnswer = ""

        self.recv_signal.connect(self.parent.updateMsg)
        self.start_signal.connect(self.parent.startServer)

    def __del__(self):
        self.stop()

    def start(self, ip, port):
        self.server = socket(AF_INET, SOCK_STREAM)

        try:
            self.server.bind((ip, port))
        except Exception as e:
            print('Bind Error : ', e)
            return False
        else:
            self.bListen = True
            self.t = Thread(target=self.listen, args=(self.server,))
            self.t.start()
            print('Server Listening...')

        self.userProfiles.append({"name": "Host", "score": 0})
        self.start_signal.emit("{}:{}".format(ip, port))
        self.updateProfile(True, "Host", None)
        self.updateUser()
        self.isInitialized = True
        return True

    def stop(self):
        self.bListen = False
        if self.server is not None:
            self.server.close()
            print('Server Stop')

    def listen(self, server):
        while self.bListen:
            server.listen(4)
            try:
                client, addr = server.accept()
            except Exception as e:
                print('Accept() Error : ', e)
                break
            else:
                self.clients.append(client)
                name = "Guest {}".format(addr[1])
                self.userProfiles.append({"name": name, "score": 0})
                self.updateProfile(False, name, client)
                self.updateUser()
                t = Thread(target=self.receive, args=(addr, client))
                self.threads.append(t)
                t.start()
                if len(self.clients) >= 2:
                    self.sendAnswerToHost()

        self.removeAllClients()
        self.server.close()

    def receive(self, addr, client):
        while True:
            try:
                recv = client.recv(1024)
            except Exception as e:
                print('Recv() Error :', e)
                break
            else:
                msg = str(recv, encoding='utf-8')
                if msg:
                    self.send(msg)
                    self.recv_signal.emit(msg)
                    self.checkAnswer(addr[1], msg)

        self.removeClient(addr, client)

    def checkAnswer(self, userName, msg):
        parsed = json.loads(msg)
        if self.currentAnswer == parsed["data"]:
            for i, item in enumerate(self.userProfiles):
                if item["name"] == "Guest {}".format(userName):
                    self.userProfiles[i]["score"] += 5

            self.updateUser()
            self.notifyCorrectAnswer(userName, self.currentAnswer)
            self.answers.remove(self.currentAnswer)
            self.sendAnswerToHost()

    def updateProfile(self, isHost, name, client):
        parcel = {"op": "profile", "data": name}
        if isHost:
            self.recv_signal.emit(json.dumps(parcel))
        else:
            client.send(json.dumps(parcel).encode())

    def updateUser(self):
        parcel = {"op": "user_list", "users": self.userProfiles}
        self.send(json.dumps(parcel))
        self.recv_signal.emit(json.dumps(parcel))

    def sendMessage(self, user, message):
        parcel = {"op": "message", "user": user, "data": message}
        self.send(json.dumps(parcel))
        self.recv_signal.emit(json.dumps(parcel))

    def notifyCorrectAnswer(self, userName, answer):
        self.send(json.dumps({"op": "message", "user": "공지", "data": "{} 정답!! {}".format(userName, answer)}))

    def sendAnswerToHost(self):
        answer = random.choice(self.answers)
        self.currentAnswer = answer
        self.recv_signal.emit(json.dumps({"op": "message", "user": "공지", "data": "이번에 그릴 정답은?: {}".format(answer)}))

    def send(self, msg):
        try:
            for c in self.clients:
                c.send(msg.encode())
        except Exception as e:
            print('Send() Error : ', e)

    def removeClient(self, addr, client):
        # find closed client index
        idx = -1
        for k, v in enumerate(self.clients):
            if v == client:
                idx = k
                break

        client.close()
        self.clients.remove(client)

        del (self.threads[idx])
        self.resourceInfo()

    def removeAllClients(self):
        for c in self.clients:
            c.close()

        self.clients.clear()
        self.threads.clear()

        self.resourceInfo()

    def resourceInfo(self):
        print('Number of Client socket\t: ', len(self.clients))
        print('Number of Client thread\t: ', len(self.threads))

    def drawMessage(self, user, message):
        parcel = {"op": "draw", "user": user, "data": message}
        self.send(json.dumps(parcel))
