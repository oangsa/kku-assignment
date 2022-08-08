from random import randint
value = randint(0,99)

def getInput():
    while True:
        user_input = int(input("Enter a number: "))
        if user_input < 100:
            break
    return user_input

user_input = getInput()

def checkInput(user_input, value):
    if user_input == value:
        print("Congratulations!")
    elif user_input - value <= 10 and user_input - value >= -10:
        print("Almost got it")
    else:
        print("No, sorry :(")
    
checkInput(user_input, value)
print("Lottery number: ", value)

#pass