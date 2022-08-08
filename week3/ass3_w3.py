import math

x1, y1, x2, y2 = map(float, input().split())

eu_dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
mat_dist = abs(x1 - x2) + abs(y1 - y2)
f_eu_dist = ("%.6f" % eu_dist)
f_mat_dist = ("%.6f" % mat_dist)

x = int(input("Select a option" + '\n' + "1. Euclidean distance" + '\n' + "2. Manhattan distance" + '\n' + "Your choice: "))

if x == 1:
    print("Euclidean distance: ", f_eu_dist)
elif x == 2:
    print("Manhattan distance: ", f_mat_dist)
else:
    print("Invalid input")

# PASS