import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from threading import Thread
from sys import exit
from os import system

cluster = MongoClient("mongodb+srv://neelkalpa:EUQ9gWA9M2X*T&K??HyYBXN9gjXxpVKg@socialmedia.ps81bcd.mongodb.net/?retryWrites=true&w=majority")
db = cluster["socialmedia"]["users"]

def cred_match(x,y):
    s = db.find_one({"username":x,"password":y})
    if (s == None):
        return False
    return True
a = ""
def check_credentials():
    x = username_entry.get()
    y = password_entry.get()
    if cred_match(x,y):
        a = 'python dashboard.py ' + x
        daemon = Thread(target=dashboard, args=(a,), daemon=True, name = "dashboard",)
        daemon.start()
        exit()
    else:
        messagebox.showerror('Login', 'Wrong Username/Password')

def dashboard(x):
    system(x)

root = tk.Tk()
root.title('Login')
root.geometry("392x400") 

username_label = tk.Label(root, text='Username:\t\t   ')
password_label = tk.Label(root, text='Password:\t\t\t   ')

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show='*')

login_button = tk.Button(root, text='Login', relief="raised",command=check_credentials)
login_button.config(fg="#fafdfc",bg="#9076a6", font=("Times New Roman", 20), relief="ridge", height=2, width=10)
login_button.bind("<Enter>", lambda event: login_button.config(bg="#ab6d88"))
login_button.bind("<Leave>", lambda event: login_button.config(bg="#9076a6"))

root.config(bg="#1d131b")
username_label.config(fg="#fafdfc", bg="#1d131b", font=("Times New Roman", 20))
username_entry.config(fg="#fafdfc", bg="#322830", font=("Times New Roman", 20),width=25)
password_label.config(fg="#fafdfc", bg="#1d131b", font=("Times New Roman", 20))
password_entry.config(fg="#fafdfc", bg="#322830", font=("Times New Roman", 20),width=25)

username_label.pack(pady = 10)
username_entry.pack(pady = 10) 
password_label.pack(pady = 10)
password_entry.pack(pady = 10)
login_button.pack(pady = 50)

root.mainloop()
