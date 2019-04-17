import redis
import pdb
import threading
import datetime


class getchats(threading.Thread):
    def __init__(self, user, p):
        threading.Thread.__init__(self)
        self.user = user
        self.p = p

    def run(self):
        self.p.subscribe("".join(sorted([myusername, self.user])))
        for message in self.p.listen():
            print(message)


r = redis.Redis(host='localhost', port=6379, db=0)
usernameavailable = True
myusername = input("Enter Your Username")
while usernameavailable:
    active = r.get(myusername)
    if active == None:
        usernameavailable = False
        r.set(myusername, "Active")
    else:
        myusername = input("Username not available. Enter Your Username")
p = r.pubsub()
mychats = []
# pdb.set_trace()
while True:
    com = input("\n >")
    if com[0:5] == "/chat":
        chat = getchats(com[6:], p)
        chat.start()
        mychats.append(chat)
        chat.setName(com[6:])
    elif com[0:8] == "/mychats":
        for item in mychats:
            print(item.getname())
