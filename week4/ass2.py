n = int(input("Enter n: "))
i=0
while i<n:
    i=i+1
    if i%3==0 or i == 1:
        print("!", end="")
    else:
        print("*", end="")

    