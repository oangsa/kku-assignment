#input
d = int(input("Enter a day: "))

#processing
month = d / 30
day = d - (int(month) * 30)

#output
print("input:", d)
print("month(s):", int(month))
print("day(s):", day)

