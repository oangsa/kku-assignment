from pymongo import MongoClient

ask = input("Register or login: ")

cluster = MongoClient("mongodb+srv://oangsa:oangsa58528@miniproject.c9yxi6i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

username=""

def register():
    username = input("Username: ")
    password = input("Password: ")

    i = 0
    result = collection.find({})
    for x in result:
        i = i+1
        
    if collection.find_one({"username":username}):
        print("This username is already exist.")
        register()
    else:
        collection.insert_one({"_id":i,"username":username,"password":password})
        print(f'Successfully created "{username}"')
        
def login():
    username = input("Username: ")
    password = input("Password: ")
    i = 0
    res = collection.find_one({"username":username})
    result = collection.find({})
    for x in result:
        i = i+1

    if collection.find_one({"username":username}):
        while res["password"] != password or res["username"] != username :
            print("Username or password isnt match!")
            username = input("Username: ")
            password = input("Password: ")
        print(f'Logged as {res["username"]}!')
        return username
    else:
        print("This username is not exist.")
        login() 


if ask.lower() == "register" or ask.lower() == "re":
    register()
elif ask.lower() == "login" or ask.lower() == "lg":
    login()



# def reset_pass():
#     username = input("Username: ")
#     password = input("Password: ")
#     i = 0
#     res = collection.find_one({"username":username})
#     result = collection.find({})
#     for x in result:
#         i = i+1

#     if collection.find_one({"username":username}):
#         while res["password"] != password or res["username"] != username :
#             print("Username or password isnt match!")
#             username = input("Username: ")
#             password = input("Password: ")
#         print(f'Logged as {res["username"]}!')
#     else:
#         print("This username is not exist.")
#         login()
#     password = input("Password: ")
#     i = 0
#     res = collection.find_one({"username":username})
#     result = collection.find({})
#     for x in result:
#         i = i+1

#     if collection.find_one({"username":username}):
#         while res["username"] != username :
#             print("Username or password isnt match!")
#             username = input("Username: ")
#             password = input("Password: ")
#         print(f'Logged as {res["username"]}!')
#     else:
#         print("This username is not exist.")
#         login()
        

# if ask.lower() == "register" or ask.lower() == "re":
#     register()
# elif ask.lower() == "login" or ask.lower() == "lg":
#     login()