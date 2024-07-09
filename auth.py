import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from threading import Thread
from sys import exit
from os import system
import re

cluster = MongoClient("mongodb+srv://neelkalpa:EUQ9gWA9M2X*T&K??HyYBXN9gjXxpVKg@socialmedia.ps81bcd.mongodb.net/?retryWrites=true&w=majority")
db = cluster["socialmedia"]["users"]

def validate_email(x,y,z):
    if (existing_email(y) == True):
        messagebox.showerror('Register',"Email already exists.")
    elif(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', y)):
        validate_password(x,y,z) 
    else:
        messagebox.showerror('Register',"Invalid email address.")


def validate_username(x,y,z):
    if (len(x) <= 2):
        messagebox.showerror('Register',"Username too short.")
    elif (existing_username(x) == True):
        messagebox.showerror('Register',"Username already exists.")
    else:
        validate_email(x,y,z)

def existing_username(x):
    s = db.find_one({"username":x})
    if (s == None):
        return False
    return True

def existing_email(x):
    s = db.find_one({"email":x})
    if (s == None):
        return False
    return True

def validate_password(x,y,z):
    if (len(z) >= 8 and len (z) <=100 and (re.search(r'[A-Z]', z) and re.search(r'[a-z]', z) and re.search(r'[0-9]', z) and re.search(r'[^A-Za-z0-9]', z))):
        create_username(x,y,z)
    messagebox.showerror('Register','Password must cointain atleast one Capital letter, one Small letter, one Number and one Special Character. Password must contain a minimum of 8 characters and maximum of 100.')
    return False

def create_username(x,y,z):
    user = ({"username":x, "email":y,"password":z})
    db.insert_one(user)
    messagebox.showerror('Register','User Registration Successful!')
    daemon = Thread(target=menu, args=(), daemon=True, name = "menu",)
    daemon.start()
    exit()

def menu():
    system("start Medialia.exe")


def check_credentials():
    x = username_entry.get()
    y = emailadd_entry.get()
    z = password_entry.get()
    validate_username(x,y,z)

def dashboard(x):
    system(x)

root = tk.Tk()
root.title('Register')
root.geometry("392x500") 

username_label = tk.Label(root, text='Username:\t\t   ')
emailadd_label = tk.Label(root, text='Email:\t\t\t   ')
password_label = tk.Label(root, text='Password:\t\t\t   ')


username_entry = tk.Entry(root)
emailadd_entry = tk.Entry(root)
password_entry = tk.Entry(root, show='*')

login_button = tk.Button(root, text='Register', relief="raised",command=check_credentials)
login_button.config(fg="#fafdfc",bg="#9076a6", font=("Times New Roman", 20), relief="ridge", height=2, width=10)
login_button.bind("<Enter>", lambda event: login_button.config(bg="#ab6d88"))
login_button.bind("<Leave>", lambda event: login_button.config(bg="#9076a6"))

root.config(bg="#1d131b")
username_label.config(fg="#fafdfc", bg="#1d131b", font=("Times New Roman", 20))
username_entry.config(fg="#fafdfc", bg="#322830", font=("Times New Roman", 20),width=25)
emailadd_label.config(fg="#fafdfc", bg="#1d131b", font=("Times New Roman", 20))
emailadd_entry.config(fg="#fafdfc", bg="#322830", font=("Times New Roman", 20),width=25)
password_label.config(fg="#fafdfc", bg="#1d131b", font=("Times New Roman", 20))
password_entry.config(fg="#fafdfc", bg="#322830", font=("Times New Roman", 20),width=25)

username_label.pack(pady = 10)
username_entry.pack(pady = 10) 
emailadd_label.pack(pady = 10)
emailadd_entry.pack(pady = 10)
password_label.pack(pady = 10)
password_entry.pack(pady = 10)
login_button.pack(pady = 50)

root.mainloop()
