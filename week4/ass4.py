x = int(input("Enter X: "))
i = 1
sum = 0
while sum<x:
    sum = sum + (1/i)
    y = "{:.5f}".format(sum)
    print("Round {}: sum = {}".format(i, y) , end= "\n")
    i = i+1
    
#PASS