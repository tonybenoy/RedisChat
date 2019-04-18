import redis
import pdb
import threading
import datetime


class getchats(threading.Thread):
    def __init__(self, chat, p):
        threading.Thread.__init__(self)
        self.chat = chat
        self.p = p

    def run(self):
        self.p.subscribe(chat)
        for message in self.p.listen():
            if message["type"] == 'message':
                print(str(datetime.datetime.now())+" : " +
                      message["data"].decode("utf-8"))


if __name__ == "__main__":
    r = redis.Redis(host='localhost', port=6379, db=0)
    usernameavailable = True
    myusername = input("Enter Your Username\n")
    while usernameavailable:
        active = r.get(myusername)
        if active == None:
            usernameavailable = False
            r.set(myusername, "Active")
        else:
            myusername = input(
                "Username not available. Enter Your Username \n")
    p = r.pubsub()
    currentchat = None
    mychats = []
    while True:
        com = input("\n >")
        if com[0:5] == "/chat":
            chat = getchats("".join(sorted([myusername, com[6:]])), p)
            chat.start()
            currentchat = com[6:]
            mychats.append(chat)
            chat.setName(com[6:])
        elif com[0:8] == "/mychats":
            for item in mychats:
                print(item.getName())
        elif com[0] == "/":
            print("Unknown Command")
        else:
            r.publish(
                "".join(sorted([myusername, currentchat])), myusername+" : "+com)
