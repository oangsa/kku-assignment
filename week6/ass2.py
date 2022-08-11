# x, y = map(int, input().split())

# outerList = [ ]
# for i in range(1,6):
#     innerList = [ ]
#     for j in range(1,5):
#         innerList.append(j*i)
#     outerList.append(innerList)
    
# print(outerList)

# for i in range(0,4):
#     for j in range(0,5):
#         print(outerList[i][j], end=' ')
#     print()
    
    
from audioop import reverse
from tkinter import Y


r, c = map(int, input("Enter 2D list size (row,col): ").split()) 
a = []
x = -1
for i in range(r):
    x = x + 1
    row = input("Enter {} integer(s) for row {}: ".format(c, x)).split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
    
print("In Order:")
for i in range(r):
    for j in range(c):
        print(a[i][j], end=' ')
    print()

print("Reverse Col , same row:")
l = []
for i in (a):
    l.insert(0, i[::-1])
    
x = list(reversed(l))

for i in range(r):
    for j in range(c):
        print(x[i][j], end=' ')
    print()


print("Same col, reverse row:")
y = list(reversed(a))
for i in range(r):
    for j in range(c):
        print(y[i][j], end=' ')
    print()


print("Reverse col, reverse row:")
for i in range(r):
    for j in range(c):
        print(l[i][j], end=' ')
    print()
    
#pass