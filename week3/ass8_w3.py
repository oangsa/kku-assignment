a = float(input("Enter your income: "))

x = 0
y = 0
z = 0
t = 0
u = 0
i = 0
o = 0
# if a >= 0 and a <= 150000:
#     print("Tax = 0")
# elif a > 150000 and a <= 300000:
#     print("Tax = " + ("%.2f" % float(a * 5/105)))
# elif a > 300000 and a <= 500000:
#     print("Tax = " + ("%.2f" % float(a * 0.1)))
# elif a > 500000 and a <= 750000:
#     print("Tax = " + ("%.2f" % float(a * 0.15)))
# elif a > 750000 and a <= 1000000:
#     print("Tax = " + ("%.2f" % float(a * 0.2)))
# elif a > 1000000 and a <= 2000000:
#     print("Tax = " + ("%.2f" % float(a * 0.25)))
# elif a > 2000000 and a <= 5000000:
#     print("Tax = " + ("%.2f" % float(a * 0.3)))
# elif a > 5000000:
#     print("Tax = " + ("%.2f" % float(a * 0.35)))
# else:
#     print("Wrong value: negative income")

if a < 0:
    print("Invalid weight. Bye!")
    exit()

if a > 0 and a <= 150000:
    print("Tax = 0")
    
if a > 150000 and a <= 300000:
    a1 = a - 150000
    x = float(a1 * 0.05)
    if a1 >= 1:
        a2 = a1 - 200000
        y  = float(a2 * 0.1)
        if a2 >= 1:
            a3 = a2 - 250000
            z = float(a3 * 0.15)
            if a3 >= 1:
                a4  = a3 - 250000
                t = float(a4 * 0.2)
                if a4 >= 1:
                    a5 = a4 - 1000000
                    u = float(a5 * 0.25)
                    if a5 >= 1:
                        a6 = a5 - 3000000
                        i = float(a6 * 0.3)
                        if a6 >= 1:
                            o = float(a6 * 0.35)

print("Tax = " + ("%.2f" % float(x + y + z + t + u + i + o)))
                             
            
    
#trash code