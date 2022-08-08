n = int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if col == row or col == n-1-row:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#PASS