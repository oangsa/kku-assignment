from pymongo import MongoClient
import json
from tkinter import *


with open('env.json') as d:
    dictData = json.load(d)
    cluster = MongoClient(dictData["dbURL"])

db = cluster["test"]
collection = db["test"]

res = collection.find().sort("highest_scores", -1).limit(5)

lst = []

for i in res:
    u = i["username"]
    s = i["highest_scores"]
    lst.append(f"Username: {u}, Scores: {s}")

print(lst)

root = Tk()
root.title("Super Quiz")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

label = Label(
    root,
    fg="red",
    font=("Mali", 16))
label.config(text=("TOP 5 HIGHEST SCORE:\n\n"+"\n\n".join(lst)))
label.place(relx=0.280, rely=0.17)
root.mainloop()