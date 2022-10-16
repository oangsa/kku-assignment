import tkinter
import tkinter.messagebox
import customtkinter
import string, json, tkinter, secrets
import random as rd
import math as m
from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox

customtkinter.set_appearance_mode("default")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

url = "mongodb+srv://oangsa:oangsa58528@miniproject.c9yxi6i.mongodb.net/?retryWrites=true&w=majority"
cluster = MongoClient(url)

db = cluster["test"]
collection = db["test"]

class score: 
    def __init__(self, score):
        self.score = score

class user_pass:
    def __init__(self, username , password):
        self.username = username
        self.password = password

class check_shitv2:
    def __init__(self, reg):
        self.reg = reg

regis = check_shitv2(0)

ez = score(0)
nm = score(0)
hd = score(0)

def destroy():
    root.destroy()
def easyStart():
    def goback():
        if regis.reg == 1:
            filter = {"username":regData.username.lower()}
            high_scores = {'$set':{"highest_scores":ez.score}}
            current_scores = {'$set':{"lastest_scores":ez.score}}
            res = collection.find_one({"username":regData.username.lower()})
            if ez.score > res["highest_scores"]:
                collection.update_one(filter, high_scores)
            else:
                pass
            collection.update_one(filter, current_scores)
        else:
            filter = {"username":logData.username}
            high_scores = {'$set':{"highest_scores":ez.score}}
            current_scores = {'$set':{"lastest_scores":ez.score}}
            res = collection.find_one({"username":logData.username})
            if ez.score > res["highest_scores"]:
                collection.update_one(filter, high_scores)
            else:
                pass
            collection.update_one(filter, current_scores)
        solving.delete(0,END)
        correct.destroy()
        wrong.destroy()
        wrong_score.destroy()
        newQ.destroy()
        easytext.destroy()
        start.destroy()
        solving.destroy()
        submit.destroy()
        btnBack.destroy()
        menu()
        ez.score = 0

    def submt(var1):
        global correct, wrong, wrong_score
        if var1.get() == str(resultPLUS()):
            correct = customtkinter.CTkLabel(
                master=root,
                text="Correct! +1",
                text_color="#79ae61",
                fg_color=("#262626"),
                text_font= ("Courier 16 bold"))
            correct.place(relx=0.5, rely=0.17, anchor=customtkinter.CENTER)
            ez.score += 1
            root.after(500, try_again)
        else:
            wrong = customtkinter.CTkLabel(
                root,
                text="Wrong!!!",
                text_color="#c75d55",
                fg_color=("#262626"),
                text_font= ("Courier 16 bold"))
            wrong.place(relx=0.5, rely=0.17, anchor=customtkinter.CENTER)
            wrong_score = customtkinter.CTkLabel(
                root,
                text=f"You got {ez.score}!",
                text_color="white",
                fg_color=("#262626"),
                text_font= ("Courier 16 bold"))
            wrong_score.place(relx=0.5, rely=0.305, anchor=customtkinter.CENTER)
            if regis.reg == 1:
                filter = {"username":regData.username.lower()}
                high_scores = {'$set':{"highest_scores":ez.score}}
                current_scores = {'$set':{"lastest_scores":ez.score}}
                res = collection.find_one({"username":regData.username.lower()})
                if ez.score > res["highest_scores"]:
                    collection.update_one(filter, high_scores)
                else:
                    pass
                collection.update_one(filter, current_scores)
                root.after(3000, goback)
            else:
                filter = {"username":logData.username}
                high_scores = {'$set':{"highest_scores":ez.score}}
                current_scores = {'$set':{"lastest_scores":ez.score}}
                res = collection.find_one({"username":logData.username})
                if ez.score > res["highest_scores"]:
                    collection.update_one(filter, high_scores)
                else:
                    pass
                collection.update_one(filter, current_scores)
                root.after(3000, goback)
    
    def try_again():
        global newQ
        newQ.destroy()
        solving.delete(0,END)
        try_again.num1update = rd.randint(0,999)
        try_again.num2update = rd.randint(0,999)
        op_choices = ["+", "-", "*", "/"]
        try_again.op_rand = secrets.choice(op_choices)
        
        if try_again.op_rand == "+":
            try_again.ans = try_again.num1update + try_again.num2update

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} + {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

        if try_again.op_rand == "-":
            try_again.num1update = rd.randint(0,999)
            try_again.num2update = rd.randint(0,99)
            try_again.ans = try_again.num1update - try_again.num2update

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} - {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

        if try_again.op_rand == "*":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(0,9)
            try_again.ans = try_again.num1update * try_again.num2update

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} * {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

        if try_again.op_rand == "/":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(1,9)
            try_again.ans = ("%.2f" % (try_again.num1update / try_again.num2update))
            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} / {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)


    def resultPLUS():
        try_again
        return try_again.ans

    def delete():
        solving.delete(1)

    easytext = customtkinter.CTkLabel(
        master=root,
        text = "EASY MODE",
        text_font= ("Courier 16 bold"),
        text_color='#79ae61')
    easytext.pack(pady=(40,0))

    start = customtkinter.CTkButton(
        master=root,
        text = "Start",
        text_font= ("Courier 16 bold"),
        command = try_again)
    start.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

    solving = customtkinter.CTkEntry(
        master=root,
        justify = "center",
        text_font="Courier 16")
    solving.place(relx=0.5, rely=0.45, relwidth=0.34, relheight=0.13, anchor=customtkinter.CENTER)

    submit = customtkinter.CTkButton(
        master=root,
        text = "Submit",
        text_font= ("Courier 16 bold"),
        command=lambda: submt(solving))
    submit.place(relx=0.5, rely=0.6, relwidth=0.24, relheight=0.13, anchor=customtkinter.CENTER)

    btnBack = customtkinter.CTkButton(
        master= root,
        text= "Go Back",
        text_font="Courier 10",
        text_color="white",
        hover= True,
        hover_color= "black",
        height=40,
        width= 120,
        border_width=2,
        corner_radius=3,
        border_color= "black", 
        bg_color="#262626",
        fg_color= "#262626",
        command = goback)
    btnBack.place(relx=0.5, rely=0.75,anchor=customtkinter.CENTER)

    # try_again = Button(
    #     root,
    #     text = "Try Again",
    #     font = ("Courier", 16),
    #     command = try_again
    # )
    # try_again.place(relx=0.42, rely=0.9)

