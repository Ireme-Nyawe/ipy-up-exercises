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