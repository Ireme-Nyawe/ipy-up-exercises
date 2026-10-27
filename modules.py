# 1. Import modules
import math
import random
import datetime

# 2. Reusing code with functions
def greet(name):
    return f"Hello, {name}!"

print("1. Code Reuse:")
print(greet("Alex"))

# 3. Mathematical calculations
print("\n2. Mathematics:")
print("Square root of 64:", math.sqrt(64))
print("Value of pi:", math.pi)

# 4. Generating random numbers
print("\n3. Random Numbers:")
print("Random number:", random.randint(1, 100))
print("Dice roll:", random.randint(1, 6))

# 5. Working with dates and time
print("\n4. Date and Time:")
today = datetime.date.today()
print("Today's date:", today)

# 6. Organizing code into functions
def calculate_area(length, width):
    return length * width

print("\n5. Organizing Code:")
print("Rectangle area:", calculate_area(5, 4))