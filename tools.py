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