from genericpath import exists
import random as rd
import secrets
import math as m
from tkinter import *
import tkinter
from tkinter import messagebox
from pymongo import MongoClient
import string
import json

with open('env.json') as d:
    dictData = json.load(d)
    cluster = MongoClient(dictData["dbURL"])

db = cluster["test"]
collection = db["test"]

class score: 
    def __init__(self, score):
        self.score = score

class user_pass:
    def __init__(self, username , password):
        self.username = username
        self.password = password
        
ez = score(0)
nm = score(0)
hd = score(0)

global exist, data
exist = exists("regData")
def destroy():
    root.destroy()
def easyStart():
    def submt(var1):
        if var1.get() == str(resultPLUS()):
            correct = Label(
                root,
                text="Correct!",
                fg="green",
                font=("Courier", 16))
            correct.place(relx=0.435, rely=0.17)
            ez.score += 1
        else:
            wrong = Label(
                root,
                text="Wrong!!!",
                fg="red",
                font=("Courier", 16))
            wrong.place(relx=0.435, rely=0.17)
            wrong_score = Label(
                root,
                text=f"You got {ez.score}!",
                fg="black",
                font=("Courier", 16))
            wrong_score.place(relx=0.413, rely=0.305)
            if exist == True:
                filter = {"username":regData.username}
                high_scores = {'$set':{"highest_scores":ez.score}}
                current_scores = {'$set':{"lastest_scores":ez.score}}
                res = collection.find_one({"username":regData.username})
                if ez.score > res["highest_scores"]:
                    collection.update_one(filter, high_scores)
                else:
                    pass
                collection.update_one(filter, current_scores)
                root.after(3000, destroy)
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
                root.after(3000, destroy)
    def try_again():
        solving.delete(0,END)
        try_again.num1update = rd.randint(0,999)
        try_again.num2update = rd.randint(0,999)
        op_choices = ["+", "-", "*", "/"]
        try_again.op_rand = secrets.choice(op_choices)
        
        if try_again.op_rand == "+":
            try_again.ans = try_again.num1update + try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} + {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "-":
            try_again.num1update = rd.randint(0,999)
            try_again.num2update = rd.randint(0,99)
            try_again.ans = try_again.num1update - try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} - {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "*":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(0,9)
            try_again.ans = try_again.num1update * try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} * {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "/":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(1,9)
            try_again.ans = ("%.2f" % (try_again.num1update / try_again.num2update))
            newQ = Label(
                root,
                text=f"{try_again.num1update} / {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


    def resultPLUS():
        try_again
        return try_again.ans

    def delete():
        solving.delete(1)

    easytext = Label(
        root,
        text = "EASY MODE",
        font = ("Comic sans MS",16,"bold"),
        background = "#ffffff")
    easytext.pack(pady=(30,0))

    start = Button(
        root,
        text = "Start",
        font = ("Courier", 16),
        command = try_again)
    start.place(relx=0.45, rely=0.2)

    solving = Entry(
        root,
        justify = "center",
        font = ("Courier", 16))
    solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

    submit = Button(
        root,
        text = "Submit",
        font = ("Courier", 16),
        command=lambda: submt(solving))
    submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

    try_again = Button(
        root,
        text = "Try Again",
        font = ("Courier", 16),
        command = try_again)
    try_again.place(relx=0.42, rely=0.9)

def normalStart():

    def submt(var1):
        if var1.get() == str(resultPLUS()):
            correct = Label(
                root,
                text="Correct!",
                fg="green",
                font=("Courier", 16))
            correct.place(relx=0.435, rely=0.17)
            nm.score += 2
        else:
            wrong = Label(
                root,
                text="Wrong!!!",
                fg="red",
                font=("Courier", 16))
            wrong.place(relx=0.435, rely=0.17)
            wrong_score = Label(
                root,
                text=f"You got {nm.score}!",
                fg="black",
                font=("Courier", 16))
            wrong_score.place(relx=0.413, rely=0.305)
            if exist == True:
                filter = {"username":regData.username}
                high_scores = {'$set':{"highest_scores":nm.score}}
                current_scores = {'$set':{"lastest_scores":nm.score}}
                res = collection.find_one({"username":regData.username})
                if nm.score > res["highest_scores"]:
                    collection.update_one(filter, high_scores)
                else:
                    pass
                collection.update_one(filter, current_scores)
                root.after(3000, destroy)
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
                root.after(3000, destroy)
            


    def try_again():
        solving.delete(0,END)
        try_again.num1update = rd.randint(0,99999)
        try_again.num2update = rd.randint(0,99999)
        op_choices = ["+", "-", "*", "/", "^"]
        try_again.op_rand = secrets.choice(op_choices)
        
        if try_again.op_rand == "+":
            try_again.ans = try_again.num1update + try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} + {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "-":
            try_again.num1update = rd.randint(0,9999)
            try_again.num2update = rd.randint(0,999)
            try_again.ans = try_again.num1update - try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} - {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "*":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(0,9)
            try_again.ans = try_again.num1update * try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} * {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "/":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(1,9)
            try_again.ans = ("%.2f" % (try_again.num1update / try_again.num2update))
            newQ = Label(
                root,
                text=f"{try_again.num1update} / {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "^":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(0,3)
            try_again.ans = try_again.num1update ** try_again.num2update
            newQ = Label(
                root,
                text=f"{try_again.num1update} ^ {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


    def resultPLUS():
        try_again
        return try_again.ans

    def delete():
        solving.delete(1)

    normaltext = Label(
        root,
        text = "NORMAL MODE",
        font = ("Comic sans MS",16,"bold"),
        background = "#ffffff")
    normaltext.pack(pady=(30,0))

    start = Button(
        root,
        text = "Start",
        font = ("Courier", 16),
        command = try_again)
    start.place(relx=0.45, rely=0.2)

    solving = Entry(
        root,
        justify = "center",
        font = ("Courier", 16))
    solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

    submit = Button(
        root,
        text = "Submit",
        font = ("Courier", 16),
        command=lambda: submt(solving))
    submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

    try_again = Button(
        root,
        text = "Try Again",
        font = ("Courier", 16),
        command = try_again)
    try_again.place(relx=0.42, rely=0.9)


def hardStart():

    def submt(var1):
        if var1.get() == str(resultPLUS()):
            correct = Label(
                root,
                text="Correct!",
                fg="green",
                font=("Courier", 16))
            correct.place(relx=0.435, rely=0.17)
            hd.score += 3
        else:
            wrong = Label(
                root,
                text="Wrong!!!",
                fg="red",
                font=("Courier", 16))
            wrong.place(relx=0.435, rely=0.17)
            wrong_score = Label(
                root,
                text=f"You got {hd.score}!",
                fg="black",
                font=("Courier", 16))
            wrong_score.place(relx=0.413, rely=0.305)
            if exist == True:
                filter = {"username":regData.username}
                high_scores = {'$set':{"highest_scores":hd.score}}
                current_scores = {'$set':{"lastest_scores":hd.score}}
                res = collection.find_one({"username":regData.username})
                if hd.score > res["highest_scores"]:
                    collection.update_one(filter, high_scores)
                else:
                    pass
                collection.update_one(filter, current_scores)
                root.after(3000, destroy)
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
                root.after(3000, destroy)


    def try_again():
        solving.delete(0,END)
        try_again.num1update = rd.randint(0,9999999)
        try_again.num2update = rd.randint(0,9999999)
        op_choices = ["+", "-", "*", "/", "^", "sqrt"]
        try_again.op_rand = secrets.choice(op_choices)
        
        if try_again.op_rand == "+":
            try_again.ans = try_again.num1update + try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} + {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "-":
            try_again.num1update = rd.randint(0,999999)
            try_again.num2update = rd.randint(0,99999)
            try_again.ans = try_again.num1update - try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} - {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "*":
            try_again.num1update = rd.randint(0,9999)
            try_again.num2update = rd.randint(0,999)
            try_again.ans = try_again.num1update * try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} * {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "/":
            try_again.num1update = rd.randint(0,9999)
            try_again.num2update = rd.randint(1,999)
            try_again.ans = ("%.2f" % (try_again.num1update / try_again.num2update))
            newQ = Label(
                root,
                text=f"{try_again.num1update} / {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "^":
            try_again.num1update = rd.randint(0,30)
            try_again.num2update = rd.randint(0,9)
            try_again.ans = try_again.num1update ** try_again.num2update
            newQ = Label(
                root,
                text=f"{try_again.num1update} ^ {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "sqrt":
            try_again.num1update = rd.randint(1,999)
            try_again.ans = ("%.2f" % (m.sqrt(try_again.num1update)))
            newQ = Label(
                root,
                text=f"√{try_again.num1update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


    def resultPLUS():
        try_again
        return try_again.ans

    def delete():
        solving.delete(1)

    hardtext = Label(
        root,
        text = "HARD MODE",
        font = ("Comic sans MS",16,"bold"),
        background = "#ffffff")
    hardtext.pack(pady=(30,0))

    start = Button(
        root,
        text = "Start",
        font = ("Courier", 16),
        command = try_again)
    start.place(relx=0.45, rely=0.2)

    solving = Entry(
        root,
        justify = "center",
        font = ("Courier", 16))
    solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

    submit = Button(
        root,
        text = "Submit",
        font = ("Courier", 16),
        command=lambda: submt(solving))
    submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

    try_again = Button(
        root,
        text = "Try Again",
        font = ("Courier", 16),
        command = try_again)
    try_again.place(relx=0.42, rely=0.9)


root = tkinter.Tk()
root.title("Super Quiz")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

def menu():
    global easy,normal,hard
    def easyIspressed():
        labeltext.destroy()
        btnStartEasy.destroy()
        btnStartNormal.destroy()
        btnStartHard.destroy()
        lblInstruction.destroy()
        easyStart()

    def normalIspressed():
        labeltext.destroy()
        btnStartEasy.destroy()
        btnStartNormal.destroy()
        btnStartHard.destroy()
        lblInstruction.destroy()
        normalStart()

    def hardIspressed():
        labeltext.destroy()
        btnStartEasy.destroy()
        btnStartNormal.destroy()
        btnStartHard.destroy()
        lblInstruction.destroy()
        hardStart()

    labeltext = Label(
        root,
        text = "Super Math Quiz",
        font = ("Comic sans MS",24,"bold"),
        background = "#ffffff"
    )
    labeltext.pack(pady=(30,10))

    easy = PhotoImage(file="easy.png")

    btnStartEasy = Button(
        root,
        image = easy,
        relief = FLAT,
        border = 0,
        command = easyIspressed,
        background = "#ffffff"
    )
    btnStartEasy.pack(pady=(10,0))

    normal = PhotoImage(file="normal.png")

    btnStartNormal = Button(
        root,
        image = normal,
        relief = FLAT,
        border = 0,
        command = normalIspressed,
        background = "#ffffff"
    )
    btnStartNormal.pack(pady=(10,0))

    hard = PhotoImage(file="hard.png")

    btnStartHard = Button(
        root,
        image = hard,
        relief = FLAT,
        border = 0,
        command = hardIspressed,
        background = "#ffffff"
    )
    btnStartHard.pack(pady=(10,20))

    lblInstruction = Label(
        root,
        text = "Math Quiz is a great way to check your math skills! \n Children pick from four math quizzes: Addition, Subtraction, Multiplication & Division.",
        font = ("Consolas",8),
        justify = "center",
        background = "#ffffff"
    )
    lblInstruction.pack()

def loginIspressed():
    
    class check_valid:
            def __init__(self, Err, err):
                self.Err = Err
                self.err = err
    myErr = check_valid(0,0)
    def logindestroy():
        global logData, username, password, log_pass
        username = logEnUsername.get()
        password = logEnPassword.get()
        logData = user_pass(username, password)
        log_pass = False
        def checklog_secure():
            global err, Err
            res = collection.find_one({"username":username})
            if collection.find_one({"username":username}):
                
                if res["password"] != password or res["username"] != username:
                    err = Label(
                    root,
                    text = "Username or Password is invalid.",
                    fg="red",
                    font = ("Courier", 16),
                    background = "#ffffff"
                    )
                    err.place(relx=0.21, rely=0.5)
                    logEnUsername.delete(0, END)
                    logEnPassword.delete(0, END)
                    myErr.err = 1
                    # print(f"myErr.err: {myErr.err}\nmyErr.Err: {myErr.Err}")
                    if myErr.Err == 1:
                        Err.destroy()
                else:
                    log_pass = True
                    return log_pass
            else:
                Err = Label(
                root,
                text = "Please enter your Username and Password.",
                fg="red",
                font = ("Courier", 16),
                background = "#ffffff"
                )
                Err.place(relx=0.13, rely=0.5)
                logEnUsername.delete(0, END)
                logEnPassword.delete(0, END)
                myErr.Err = 1
                # print(f"myErr.err: {myErr.err}\nmyErr.Err: {myErr.Err}")
                if myErr.err == 1:
                    err.destroy()
        
        if checklog_secure() == True:
            if myErr.err == 1:
                err.destroy()
            if myErr.Err == 1:
                Err.destroy()
            logusername.destroy()
            logEnUsername.destroy()
            logpassword.destroy()
            logEnPassword.destroy()
            btnGoLogin.destroy()
            menu()
        else:
            pass
        
    btnLogin.destroy()
    btnRegister.destroy()
    logusername = Label(
        root,
        text = "USERNAME:",
        font = ("Courier", 16),
        background = "#ffffff"
    )
    logusername.place(relx=0.2, rely=0.3)
    global logEnUsername, logEnPassword
    logEnUsername = Entry(
        root,
        font = ("Courier", 16))
    logEnUsername.place(relx=0.38, rely=0.3, relwidth=0.34, relheight=0.05)

    logpassword = Label(
        root,
        text = "PASSWORD:",
        font = ("Courier", 16),
        background = "#ffffff"
    )
    logpassword.place(relx=0.2, rely=0.37)

    logEnPassword = Entry(
        root,
        font = ("Courier", 16),
        show = '*'
        )

    logEnPassword.place(relx=0.38, rely=0.37, relwidth=0.34, relheight=0.05)

    btnGoLogin = Button(
        root,
        text = "LOGIN",
        font = ("Courier", 16),
        command = logindestroy,
        background = "#ffffff",
    )
    btnGoLogin.place(relx=0.42, rely=0.6)

def registerIspressed():
    class check_shit:
        def __init__(self, lenErr, numErr, lowCharErr, upperCharErr):
            self.lenErr = lenErr
            self.numErr = numErr
            self.lowCharErr = lowCharErr
            self.upperCharErr = upperCharErr
    my_shit = check_shit(0,0,0,0)
    def check_secure():
        global lenerr, Numerr, low_char_err, upper_charerr
        password = RegEnPassword.get()
        secure_pass = True
        lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
        upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
        number = any([1 if c in string.digits else 0 for c in password])        
        if len(password) < 6:
            lenerr = Label(
            root,
            text = "Password must be 6 charactors long.",
            fg="red",
            font = ("Courier", 16),
            background = "#ffffff"
            )
            lenerr.place(relx=0.263, rely=0.5)
            my_shit.lenErr = 1
            if my_shit.upperCharErr == 1:
                upper_charerr.destroy()
            if my_shit.lowCharErr == 1:
                low_char_err.destroy()
            if my_shit.numErr == 1:
                Numerr.destroy()
            secure_pass = False
            return secure_pass
        
        if number == False:
            Numerr = Label(
            root,
            text = "Password must be contain at least 1 number.",
            fg="red",
            font = ("Courier", 16),
            background = "#ffffff"
            )
            Numerr.place(relx=0.097, rely=0.5)
            my_shit.numErr = 1
            if my_shit.upperCharErr == 1:
                upper_charerr.destroy()
            if my_shit.lowCharErr == 1:
                low_char_err.destroy()
            if my_shit.lenErr == 1:
                lenerr.destroy()
            secure_pass = False
            return secure_pass

        if lower_case == False:
            low_char_err = Label(
            root,
            text = "Password must be contain at least 1 character.",
            fg="red",
            font = ("Courier", 16),
            background = "#ffffff"
            )
            low_char_err.place(relx=0.07, rely=0.5)
            my_shit.lowCharErr = 1
            if my_shit.upperCharErr == 1:
                upper_charerr.destroy()
            if my_shit.numErr == 1:
                Numerr.destroy()
            if my_shit.lenErr == 1:
                lenerr.destroy()
            secure_pass = False
            return secure_pass
        
        if upper_case == False:
            upper_charerr = Label(
            root,
            text = "Password must be contain at least 1 upper character.",
            fg="red",
            font = ("Courier", 16),
            background = "#ffffff"
            )
            upper_charerr.place(relx=0.018, rely=0.5)
            my_shit.upperCharErr = 1
            if my_shit.lowCharErr == 1:
                low_char_err.destroy()
            if my_shit.numErr == 1:
                Numerr.destroy()
            if my_shit.lenErr == 1:
                lenerr.destroy()
            secure_pass = False
            return secure_pass
        
        if my_shit.upperCharErr == 1:
                upper_charerr.destroy()
        if my_shit.lowCharErr == 1:
                low_char_err.destroy()           
        if my_shit.lenErr == 1:
                lenerr.destroy()
        if my_shit.numErr == 1:
                Numerr.destroy()
        secure_pass = True
        return secure_pass
    
    def registerdestroy():
        global regData
        regData = user_pass(RegEnUsername.get(), RegEnPassword.get())
        res = collection.find_one({"username":regData.username})
        if regData.username != "" or regData.password != "":
            if collection.find_one({"username":regData.username}):
                err = Label(
                    root,
                    text = "Username is already exist.",
                    fg="red",
                    font = ("Courier", 16),
                    background = "#ffffff"
                    )
                err.place(relx=0.263, rely=0.5)
                RegEnUsername.delete(0, END)
                RegEnPassword.delete(0, END)
            else:
                if regData.username == "" and regData != "":
                    userErr = Label(
                    root,
                    text = "Username is invalid.",
                    fg="red",
                    font = ("Courier", 16),
                    background = "#ffffff"
                    )
                    userErr.place(relx=0.263, rely=0.5)
                i = 0
                result = collection.find({})
                for x in result:
                    i = i+1
                if check_secure() == True:
                    if regData.username == "" and regData != "":
                        userErr = Label(
                        root,
                        text = "Please enter a username.",
                        fg="red",
                        font = ("Courier", 16),
                        background = "#ffffff"
                        )
                        userErr.place(relx=0.263, rely=0.5)
                    else:
                        userErr.destroy()
                        collection.insert_one({"_id":i,"username":regData.username,"password":regData.password, "highest_scores":0, "lastest_scores":0})
                        logusername.destroy()
                        RegEnUsername.destroy()
                        regpassword.destroy()
                        RegEnPassword.destroy()
                        btnGoReg.destroy()
                        messagebox.showinfo("Registered Success!")
                        menu()
        else:
            err3 = Label(
            root,
            text = "Please enter all of entry.",
            fg="red",
            font = ("Courier", 16),
            background = "#ffffff"
            )
            err3.place(relx=0.263, rely=0.5)
    
    btnLogin.destroy()
    btnRegister.destroy()
    logusername = Label(
        root,
        text = "USERNAME:",
        font = ("Courier", 16),
        background = "#ffffff"
    )
    logusername.place(relx=0.2, rely=0.3)
    global RegEnUsername, RegEnPassword
    RegEnUsername = Entry(
        root,
        font = ("Courier", 16))
    RegEnUsername.place(relx=0.38, rely=0.3, relwidth=0.34, relheight=0.05)

    regpassword = Label(
        root,
        text = "PASSWORD:",
        font = ("Courier", 16),
        background = "#ffffff"
    )
    regpassword.place(relx=0.2, rely=0.37)
    RegEnPassword = Entry(
        root,
        font = ("Courier", 16),
        show = '*'
        )
    RegEnPassword.place(relx=0.38, rely=0.37, relwidth=0.34, relheight=0.05)

    btnGoReg = Button(
        root,
        text = "REGISTER",
        font = ("Courier", 16),
        command = registerdestroy,
        background = "#ffffff",
    )
    btnGoReg.place(relx=0.42, rely=0.6)

btnLogin = Button(
    root,
    text = "LOGIN",
    font = ("Courier", 16),
    command = loginIspressed,
    background = "#ffffff"
)
btnLogin.place(relx=0.35, rely=0.15)

btnRegister = Button(
    root,
    text = "REGISTER",
    font = ("Courier", 16),
    command = registerIspressed,
    background = "#ffffff"
)
btnRegister.place(relx=0.48, rely=0.15)

root.mainloop()