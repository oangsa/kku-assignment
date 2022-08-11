r, c = map(int, input("Enter 2D list size (row,col): ").split()) 
a = []
x = -1
for i in range(r):
    x = x + 1
    row = input("Enter {} integer(s) for row {}: ".format(c, x)).split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
    
print("\nIn Order:")
for i in range(r):
    for j in range(c):
        print(a[i][j], end=' ')
    print()

print("\nReverse Col , same row:")
l = []
for i in (a):
    l.insert(0, i[::-1])
    
x = list(reversed(l))

for i in range(r):
    for j in range(c):
        print(x[i][j], end=' ')
    print()


print("\nSame col, reverse row:")
y = list(reversed(a))
for i in range(r):
    for j in range(c):
        print(y[i][j], end=' ')
    print()


print("\nReverse col and row:")
for i in range(r):
    for j in range(c):
        print(l[i][j], end=' ')
    print()
    
#pass