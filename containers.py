# ============================================================
# 1. LIST
# ============================================================

# 1.1 Create a list
numbers = [10, 20, 30, 20]
empty_list = []

print("Original:", numbers)
print("Empty list:", empty_list)

# 1.2 Access items using indexes
print(numbers[0])     # First item: 10
print(numbers[1])     # Second item: 20
print(numbers[-1])    # Last item: 20
print(numbers[-2])    # Second-last item: 30

# 1.3 Slice a list: list[start:stop]
print(numbers[1:3])   # [20, 30]
print(numbers[:2])    # [10, 20]
print(numbers[2:])    # [30, 20]
print(numbers[:])     # Copy of the full list

# 1.4 Change an item
numbers[0] = 100
print(numbers)        # [100, 20, 30, 20]

# 1.5 Add items
numbers.append(40)           # Add one item at the end
numbers.extend([50, 60])     # Add several items
numbers.insert(1, 15)        # Insert 15 at index 1

print(numbers)

# 1.6 Remove items
numbers.remove(20)     # Remove the first matching 20
last_item = numbers.pop()  # Remove and return last item
item = numbers.pop(0)     # Remove and return item at index 0

print(numbers)
print("Last removed:", last_item)
print("Index 0 removed:", item)

# 1.7 Delete by index or slice
del numbers[0]        # Delete first item
del numbers[0:2]      # Delete items in indexes 0 and 1
print(numbers)

# 1.8 Search and count
numbers = [10, 20, 30, 20]

print(20 in numbers)        # True
print(99 not in numbers)    # True
print(numbers.index(20))    # 1: first matching index
print(numbers.count(20))    # 2: occurrences of 20

# 1.9 Sort and reverse
numbers.sort()              # Ascending order
print(numbers)

numbers.sort(reverse=True)  # Descending order
print(numbers)

numbers.reverse()           # Reverse current order
print(numbers)

# Create a sorted copy without changing the original
original = [30, 10, 20]
sorted_copy = sorted(original)

print(original)             # [30, 10, 20]
print(sorted_copy)          # [10, 20, 30]

# 1.10 Copy and combine
a = [1, 2, 3]
b = a.copy()
combined = a + [4, 5]
repeated = [1, 2] * 3

print(b)                    # [1, 2, 3]
print(combined)             # [1, 2, 3, 4, 5]
print(repeated)             # [1, 2, 1, 2, 1, 2]

# 1.11 Useful built-in functions
numbers = [10, 20, 30]

print(len(numbers))         # Number of items: 3
print(min(numbers))         # Smallest: 10
print(max(numbers))         # Largest: 30
print(sum(numbers))         # Total: 60
print(any(numbers))         # True if any item is truthy
print(all(numbers))         # True if all items are truthy

# 1.12 Loop through a list
for number in numbers:
    print(number)

# Get both index and value
for index, value in enumerate(numbers):
    print(index, value)

# 1.13 List comprehension
squares = [n ** 2 for n in range(5)]
print(squares)              # [0, 1, 4, 9, 16]

evens = [n for n in range(10) if n % 2 == 0]
print(evens)                # [0, 2, 4, 6, 8]

# 1.14 Clear all items
numbers.clear()
print(numbers)              # []

# 1.15 Check whether a list is empty
if not numbers:
    print("The list is empty")



# ============================================================
# 2. TUPLE
# ============================================================

# 2.1 Create a tuple
numbers = (10, 20, 30, 20)
empty_tuple = ()
single_item = (5,)       # Comma is required for one item

print(numbers)
print(empty_tuple)
print(single_item)

# You can also create a tuple without parentheses
coordinates = 10, 20
print(coordinates)

# 2.2 Convert another iterable into a tuple
from_list = tuple([1, 2, 3])
from_range = tuple(range(5))

print(from_list)
print(from_range)

# 2.3 Access items
print(numbers[0])        # 10
print(numbers[-1])       # 20

# 2.4 Slice a tuple
print(numbers[1:3])      # (20, 30)
print(numbers[:2])       # (10, 20)
print(numbers[2:])       # (30, 20)

# 2.5 Search and count
print(20 in numbers)          # True
print(99 not in numbers)      # True
print(numbers.index(20))      # 1
print(numbers.count(20))      # 2

# 2.6 Combine and repeat
a = (1, 2)
b = (3, 4)

print(a + b)             # (1, 2, 3, 4)
print(a * 3)              # (1, 2, 1, 2, 1, 2)

# 2.7 Useful built-in functions
print(len(numbers))      # 4
print(min(numbers))      # 10
print(max(numbers))      # 30
print(sum(numbers))      # 80

# 2.8 Loop through a tuple
for item in numbers:
    print(item)

# 2.9 Tuple unpacking
student = ("Aline", 21, "Python")

name, age, course = student

print(name)
print(age)
print(course)

# Extended unpacking
first, *middle, last = (10, 20, 30, 40, 50)

print(first)             # 10
print(middle)            # [20, 30, 40]
print(last)              # 50

# 2.10 Change a tuple indirectly
original = (10, 20, 30)

temporary_list = list(original)
temporary_list[0] = 100
temporary_list.append(40)

updated_tuple = tuple(temporary_list)
print(updated_tuple)     # (100, 20, 30, 40)

# 2.11 Tuple comprehension clarification
# Parentheses around a comprehension create a generator,
# not a tuple.
generator = (n ** 2 for n in range(5))
squares = tuple(generator)

print(squares)           # (0, 1, 4, 9, 16)