x1, y1 = input("Enter 1st products code and price like this (code, price): ").split()
x2, y2 = input("Enter 2nd products code and price like this (code, price): ").split()
x3, y3 = input("Enter 3rd products code and price like this (code, price): ").split()
#Global Variables
t_p1 = 0
t_p2 = 0
t_p3 = 0

if "t" in x1.lower():
    t_p1 = float(float(int(y1)*7)/107)
if "t" in x2.lower():
    t_p2 = float(float(int(y2)*7)/107)
if "t" in x3.lower():
    t_p3 = float(float(int(y3)*7)/107)

p1 = float(float(y1) - t_p1)
p2 = float(float(y2) - t_p2)
p3 = float(float(y3) - t_p3)
print("Items" + '\t\t\t' + "Prices" + '\n' + x1 + '\t\t\t' + str(y1) + '\n' + x2 + '\t\t\t' + str(y2) + '\n' + x3 + '\t\t\t' + str(y3))
print("Total Price: ", ("%.2f" % float(float(y1) + float(y2) + float(y3))))
print("Total Price without tax: ", ("%.2f" % float(float(p1) + float(p2) + float(p3))))
print("Total Tax:", ("%.2f" % float(t_p1 + t_p2 + t_p3)))

# PASS