def normalStart():
    global try_again
    def goback():
        if regis.reg == 1:
            filter = {"username":regData.username.lower()}
            high_scores = {'$set':{"highest_scores":nm.score}}
            current_scores = {'$set':{"lastest_scores":nm.score}}
            res = collection.find_one({"username":regData.username.lower()})
            if nm.score > res["highest_scores"]:
                collection.update_one(filter, high_scores)
            else:
                pass
            collection.update_one(filter, current_scores)
        else:
            filter = {"username":logData.username}
            high_scores = {'$set':{"highest_scores":nm.score}}
            current_scores = {'$set':{"lastest_scores":nm.score}}
            res = collection.find_one({"username":logData.username})
            if nm.score > res["highest_scores"]:
                collection.update_one(filter, high_scores)
            else:
                pass
            collection.update_one(filter, current_scores)
        solving.delete(0,END)
        correct.destroy()
        wrong.destroy()
        wrong_score.destroy()
        newQ.destroy()
        normaltext.destroy()
        start.destroy()
        solving.destroy()
        submit.destroy()
        btnBack.destroy()
        menu()
        nm.score = 0

    def submt(var1):
        global correct, wrong, wrong_score
        if var1.get() == str(resultPLUS()):
            correct = customtkinter.CTkLabel(
                master=root,
                text="Correct! +2",
                text_color="#79ae61",
                fg_color=("#262626"),
                text_font= ("Courier 16 bold"))
            correct.place(relx=0.5, rely=0.17, anchor=customtkinter.CENTER)
            nm.score += 2
            root.after(500, try_again)
        else:
            wrong = customtkinter.CTkLabel(
                root,
                text="Wrong!!!",
                text_color="#c75d55",
                fg_color=("#262626"),
                text_font= ("Courier 16 bold"))
            wrong.place(relx=0.5, rely=0.17, anchor=customtkinter.CENTER)
            wrong_score = customtkinter.CTkLabel(
                root,
                text=f"You got {nm.score}!",
                text_color="white",
                fg_color=("#262626"),
                text_font= ("Courier 16 bold"))
            wrong_score.place(relx=0.5, rely=0.305, anchor=customtkinter.CENTER)
            if regis.reg == 1:
                filter = {"username":regData.username.lower()}
                high_scores = {'$set':{"highest_scores":nm.score}}
                current_scores = {'$set':{"lastest_scores":nm.score}}
                res = collection.find_one({"username":regData.username.lower()})
                if nm.score > res["highest_scores"]:
                    collection.update_one(filter, high_scores)
                else:
                    pass
                collection.update_one(filter, current_scores)
                root.after(3000, goback)
            else:
                filter = {"username":logData.username}
                high_scores = {'$set':{"highest_scores":nm.score}}
                current_scores = {'$set':{"lastest_scores":nm.score}}
                res = collection.find_one({"username":logData.username})
                if nm.score > res["highest_scores"]:
                    collection.update_one(filter, high_scores)
                else:
                    pass
                collection.update_one(filter, current_scores)
                root.after(3000, goback)
            


    def try_again():
        global newQ
        newQ.destroy()
        solving.delete(0,END)
        try_again.num1update = rd.randint(0,99999)
        try_again.num2update = rd.randint(0,99999)
        op_choices = ["+", "-", "*", "/", "^"]
        try_again.op_rand = secrets.choice(op_choices)
        
        if try_again.op_rand == "+":
            try_again.ans = try_again.num1update + try_again.num2update

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} + {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

        if try_again.op_rand == "-":
            try_again.num1update = rd.randint(0,9999)
            try_again.num2update = rd.randint(0,999)
            try_again.ans = try_again.num1update - try_again.num2update

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} - {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

        if try_again.op_rand == "*":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(0,9)
            try_again.ans = try_again.num1update * try_again.num2update

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} * {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

        if try_again.op_rand == "/":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(1,9)
            try_again.ans = ("%.2f" % (try_again.num1update / try_again.num2update))

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} / {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

        if try_again.op_rand == "^":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(0,3)
            try_again.ans = try_again.num1update ** try_again.num2update

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} ^ {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)


    def resultPLUS():
        try_again
        return try_again.ans

    def delete():
        solving.delete(1)

    normaltext = customtkinter.CTkLabel(
        master=root,
        text = "NORMAL MODE",
        text_font= ("Courier 16 bold"),
        text_color='#eda850')
    normaltext.pack(pady=(40,0))

    start = customtkinter.CTkButton(
        master=root,
        text = "Start",
        text_font= ("Courier 16 bold"),
        command = try_again)
    start.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

    solving = customtkinter.CTkEntry(
        master=root,
        justify = "center",
        text_font="Courier 16")
    solving.place(relx=0.5, rely=0.45, relwidth=0.34, relheight=0.13, anchor=customtkinter.CENTER)

    submit = customtkinter.CTkButton(
        master=root,
        text = "Submit",
        text_font= ("Courier 16 bold"),
        command=lambda: submt(solving))
    submit.place(relx=0.5, rely=0.6, relwidth=0.24, relheight=0.13, anchor=customtkinter.CENTER)

    btnBack = customtkinter.CTkButton(
        master= root,
        text= "Go Back",
        text_font="Courier 10",
        text_color="white",
        hover= True,
        hover_color= "black",
        height=40,
        width= 120,
        border_width=2,
        corner_radius=3,
        border_color= "black", 
        bg_color="#262626",
        fg_color= "#262626",
        command = goback)
    btnBack.place(relx=0.5, rely=0.75,anchor=customtkinter.CENTER)

    # try_again = Button(
    #     root,
    #     text = "Try Again",
    #     font = ("Courier", 16),
    #     command = try_again)
    # try_again.place(relx=0.42, rely=0.9)


