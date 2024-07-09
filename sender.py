from pymongo import MongoClient
from datetime import datetime
from threading import Thread
from time import sleep
import os
import sys

u1 = str(sys.argv[1])
u2 = str(sys.argv[2])

cluster = MongoClient("mongodb+srv://neelkalpa:EUQ9gWA9M2X*T&K??HyYBXN9gjXxpVKg@socialmedia.ps81bcd.mongodb.net/?retryWrites=true&w=majority")
db = cluster["socialmedia"]["messages"]

def sendmsg(sender, receiver, message):
    date = datetime.now().strftime("%x")
    time = datetime.now().strftime("%X")
    msg = {"sender": sender, "receiver":receiver, "message":message, "date":date, "time":time}
    db.insert_one(msg)

def newmsg(receiver,sender):
    newmessages = []
    oldmsg = readoldmsg({"date":"00/00/00", "time":"00:00:00"})
    for x in db.find({"sender":sender,"receiver":receiver}):
        if (stripdatetime(oldmsg["date"],oldmsg["time"]) < stripdatetime(x["date"],x["time"])):
            writeoldmsg(x)
            newmessages.append(x["message"])
            db.delete_one({"message":x["message"]})
    return newmessages        


def stripdatetime(date, time):
    date = date[6:8] + date[3:5] + date[0:2]
    x = str(date).replace('/','') + str(time).replace(':','')
    return int(x)

def writeoldmsg(msg):
    f = open('temp'+u1+u2+'.txt', 'w')
    f.write(msg["date"] + '\n')
    f.write(msg["time"])
    f.close()

def readoldmsg(msg):
    f = open('temp'+u1+u2+'.txt', 'r')
    msg["date"] = f.readline().replace('\n','')
    msg["time"] = f.readline()
    f.close()
    return msg

def background(t):
    while True:
        sleep(t)
        x = newmsg(u1,u2)
        if (len(x) != None):
            for y in x:
                inputformat('\n' + u2 + ': ' + y)

def inputformat(s):
    f = open('data'+u1+u2+'.txt', 'a')
    s = s + '\n'
    f.write(s) 
    f.close()

def main():
    daemon = Thread(target=background, args=(1,), daemon=True, name = "Background")
    daemon.start()
    os.system('start cmd /k python chat.py ' + u1 + ' ' + u2)
    while True:
        x = input('You: ')
        os.system('cls')
        if (len(x) > 0):
            sendmsg(u1,u2, x)
            x = 'You: ' + x
            inputformat(x)

main()

