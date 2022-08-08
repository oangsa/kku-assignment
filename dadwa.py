import datetime as dt

y = dt.date.today().year

first_name = input("Please provide me your first name: ")
last_name = input("Please put your last name: ")
year, month, day = input("Your birth day (year month date): ").split()
bless = input("Bless him,her: ")
 
print("Welcome", last_name + "," + " " + first_name + " " + "(" + year + " / " + month + " /",day + " , " + "age " + str(y - int(year)) + ")" + '\n' + bless)