def hardStart():
    global try_again
    def goback():
        if regis.reg == 1:
            filter = {"username":regData.username.lower()}
            high_scores = {'$set':{"highest_scores":hd.score}}
            current_scores = {'$set':{"lastest_scores":hd.score}}
            res = collection.find_one({"username":regData.username.lower()})
            if hd.score > res["highest_scores"]:
                collection.update_one(filter, high_scores)
            else:
                pass
            collection.update_one(filter, current_scores)
        else:
            filter = {"username":logData.username}
            high_scores = {'$set':{"highest_scores":hd.score}}
            current_scores = {'$set':{"lastest_scores":hd.score}}
            res = collection.find_one({"username":logData.username})
            if hd.score > res["highest_scores"]:
                collection.update_one(filter, high_scores)
            else:
                pass
            collection.update_one(filter, current_scores)
        solving.delete(0,END)
        correct.destroy()
        wrong.destroy()
        wrong_score.destroy()
        newQ.destroy()
        hardtext.destroy()
        start.destroy()
        solving.destroy()
        submit.destroy()
        btnBack.destroy()
        menu()
        hd.score = 0

    def submt(var1):
        global correct, wrong, wrong_score
        if var1.get() == str(resultPLUS()):
            correct = customtkinter.CTkLabel(
                master=root,
                text="Correct! +3",
                text_color="#79ae61",
                fg_color=("#262626"),
                text_font= ("Courier 16 bold"))
            correct.place(relx=0.5, rely=0.17, anchor=customtkinter.CENTER)
            hd.score += 3
            root.after(500, try_again)
        else:
            wrong = customtkinter.CTkLabel(
                root,
                text="Wrong!!!",
                text_color="#c75d55",
                fg_color=("#262626"),
                text_font= ("Courier 16 bold"))
            wrong.place(relx=0.5, rely=0.17, anchor=customtkinter.CENTER)
            wrong_score = customtkinter.CTkLabel(
                root,
                text=f"You got {hd.score}!",
                text_color="white",
                fg_color=("#262626"),
                text_font= ("Courier 16 bold"))
            wrong_score.place(relx=0.5, rely=0.305, anchor=customtkinter.CENTER)
            if regis.reg == 1:
                filter = {'username':regData.username.lower()}
                high_scores = {'$set':{"highest_scores":hd.score}}
                current_scores = {'$set':{"lastest_scores":hd.score}}
                res = collection.find_one({"username":regData.username.lower()})
                if hd.score > res["highest_scores"]:
                    collection.update_one(filter, high_scores)
                else:
                    pass
                collection.update_one(filter, current_scores)
                root.after(3000, goback)
            else:
                filter = {"username":logData.username}
                high_scores = {'$set':{"highest_scores":hd.score}}
                current_scores = {'$set':{"lastest_scores":hd.score}}
                res = collection.find_one({"username":logData.username})
                if hd.score > res["highest_scores"]:
                    collection.update_one(filter, high_scores)
                else:
                    pass
                collection.update_one(filter, current_scores)
                root.after(3000, goback)


    def try_again():
        global newQ
        newQ.destroy()
        solving.delete(0,END)
        try_again.num1update = rd.randint(0,9999999)
        try_again.num2update = rd.randint(0,9999999)
        op_choices = ["+", "-", "*", "/", "^", "sqrt"]
        try_again.op_rand = secrets.choice(op_choices)
        
        if try_again.op_rand == "+":
            try_again.ans = try_again.num1update + try_again.num2update

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} + {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

        if try_again.op_rand == "-":
            try_again.num1update = rd.randint(0,999999)
            try_again.num2update = rd.randint(0,99999)
            try_again.ans = try_again.num1update - try_again.num2update

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} - {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

        if try_again.op_rand == "*":
            try_again.num1update = rd.randint(0,9999)
            try_again.num2update = rd.randint(0,999)
            try_again.ans = try_again.num1update * try_again.num2update

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} * {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

        if try_again.op_rand == "/":
            try_again.num1update = rd.randint(0,9999)
            try_again.num2update = rd.randint(1,999)
            try_again.ans = ("%.2f" % (try_again.num1update / try_again.num2update))

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} / {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)
        if try_again.op_rand == "^":
            try_again.num1update = rd.randint(0,30)
            try_again.num2update = rd.randint(0,9)
            try_again.ans = try_again.num1update ** try_again.num2update

            newQ = customtkinter.CTkLabel(
                root,
                text=f"{try_again.num1update} ^ {try_again.num2update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

        if try_again.op_rand == "sqrt":
            try_again.num1update = rd.randint(1,999)
            try_again.ans = ("%.2f" % (m.sqrt(try_again.num1update)))
            newQ = customtkinter.CTkLabel(
                root,
                text=f"√{try_again.num1update}",
                fg_color=("#262626"),
                corner_radius=6,
                text_font= ("Courier 16 bold")
            )
            newQ.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

    def resultPLUS():
        try_again
        return try_again.ans

    def delete():
        solving.delete(1)

    hardtext = customtkinter.CTkLabel(
        master=root,
        text = "HARD MODE",
        text_font= ("Courier 16 bold"),
        text_color='#c75d55')
    hardtext.pack(pady=(40,0))

    start = customtkinter.CTkButton(
        master=root,
        text = "Start",
        text_font= ("Courier 16 bold"),
        command = try_again)
    start.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

    solving = customtkinter.CTkEntry(
        master=root,
        justify = "center",
        text_font="Courier 16")
    solving.place(relx=0.5, rely=0.45, relwidth=0.34, relheight=0.13, anchor=customtkinter.CENTER)

    submit = customtkinter.CTkButton(
        master=root,
        text = "Submit",
        text_font= ("Courier 16 bold"),
        command=lambda: submt(solving))
    submit.place(relx=0.5, rely=0.6, relwidth=0.24, relheight=0.13, anchor=customtkinter.CENTER)

    btnBack = customtkinter.CTkButton(
        master= root,
        text= "Go Back",
        text_font="Courier 10",
        text_color="white",
        hover= True,
        hover_color= "black",
        height=40,
        width= 120,
        border_width=2,
        corner_radius=3,
        border_color= "black", 
        bg_color="#262626",
        fg_color= "#262626",
        command = goback)
    btnBack.place(relx=0.5, rely=0.75,anchor=customtkinter.CENTER)
'''
    try_again = Button(
        root,
        text = "Try Again",
        font = ("Courier", 16),
        command = try_again)
    try_again.place(relx=0.42, rely=0.9)
'''

def leaderStart():

    def goback():
        leadtext.destroy()
        leaderboard.destroy()
        userb.destroy()
        scoreb.destroy()
        btnBack.destroy()
        score.destroy()
        menu()
    

    if regis.reg == 1:
        leadres = collection.find_one({"username":regData.username.lower()})
    else:
        leadres = collection.find_one({"username":logData.username})

    res = collection.find().sort("highest_scores", -1).limit(7)
    rank = 0
    lst = []
    for i in res:
        u = i["username"]
        s = i["highest_scores"]
        rank += 1
        tab = "\t\t"
        lst.append(f"{rank}. name: {u}{tab}Scores: {s}")

    leadtext = customtkinter.CTkLabel(
        root,
        text = "LEADERBOARD",
        text_font= ("Courier 30 bold"),
        text_color='#eda850'
    )
    leadtext.pack(pady=(60,30))

    leaderboard = customtkinter.CTkLabel(
        root,
        text=("\n".join(lst)),
        text_font= ("Courier 16"),
        text_color='#eda850',
        fg_color=("#262626"),
        corner_radius=6,
        justify=tkinter.LEFT)
    leaderboard.place(relx=0.5, rely=0.5, relwidth=1, relheight=0.5, anchor=customtkinter.CENTER)

    cs = leadres["lastest_scores"]
    hs = leadres["highest_scores"]
    
    score = customtkinter.CTkLabel(
        root,
        text=(f"Your Current Scores: {cs}{tab} Your Highest Scores: {hs}"),
        text_font= ("Courier 10 bold"),
        text_color='#262626',
        fg_color=("#eda850"),
        corner_radius=6,
        justify=tkinter.LEFT)
    score.place(relx=0.5, rely=0.9, relwidth=1, relheight=0.2, anchor=customtkinter.CENTER)

    userb = customtkinter.CTkLabel(
        root,
        text=("User"),
        text_font= ("Courier 20 bold"),
        text_color='white',
        fg_color=("#262626"),
        corner_radius=6)
    userb.place(relx=0.2, rely=0.28)

    scoreb = customtkinter.CTkLabel(
        root,
        text=("Score"),
        text_font= ("Courier 20 bold"),
        text_color='white',
        fg_color=("#262626"),
        corner_radius=6)
    scoreb.place(relx=0.6, rely=0.28)

    btnBack = customtkinter.CTkButton(
        master= root,
        text= "Go Back",
        text_font="Courier 10",
        text_color="white",
        hover= True,
        hover_color= "black",
        height=40,
        width= 120,
        border_width=2,
        corner_radius=3,
        border_color= "black", 
        bg_color="#262626",
        fg_color= "#262626",
        command = goback)
    btnBack.place(relx=0.5, rely=0.7,anchor=customtkinter.CENTER)



root = customtkinter.CTk()
root.title("Super Quiz")
root.geometry("700x600")
root.resizable(0,0)

def menu():
    global easy,normal,hard
    def easyIspressed():
        labeltext.destroy()
        btnStartEasy.destroy()
        btnStartNormal.destroy()
        btnStartHard.destroy()
        lblInstruction.destroy()
        btnStartLeader.destroy()
        btnLogout.destroy()
        lblrule.destroy()
        easyStart()

    def normalIspressed():
        labeltext.destroy()
        btnStartEasy.destroy()
        btnStartNormal.destroy()
        btnStartHard.destroy()
        lblInstruction.destroy()
        btnStartLeader.destroy()
        btnLogout.destroy()
        lblrule.destroy()
        normalStart()

    def hardIspressed():
        labeltext.destroy()
        btnStartEasy.destroy()
        btnStartNormal.destroy()
        btnStartHard.destroy()
        lblInstruction.destroy()
        btnStartLeader.destroy()
        btnLogout.destroy()
        lblrule.destroy()
        hardStart()

    def leaderIspressed():
        labeltext.destroy()
        btnStartEasy.destroy()
        btnStartNormal.destroy()
        btnStartHard.destroy()
        lblInstruction.destroy()
        btnStartLeader.destroy()
        btnLogout.destroy()
        lblrule.destroy()
        leaderStart()

    def logoutIspressed():
        labeltext.destroy()
        btnStartEasy.destroy()
        btnStartNormal.destroy()
        btnStartHard.destroy()
        lblInstruction.destroy()
        btnStartLeader.destroy()
        btnLogout.destroy()
        lblrule.destroy()
        loginmenu()

    labeltext = customtkinter.CTkLabel(
        root,
        text = "Super Math Quiz",
        text_font= ("Courier 30 bold"),
        text_color='#738ADB'
    )
    labeltext.pack(pady=(50,30))


    btnStartEasy = customtkinter.CTkButton(
        master= root,
        text= "EASY ★",
        text_font="none 10",
        text_color="white",
        hover= True,
        hover_color= "#79ae61",
        height=40,
        width= 120,
        border_width=2,
        corner_radius=3,
        border_color= "#79ae61", 
        bg_color="#262626",
        fg_color= "#262626",
        command = easyIspressed)

    btnStartEasy.pack(pady=(10,0))

    btnStartNormal = customtkinter.CTkButton(
        master= root,
        text= "NORMAL ★★",
        text_font="none 10",
        text_color="white",
        hover= True,
        hover_color= "#eda850",
        height=40,
        width= 120,
        border_width=2,
        corner_radius=3,
        border_color= "#eda850", 
        bg_color="#262626",
        fg_color= "#262626",
        command = normalIspressed)
    btnStartNormal.pack(pady=(10,0))

    btnStartHard = customtkinter.CTkButton(
        master= root,
        text= "HARD ★★★",
        text_font="none 10",
        text_color="white",
        hover= True,
        hover_color= "#c75d55",
        height=40,
        width= 120,
        border_width=2,
        corner_radius=3,
        border_color= "#c75d55", 
        bg_color="#262626",
        fg_color= "#262626",
        command = hardIspressed)

    btnStartHard.pack(pady=(10,0))

    btnStartLeader = customtkinter.CTkButton(
        master= root,
        text= "LEADERBOARD",
        text_font="none 10",
        text_color="white",
        hover= True,
        hover_color= "black",
        height=40,
        width= 120,
        border_width=2,
        corner_radius=3,
        border_color= "black", 
        bg_color="#262626",
        fg_color= "#262626",
        command = leaderIspressed)
    btnStartLeader.pack(pady=(10,50))

    lblInstruction = customtkinter.CTkLabel(
        root,
        text = "Math Quiz is a great way to check your math skills! \n Children pick from four math quizzes: Addition, Subtraction, Multiplication & Division.",
        text_font="Consolas 8"
    )
    lblInstruction.pack(pady=(10,10))

    lblrule = customtkinter.CTkLabel(
        root,
        text = "WARNING! in every divisions and mutiplications questions, you need to answer with 2 decimals",
        text_color="#c75d55",
        text_font="Consolas 8"
    )
    lblrule.pack(pady=(2,10))

    btnLogout = customtkinter.CTkButton(
        master= root,
        text= "LOGOUT",
        text_font="none 10",
        text_color="white",
        hover= True,
        hover_color= "#c75d55",
        height=40,
        width= 120,
        border_width=2,
        corner_radius=3,
        border_color= "#c75d55", 
        bg_color="#262626",
        fg_color= "#262626",
        command = logoutIspressed)
    btnLogout.pack(pady=(10,50))

def loginIspressed():
    def logindestroy():
        global logData, username, password, log_pass
        username = logEnUsername.get().lower()
        password = logEnPassword.get()
        logData = user_pass(username, password)
        log_pass = False
        def checklog_secure():
            global err, Err
            res = collection.find_one({"username":username})
            if collection.find_one({"username":username}):
                
                if res["password"] != password or res["username"] != username:
                    messagebox.showerror(title="Error", message="Password is not match or Username is invalid.")
                    logEnUsername.delete(0, END)
                    logEnPassword.delete(0, END)
                else:
                    log_pass = True
                    return log_pass
            else:
                messagebox.showerror(title="Error", message="Username or Password is invalid")
                logEnUsername.delete(0, END)
                logEnPassword.delete(0, END)
        
        if checklog_secure() == True:
            logusername.destroy()
            logEnUsername.destroy()
            logpassword.destroy()
            logEnPassword.destroy()
            btnGoLogin.destroy()
            # messagebox.showinfo(title="Success", message="Loggedin Success!")
            menu()

    btnLogin.destroy()
    btnRegister.destroy()
    newQ.destroy()
    correct.destroy()
    wrong.destroy()
    wrong_score.destroy()
    logusername = customtkinter.CTkLabel(
        root,
        text_font="Courier 12",
        text = "USERNAME :",
    )
    logusername.place(relx=0.2, rely=0.3)
    global logEnUsername, logEnPassword
    logEnUsername = customtkinter.CTkEntry(
        root)
    logEnUsername.place(relx=0.38, rely=0.3, relwidth=0.34, relheight=0.05)

    logpassword = customtkinter.CTkLabel(
        root,
        text_font="Courier 12",
        text = "PASSWORD :",
    )
    logpassword.place(relx=0.2, rely=0.37)

    logEnPassword = customtkinter.CTkEntry(
        root,
        show = '*',
        text_font="Courier 12",
        )

    logEnPassword.place(relx=0.38, rely=0.37, relwidth=0.34, relheight=0.05)

    btnGoLogin = customtkinter.CTkButton(
        root,
        text = "LOGIN",
        text_font="Courier 12 bold",
        command = logindestroy,
    )
    btnGoLogin.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

def registerIspressed():
    def check_secure():
        password = RegEnPassword.get()
        secure_pass = True
        lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
        upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
        number = any([1 if c in string.digits else 0 for c in password])        
        if len(password) < 6:
            messagebox.showerror(title="Error", message="Password must be at least 6 characters long.")
            secure_pass = False
            return secure_pass
        
        if number == False:
            messagebox.showerror(title="Error", message="Password must be contain at least 1 number.")
            secure_pass = False
            return secure_pass

        if lower_case == False:
            messagebox.showerror(title="Error", message="Password must be contain at least 1 character.")
            secure_pass = False
            return secure_pass
        
        if upper_case == False:
            messagebox.showerror(title="Error", message="Password must be contain at least 1 upper character.")
            secure_pass = False
            return secure_pass
        secure_pass = True
        return secure_pass
    def registerdestroy():
        global regData
        regData = user_pass(RegEnUsername.get(), RegEnPassword.get())
        if regData.username != "" or regData.password != "":
            if collection.find_one({"username":regData.username.lower()}):
                messagebox.showerror(title="Error", message="Username is already exist.")
                RegEnUsername.delete(0, END)
                RegEnPassword.delete(0, END)
            else:
                if regData.username == "" and regData != "":
                    messagebox.showerror(title="Error", message="Username is invalid.")
                i = 0
                result = collection.find({})
                for x in result:
                    i = i+1
                if check_secure() == True:
                    if regData.username == "" and regData != "":
                        messagebox.showerror(title="Error", message="Username is invalid.")
                    else:
                        regis.reg = 1
                        collection.insert_one({"_id":i,"username":regData.username.lower(),"password":regData.password, "highest_scores":0, "lastest_scores":0})
                        logusername.destroy()
                        RegEnUsername.destroy()
                        regpassword.destroy()
                        RegEnPassword.destroy()
                        btnGoReg.destroy()
                        messagebox.showinfo(title="Success", message="Registered success!")
                        menu()
        else:
            messagebox.showerror(title="Error", message="Please enter all of entry")

    
    btnLogin.destroy()
    btnRegister.destroy()
    newQ.destroy()
    correct.destroy()
    wrong.destroy()
    wrong_score.destroy()
    logusername = customtkinter.CTkLabel(
        root,
        text_font="Courier 12",
        text = "USERNAME :",
    )
    logusername.place(relx=0.2, rely=0.3)
    global RegEnUsername, RegEnPassword
    RegEnUsername = customtkinter.CTkEntry(
        root,
        text_font="Courier 12")
    RegEnUsername.place(relx=0.38, rely=0.3, relwidth=0.34, relheight=0.05)

    regpassword = customtkinter.CTkLabel(
        root,
        text_font="Courier 12",
        text = "PASSWORD :",
    )
    regpassword.place(relx=0.2, rely=0.37)

    RegEnPassword = customtkinter.CTkEntry(
        root,
        show = '*',
        text_font="Courier 12",
        )
    RegEnPassword.place(relx=0.38, rely=0.37, relwidth=0.34, relheight=0.05)


    btnGoReg = customtkinter.CTkButton(
        root,
        text = "REGISTER",
        text_font="Courier 12 bold",
        command = registerdestroy,
    )
    btnGoReg.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

def loginmenu():
    global btnLogin, btnRegister, newQ, correct, wrong, wrong_score
    btnLogin = customtkinter.CTkButton(
        master=root,
        text = "LOGIN",
        text_font="Courier 12 bold",
        command = loginIspressed,
    )
    btnLogin.place(relx=0.35, rely=0.15, relwidth=0.12, relheight=0.05)

    btnRegister = customtkinter.CTkButton(
        master=root,
        text = "REGISTER",
        text_font="Courier 12 bold",
        command = registerIspressed,
    )
    btnRegister.place(relx=0.48, rely=0.15, relwidth=0.14, relheight=0.05)

    newQ = customtkinter.CTkLabel(
        root,
        text=f"Super Quiz V6.9", 
        fg_color=("#262626"),
        corner_radius=6,
        text_font= ("Courier 16 bold")
    )
    newQ.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.23, anchor=customtkinter.CENTER)

    correct = customtkinter.CTkLabel(
        master=root,
        text="",
        text_color="#79ae61",
        fg_color=("#262626"),
        text_font= ("Courier 16 bold"))
    correct.place(relx=0.5, rely=0.55, relwidth=0.1, relheight=0.05, anchor=customtkinter.CENTER)

    wrong = customtkinter.CTkLabel(
        master=root,
        text="",
        text_color="#79ae61",
        fg_color=("#262626"),
        text_font= ("Courier 16 bold"))
    wrong.place(relx=0.5, rely=0.55, relwidth=0.1, relheight=0.05, anchor=customtkinter.CENTER)

    wrong_score = customtkinter.CTkLabel(
        master=root,
        text="",
        text_color="#79ae61",
        fg_color=("#262626"),
        text_font= ("Courier 16 bold"))
    wrong_score.place(relx=0.5, rely=0.55, relwidth=0.1, relheight=0.05, anchor=customtkinter.CENTER)



loginmenu()
root.mainloop()