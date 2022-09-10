from ast import Delete
import tkinter
import random as rd
from tkinter import *
import time as t

class score:
    def __init__(self, score):
        self.score = score
        
def easyStart():
    myscore = score(0)
    def submt(var1):
        if var1.get() == str(resultPLUS()):
            correct = Label(
                root,
                text="Correct!",
                fg="green",
                font=("Courier", 16))
            correct.place(relx=0.435, rely=0.17)
            myscore.score += 1
        else:
            wrong = Label(
                root,
                text="Wrong!!!",
                fg="red",
                font=("Courier", 16))
            wrong.place(relx=0.435, rely=0.17)
            total_score = Label(
                root,
                text=f'Your scores is {myscore.score}'
            )
            total_score.place(relx=0.445, rely=0.02)
            def update():
                root.destroy()   
            root.after(1500, update)
            
            
    def try_again():
        solving.delete(0, END)
        try_again.num1update = rd.randint(1,9)
        try_again.num2update = rd.randint(1,9)
        newQ = Label(
            root,
            text=f"{try_again.num1update}+{try_again.num2update}",
            font=("Courier", 16)
        )
        newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


    def resultPLUS():
        try_again
        return try_again.num1update + try_again.num2update

    start = Button(
        root,
        text="Start",
        font=("Courier", 16),
        command=try_again)
    start.place(relx=0.45, rely=0.2)

    solving = Entry(
        root,
        justify = "center",
        font=("Courier", 16))
    solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

    submit = Button(
        root,
        text="Submit",
        font=("Courier", 16),
        command=lambda: submt(solving))
    submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

    try_again = Button(
        root,
        text="Try Again",
        font=("Courier", 16),
        command=try_again)
    try_again.place(relx=0.42, rely=0.9)
    
    
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
    
def hardIspressed():
    labeltext.destroy()
    btnStartEasy.destroy()
    btnStartNormal.destroy()
    btnStartHard.destroy()
    lblInstruction.destroy()


root = tkinter.Tk()
root.title("Super Quiz")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

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

root.mainloop()