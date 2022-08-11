print("-------- Input Process --------")
to_do = { }

while True:
    td = input("To do: ")
    if td == "":
        break
    details = input("* Details: ")
    to_do[td] = details

print("-------- Actual Output --------")
sortednames=sorted(to_do.keys(), key=lambda x:x.lower())
count = len(to_do)
print("You have {} thing(s) to do:\n".format(count))

for i in range(count):
    print(sortednames[i])
    print("* {}\n".format(to_do[sortednames[i]]))

#pass