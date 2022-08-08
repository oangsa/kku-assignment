a = float(input("Enter your height(cm): "))

if a >= 120:
    print("Yes, you are tall enough to ride")
    
else:
    print("Sorry, you are not tall enough to ride. You need " + ("%.2f" % float(120 - a)) + " cm more to ride.")