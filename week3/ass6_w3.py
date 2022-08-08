x, y = input("Enter products code and price like this (code, price): ").split()

if "t" in x.lower():
    t_p = float(float(int(y)*7)/107)
    p = float(y) - t_p
    print("price without Tax: ", float(p))
    print("Tax:", t_p)
else: 
    print("price without Tax: ", float(y))
    print("7% Tax:", 0)

# PASS