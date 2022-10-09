import math

x1, y1, x2, y2 = map(int, input("Enter position[x1, y1, x2, y2]: ").split())

eu_dist = float(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
mat_dist = float(abs(x1 - x2) + abs(y1 - y2))
f_eu_dist = ("%.6f" % eu_dist)
f_mat_dist = ("%.6f" % mat_dist)

print("Euclidean_distance", f_eu_dist)
print("Manhattan distance:", f_mat_dist)

