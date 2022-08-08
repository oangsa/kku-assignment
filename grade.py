"""
This is a comment LMFAO
"""

s1 = int(input("Enter 1st subject score: "))
s2 = int(input("Enter 2nd subject score: "))
s3 = int(input("Enter 3rd subject score: "))
s4 = int(input("Enter 4th subject score: "))

score = int(s1 + s2 + s3 + s4)

print("Total score:", score)

if score < 0:
    print("error")

elif score >= 0 and score <= 200:
    print("F")

elif score >= 201 and score <= 400:
    print("D")

elif score >= 401 and score <= 600:
    print("C")
    
elif score >= 601 and score <= 800:
    print("B")
    
else: print("A")