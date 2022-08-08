A = int(input("Enter a number: "))

def a(A):
    i = 0
    while i<A:
        i=i+1 
        print(i, end= " ")

def b(A):
    i = 0
    while i<A:
        i=i+1
        if (i % 10) == 1:
            print("")
        print(i, end= " ")

def c(A):
    i = 0
    while i<A:
        i=i+1
        x = str(i)
        if (i % 5) == 0:
            x = "x"
        
        print(x, end= " ")
        
        if (i % 10) == 0:
            print("")

a(A)
print("\n\n-----------------------------------------------------")
b(A)
print("\n\n-----------------------------------------------------\n")
c(A)
print("\n")

#PASS