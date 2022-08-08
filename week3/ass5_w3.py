h = int(input("How many hour you you submit late?: "))
s = float(input("What is your estimated score(s): "))

if h > 48:
    print("You aren't getting any score :(")
elif h >= 24 and h < 48:
    ac_s = s / 2
    print("Your expect score is: ", ("%.1f" % float(ac_s)))
elif h < 24 and h >= 1:
    ac_s = s - (s * 0.2)
    print("Your expect score is: ", ("%.1f" % float(ac_s)))
else:
    print("Your expect score is: ", ("%.1f" % float(s)))

#ass5_w3