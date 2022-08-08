from statistics import median, mode


with open('scores.txt') as f:
    lines = f.read().splitlines()


sums = sum(map(float, lines))
items = len(lines)
av = sums / items
count = sum(map(lambda x : x>40, map(float, lines)))
print("Max score =", "%.2f" % float(max(lines)))
print("Min score =", "%.2f" % float(min(lines)))
print("Avg score =", "%.2f" % float(av))
print("Median score =", "%.2f" % float(sorted(lines)[int(items/2)]))
print("Mode score =", "%.2f" % float(mode(lines)))
print("Number of students who pass the exam =", "%.2f" % float(count))
# print("Median2: ", median(map(float, lines)))

with open('stat.txt', 'w') as f:
    f.write("Max score = " + str("%.2f" % float(max(lines))) + "\n")
    f.write("Min score = " + str("%.2f" % float(min(lines))) + "\n")
    f.write("Avg score = " + str("%.2f" % float(av)) + "\n")
    f.write("Median score = " + str("%.2f" % float(sorted(lines)[int(items/2)])) + "\n")
    f.write("Mode score = " + str("%.2f" % float(mode(lines))) + "\n")
    f.write("Number of students who pass the exam = " + str("%.2f" % float(count)) + "\n")
    
    