import math

x1, y1, x2, y2 = map(int, input("Enter x1, y1, x2, y2: ").split())

def Eulidean(x1, x2, y1, y2):
    eu_dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print("Eulidean distances = " + "%.4f" % eu_dist)
    
def Manhattan(x1, x2, y1, y2):
    mat_dist = abs(x1 - x2) + abs(y1 - y2)
    print("Manhattan distances = " + "%.4f" % mat_dist)


Manhattan(x1, x2, y1, y2)
Eulidean(x1, x2, y1, y2)