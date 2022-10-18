# from pymongo import MongoClient
# import json
# from tkinter import *


# with open('env.json') as d:
#     dictData = json.load(d)
#     cluster = MongoClient(dictData["dbURL"])

# db = cluster["test"]
# collection = db["test"]

# res = collection.find().sort("highest_scores", -1).limit(5)

# lst = []

# for i in res:
#     u = i["username"]
#     s = i["highest_scores"]
#     lst.append(f"Username: {u}, Scores: {s}")

# print(lst)

# root = Tk()
# root.title("Super Quiz")
# root.geometry("700x600")
# root.config(background="#ffffff")
# root.resizable(0,0)

# label = Label(
#     root,
#     fg="red",
#     font=("Mali", 16))

# label.config(text=("TOP 5 HIGHEST SCORE:\n\n"+"\n\n".join(lst)))
# label.place(relx=0.280, rely=0.17)
# root.mainloop()

# import threading
# import sched, time

# flag = True

# def printit():
#     while(flag):
#         time.sleep(5)
#         print("Hello, world!")  
  
# t = threading.Thread(target=printit)
# t.start()

# x=25

# while x>1:
#     time.sleep(1)
#     print(x)
#     x=x-1 

# flag = False

from tkinter import *
import webbrowser

# Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")

def sayhello():
    print("Hello")

# Create a Label Widget
label= Label(win, text= "Welcome to TutorialsPoint", cursor= "hand2", foreground= "green", font= ('Aerial 18 underline'))
label.pack(pady= 30)

# Define the URL to open
# url= 'https://www.tutorialspoint.com/'

# Bind the label with the URL to open in a new tab
label.bind("<Button-1>", lambda _:sayhello())
win.mainloop()