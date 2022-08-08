import math
A, B, C, D = 0, 0, 0, 0

def read(A, B, C, D):
    while A <= 0:
        A = int(input("Please enter a positive integer A: "))
        if A <= 0:
            print("A must be greater than 0")
        else:
            while B <= 0:
                B = int(input("Please enter a positive integer B: "))
                if B <= 0:
                    print("B must be greater than 0")
                else:
                    while C <= 0:
                        C = int(input("Please enter a positive integer C: "))
                        if C <= 0:
                            print("C must be greater than 0")
                        else:
                            while D <= 0:
                                D = int(input("Please enter a positive integer D: "))
                                if D <= 0:
                                    print("D must be greater than 0")
                                else:
                                    return A, B, C, D
                            continue
                    continue
            continue

x = read(A, B, C, D)

def findPower(x):
    P = (x[0]**x[1]) + (x[1]**x[2]) + (x[2]**x[3])
    return P
    
P = findPower(x)

def main(P):
    z = math.sqrt(P/10.25)
    print("z = " + "%.5f" % z)

main(P)

#pass