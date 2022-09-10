v1, v2, v3 = map(float, input("Enter values of the vector: ").split())
w1, w2, w3 = map(float, input("Enter values of the vector: ").split())

V = [v1, v2, v3]
W = [w1, w2, w3]

U = [V[i] + W[i] for i in range(3)]

print(f'v1: {V}\nv2: {W}')
print("v1 + v2: ", U)