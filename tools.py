# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Multiple arguments
add = lambda a, b: a + b
print(add(3, 4))  # 7

# Conditional inside a lambda
is_even = lambda n: "even" if n % 2 == 0 else "odd"
print(is_even(7))  # odd

# With sorted(): sort by the second item of each tuple
pairs = [(1, "pear"), (2, "apple"), (3, "fig")]
print(sorted(pairs, key=lambda p: p[1]))

# With map() and filter()
nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * 10, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))


nums = [1, 2, 3, 4, 5, 6]

# Basic: [expression for item in iterable]
squares = [n ** 2 for n in nums]

# With a condition (filter)
evens = [n for n in nums if n % 2 == 0]

# With if/else (transform), note the position
labels = ["even" if n % 2 == 0 else "odd" for n in nums]

# Nested loops
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]

# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [item for row in matrix for item in row]

# Transform strings
words = ["apple", "banana", "cherry"]
upper = [w.upper() for w in words]

# Dict and set comprehensions
word_lengths = {w: len(w) for w in words}
unique_lengths = {len(w) for w in words}



name = "Great"
age = 25
price = 1234.5678

# Basic
print(f"Hello, {name}!")

# Expressions inside braces
print(f"Next year you'll be {age + 1}")
print(f"Name in caps: {name.upper()}")

# Number formatting
print(f"Price: {price:.2f}")        # 1234.57
print(f"Price: {price:,.2f}")       # 1,234.57
print(f"Percent: {0.256:.1%}")      # 25.6%
print(f"Padded: {7:03d}")           # 007

# Alignment and width
print(f"|{name:<10}|")   # left
print(f"|{name:>10}|")   # right
print(f"|{name:^10}|")   # center

# Debug shortcut (prints name and value)
print(f"{age=}")         # age=25

# Dict access and multiline
user = {"name": "Great", "role": "founder"}
print(f"{user['name']} is a {user['role']}")

msg = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"Price: {price:.2f}"
)
print(msg)
