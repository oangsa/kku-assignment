pw = float(input("Enter the weight of package: "))
#Global Variables
x = 0
y = 0
z = 0

#weird processing
if pw <= 0:
    print("Invalid weight. Bye!")
    exit()

if pw >= 5:
    x = float(5 * 20)
    pw1 = pw - 5
    if pw1 >= 5:
        y = float(5 * 30)
        pw2 = pw1 - 5
        z  = float(pw2 * 40)
    else:
        z  = float(pw1 * 30)
else:   
    z  = float(pw * 20)

#print something
print("Total price: ", x + y + z)

# PASS