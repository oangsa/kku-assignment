#Demo Without GUI
import random as rd
from pymongo import MongoClient
class score: 
    def __init__(self, score):
        self.score = score

class user_pass:
    def __init__(self, username , password):
        self.username = username
        self.password = password

    
#DB
cluster = MongoClient("mongodb+srv://oangsa:oangsa58528@miniproject.c9yxi6i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

def register():
    username = input("Username: ")
    password = input("Password: ")
    global myData
    myData = user_pass(username, password)

    i = 0
    result = collection.find({})
    for x in result:
        i = i+1
        
    if collection.find_one({"username":myData.username}):
        print("This username is already exist.")
        x = input("Do you want to login instead?(Y/N): ")
        if x.lower() == "y":
            login()
        elif x.lower() == "n":
            register()
    else:
        collection.insert_one({"_id":i,"username":myData.username,"password":myData.password, "scores":0})
        print(f'Successfully created "{username}"')
        easyMode()
      
def login():
    username = input("Username: ")
    password = input("Password: ")
    i = 0
    global myData
    myData = user_pass(username, password)
    res = collection.find_one({"username":myData.username})
    result = collection.find({})
    for x in result:
        i = i+1

    if collection.find_one({"username":myData.username}): 
        while res["password"] != password or res["username"] != username :
            print("Username or password isnt match!")
            username = input("Username: ")
            password = input("Password: ")
        print(f'Logged as {res["username"]}!')
        while True:
            quest = input("Select difficulties (easy, normal, hard) or check your best scores(score): ")
            if quest.lower() == "easy":  
                easyMode()
                break
            elif quest.lower() == "normal":
                print("You've selected a normal mode.")
                break
            elif quest.lower() == "hard":
                print("You've selected a hard mode.")
                break
            elif quest.lower() == "score":
                print(f'Your current scores is: {res["scores"]}')
    else:
        print("This username is not exist.")
        login() 


def easyMode():
    myscore = score(0)
    while True:
        choice = ["+", "-"]
        op_rand = rd.choice(choice)
        num1 = rd.randint(0,10)
        num2 = rd.randint(0,10)

        if op_rand == "+":
            ans = num1+num2
        elif op_rand == "-":
            ans = num1-num2

        user_ans = input(f'Enter the value of {num1} {op_rand} {num2}: ')
        if user_ans == "":
            print("Incorrect")
            print("Total Score(s):", myscore.score)
            break
        if int(user_ans) == ans:
            print("Correct.")
            myscore.score += 1
        else:
            filter = {"username":myData.username}
            scores = {'$set':{"scores":myscore.score}}
            res = collection.find_one({"username":myData.username})
            if myscore.score > res["scores"]:
                collection.update_one(filter, scores)
            else:
                pass
            print("Incorrect.")
            print("Total Score(s):", myscore.score)
            break

ask = input("Login or Register: ")

if ask.lower() == "login" or ask.lower() == "l":
    login()
elif ask.lower() == "register" or  ask.lower() == "re":
    register()