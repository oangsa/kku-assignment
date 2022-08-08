x1, y1 = input("Enter products code and price like this (code, price): ").split()
x2, y2 = input("Enter products code and price like this (code, price): ").split()
x3, y3 = input("Enter products code and price like this (code, price): ").split()
t_p1 = 0
t_p2 = 0
t_p3 = 0


if "t" in x1.lower() or "t" in x2.lower() or "t" in x3.lower():
    if "t" in x1.lower():
        t_p1 = float(y1) * 0.07
    elif "t" in x2.lower():
        t_p2 = float(y2) * 0.07
    elif "t" in x3.lower():
        t_p3 = float(y3) * 0.07
    
    p1 = float(float(y1) + t_p1)
    p2 = float(float(y2) + t_p2)
    p3 = float(float(y3) + t_p3)
    print("Items" + '\t\t\t' + "Prices" + '\n' + x1 + '\t\t\t' + str(p1) + '\n' + x2 + '\t\t\t' + str(p2) + '\n' + x3 + '\t\t\t' + str(p3) + '\n' + "Total price: " + str(float(p1 + p2 + p3)))
    print("Total Price without tax: ", float(y1) + float(y2) + float(y3))
    print("Total Tax:", t_p1 + t_p2 + t_p3)
    print("Total Price with tax: ", float(y1) + float(y2) + float(y3) + t_p1 + t_p2 + t_p3)
else:

    p1 = float(float(y1) + t_p1)
    p2 = float(float(y2) + t_p2)
    p3 = float(float(y3) + t_p3)
    print("Items" + '\t\t\t' + "Prices" + '\n' + x1 + '\t\t\t' + str(p1) + '\n' + x2 + '\t\t\t' + str(p2) + '\n' + x3 + '\t\t\t' + str(p3) + '\n' + "Total price: " + str(float(p1 + p2 + p3)))



#not pass