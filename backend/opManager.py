import json


class OpManager:
    def __init__(self, onUserList, onChat, onDraw, onCorrectAnswer):
        self.onUserList = onUserList
        self.onChat = onChat
        self.onDraw = onDraw
        self.onCorrectAnswer = onCorrectAnswer

    def parse(self, msg):
        parcel = json.loads(msg)
        if parcel["op"] == "user_list":
            self.onUserList(json.loads(parcel["user"]))
        elif parcel["op"] == "correct_answer":
            self.onCorrectAnswer(parcel["user"])
        elif parcel["op"] == "message":
            self.onChat(parcel["user"], parcel["data"])
        elif parcel["op"] == "draw":
            self.onDraw(parcel["data"])


