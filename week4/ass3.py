while True:
    x, z, y = input("Enter X op Y (+ - * / // %): ").split()
    x = float(x)
    y = float(y)
    if x == 0 and y == 0:
        print("Bye!")
        break
    elif z == "+":
        print("{} + {} =".format(x, y), ("%.2f" % float(x + y)))
    elif z == "-":
        print("{} - {} =".format(x, y), ("%.2f" % float(x - y)))
    elif z == "*":
        print("{} * {} =".format(x, y), ("%.2f" % float(x * y)))
    elif z == "/":
        print("{} / {} =".format(x, y), ("%.2f" % float(x / y)))
    elif z == "//":
        print("{} // {} =".format(x, y), ("%.2f" % float(x // y)))
    elif z == "%":
        print("{} % {} =".format(x, y), ("%.2f" % float(x % y)))
    else:
        print("Invalid operator!")

#PASS