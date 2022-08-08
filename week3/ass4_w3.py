r = input("Is it rainning?: ").lower()
h = int(input("Humidity: "))
ws = float(input("Wind speed: "))

if r == "yes":
    print("We will NOT play tennis.")
elif r == "no" and h >= 65 or ws >= 5:
    print("We will NOT play tennis.")
else:
    print("We will play tennis.")

# PASS