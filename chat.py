import os
import sys
from time import sleep

def displaymessages(x,y):
    os.system('cls')
    f = open('data'+x+y+'.txt', 'r')
    s = [line.rstrip() for line in f]
    f.close()
    while (len(s) > 100):
        s.pop(0)
    for x in s:
        if (x == '' or x == '\n'):
            continue
        print(x)


def chat():
    x = str(sys.argv[1])
    y = str(sys.argv[2])
    while True:
        sleep (1)
        displaymessages(x,y)
chat()


