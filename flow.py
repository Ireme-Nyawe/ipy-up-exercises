data = [0, "hello", "", None, 42, [], "py", False, 7]

clean = []
for item in data:
    if item:
        clean.append(item)

dropped = len(data) - len(clean)
print(clean)
print("Dropped:", dropped)


# Gues the number game
secret = 6
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess == secret:
        print(f"Correct! You got it in {attempts} attempts.")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")

#Safe default
data = [0, "", None, 5, "Great"]

for item in data:
    if item or item == 0:
        print(item)
    else:
        print("default")
#First prime in a range
data = [8, 9, 10, 11, 12]

for n in data:
    if n < 2:
        continue
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, "is the first prime")
        break
else:
    print("no prime found")