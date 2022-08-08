x, op, y = input("Enter x operation with y(+ - * / ^): ").split()

if op == "+":
    print(("%.2f" % float(x) + float(y)))
elif op == "-":
    print(("%.2f" % float(x) - float(y)))
elif op == "*":
    print(("%.2f" % float(x) * float(y)))
elif op == "/":
    print(("%.2f" % float(x) / float(y)))
elif op == "^":
    print(("%.2f" % float(x) ** float(y)))
else:
    print("Invalid operator")
    
# ass11_w3