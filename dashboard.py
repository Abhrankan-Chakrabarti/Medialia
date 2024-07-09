import glob
import sys
import os
from pymongo import MongoClient

def dasboard():
    user = str(sys.argv[1])
    while True:
        chats = chatlist(user)
        for x in range (1, len(chats)+2):
            if (x == 1):
                print ('1. Add new friend')
            else:
                print (str(x) + '. Chat with ' + str(chats[x-2])[4:-4].replace(user,'',1))
        x = int(input('Enter your choice: '))
        if (x == 1):
            newfriend(user)
        elif (x < len(chats)+2):
            os.system('python sender.py ' + user + ' ' + str(chats[x-2])[4:-4].replace(user,'',1))
        os.system('cls')


def chatlist(x):
    chats = glob.glob("data"+x+"*.txt")
    return chats

def newfriend(x):
    y = input ('Enter username to chat with : ').lower()
    if existing_username(y):
        os.system ('type nul > data'+x+y+'.txt')
        os.system ('type nul > temp'+x+y+'.txt')
        f = open('temp'+x+y+'.txt', 'w')
        f.write('00/00/00' + '\n')
        f.write('00:00:00')
        f.close()
    else:
        print ("User doesn't exist.")

def existing_username(x):
    cluster = MongoClient("mongodb+srv://neelkalpa:EUQ9gWA9M2X*T&K??HyYBXN9gjXxpVKg@socialmedia.ps81bcd.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["socialmedia"]["users"]
    s = db.find_one({"username":x})
    if (s == None):
        return False
    return True

dasboard()
