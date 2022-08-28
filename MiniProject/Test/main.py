import random as rd
import secrets
import math as m

normal = True
hard = True
easy = True

ez = False
nor = False
hd = False

score = 0

def select_mode(ez, nor, hd):
    while True:
        user_input = input("Please select a difficulty(easy(ez), normal(n), hard(h)) / q to exit: ")
        
        f_user_input = user_input.lower()
        
        
        if f_user_input == "easy" or f_user_input == "ez":
            ez = True
        elif f_user_input == "normal" or f_user_input == "n":
            nor = True
        elif f_user_input == "hard" or f_user_input == "h":
            hd = True
        elif f_user_input == "q" or f_user_input == "quit":
            print("Stopped.")
            exit
        else:
            continue
        
        return ez, nor, hd


def easy_mode(easy, score):
    op_choices = ["+", "-", "*", "/"]
    op_rand = secrets.choice(op_choices)
    while easy == True:
        ran_n1 = rd.randint(0,9999)
        ran_n2 = rd.randint(0,9999)

        op_rand = secrets.choice(op_choices)
    
        if op_rand == "+":
            ans = ("%.2f" % (ran_n1 + ran_n2))

        if op_rand == "-":
            ans = ("%.2f" % (ran_n1 - ran_n2))

        if op_rand == "*":
            ran_n1 = rd.randint(0,99)
            ran_n2 = rd.randint(0,9)
            ans = ("%.2f" % (ran_n1 * ran_n2))

        if op_rand == "/":
            ran_n1 = rd.randint(0,99)
            ran_n2 = rd.randint(1,9)
            ans = ("%.2f" % (ran_n1 / ran_n2))
        
        print(f'What is the answer of {ran_n1} {op_rand} {ran_n2}')
        
        #Deal with input error
        try:
            user_ans = ("%.2f" % float(input("Enter your answer(2 digits decimal): ")))
        except ValueError:
            print("Please provide me a number.")
            continue
        
        # print(f'Original ans: {ans} \nUser ans: {user_ans}')
        
        if ans == user_ans:
            score = score+1
            print("Correct")
        else:
            easy = False
            print("Not Correct")
            print("Total scores:", score)


def normal_mode(normal, score):
    op_choices = ["+", "-", "*", "/", "^"]
    op_rand = secrets.choice(op_choices)
    while normal == True:
        ran_n1 = rd.randint(0,999999)
        ran_n2 = rd.randint(0,999999)

        op_rand = secrets.choice(op_choices)
    
        if op_rand == "+":
            ans = ("%.2f" % (ran_n1 + ran_n2))

        if op_rand == "-":
            ans = ("%.2f" % (ran_n1 - ran_n2))

        if op_rand == "*":
            ran_n1 = rd.randint(0,99)
            ran_n2 = rd.randint(0,99)
            ans = ("%.2f" % (ran_n1 * ran_n2))

        if op_rand == "/":
            ran_n1 = rd.randint(0,99)
            ran_n2 = rd.randint(1,99)
            ans = ("%.2f" % (ran_n1 / ran_n2))
            
        if op_rand == "^":
            ran_n1 = rd.randint(0,99)
            ran_n2 = rd.randint(0,3)
            ans = ("%.2f" % (ran_n1 ** ran_n2))
        
        print(f'What is the answer of {ran_n1} {op_rand} {ran_n2}')
        
        #Deal with input error
        try:
            user_ans = ("%.2f" % float(input("Enter your answer(2 digits decimal): ")))
        except ValueError:
            print("Please provide me a number.")
            continue
        
        # print(f'Original ans: {ans} \nUser ans: {user_ans}')
        
        if ans == user_ans:
            score = score+2
            print("Correct")
        else:
            normal = False
            print("Not Correct")
            print("Total scores:", score)


def hard_mode(hard, score):
    sqrt = 0
    op_choices = ["+", "-", "*", "/", "^", "sqrt"]
    op_rand = secrets.choice(op_choices)
    while hard == True:
        ran_n1 = rd.randint(0,99999999)
        ran_n2 = rd.randint(0,99999999)

        op_rand = secrets.choice(op_choices)
    
        if op_rand == "+":
            ans = ("%.2f" % (ran_n1 + ran_n2))

        if op_rand == "-":
            ans = ("%.2f" % (ran_n1 - ran_n2))

        if op_rand == "*":
            ran_n1 = rd.randint(0,9999)
            ran_n2 = rd.randint(0,999)
            ans = ("%.2f" % (ran_n1 * ran_n2))

        if op_rand == "/":
            ran_n1 = rd.randint(0,9999)
            ran_n2 = rd.randint(1,999)
            ans = ("%.2f" % (ran_n1 / ran_n2))
            
        if op_rand == "^":
            ran_n1 = rd.randint(0,999)
            ran_n2 = rd.randint(0,9)
            ans = ("%.2f" % (ran_n1 ** ran_n2))
            
        if op_rand == "sqrt":
            ran_n1 = rd.randint(1,999)
            ans = ("%.2f" % (m.sqrt(ran_n1)))
            sqrt = 1
        
        if sqrt == 1:
            print(f'What is the answer of √{ran_n1}')
        else:
            print(f'What is the answer of {ran_n1} {op_rand} {ran_n2}')
        
        #Deal with input error
        try:
            user_ans = ("%.2f" % float(input("Enter your answer(2 digits decimal): ")))
        except ValueError:
            print("Please provide me a number.")
            continue
        
        # print(f'Original ans: {ans} \nUser ans: {user_ans}')
        
        if ans == user_ans:
            score = score+3
            print("Correct")
        else:
            hard = False
            print("Not Correct")
            print("Total scores:", score)
        sqrt = 0

check_mode = select_mode(ez, nor, hd)
ez, nor, hd = check_mode[0], check_mode[1], check_mode[2]

if ez == True:
    easy_mode(easy, score)

elif nor == True:
    normal_mode(normal, score)
    
elif hd == True:
    hard_mode(hard, score)