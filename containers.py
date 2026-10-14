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




# ============================================================
# 3. SET
# ============================================================

# 3.1 Create a set
numbers = {10, 20, 30, 20}

print(numbers)            # Contains 10, 20, 30; duplicate 20 removed

empty_set = set()
print(empty_set)

# Create a set from a list
from_list = set([1, 2, 2, 3, 3, 4])
print(from_list)          # Unique values only

# 3.2 Add items
numbers.add(40)           # Add one item
numbers.update([50, 60])  # Add multiple items
print(numbers)

# 3.3 Remove items
numbers.remove(20)        # Error if 20 is absent
numbers.discard(999)      # No error if 999 is absent

# pop() removes an arbitrary item
removed_item = numbers.pop()
print("Removed:", removed_item)
print(numbers)

# 3.4 Check membership and length
print(30 in numbers)
print(999 not in numbers)
print(len(numbers))

# 3.5 Set union: combine unique items
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a | b)              # Same operation

# 3.6 Intersection: items found in both sets
print(a.intersection(b))
print(a & b)              # Same operation

# 3.7 Difference: items in A but not in B
print(a.difference(b))
print(a - b)

# Items in B but not in A
print(b - a)

# 3.8 Symmetric difference: items in either set, but not both
print(a.symmetric_difference(b))
print(a ^ b)

# 3.9 Compare sets
print({1, 2}.issubset(a))       # True
print(a.issuperset({1, 2}))     # True
print(a.isdisjoint({7, 8}))     # True: no shared items

print({1, 2} <= a)              # Subset
print(a >= {1, 2})              # Superset

# 3.10 Update a set using operations
x = {1, 2, 3}
x.update({3, 4})                # Add values
print(x)                        # {1, 2, 3, 4}

x.intersection_update({2, 3, 4})
print(x)                        # {2, 3, 4}

x.difference_update({4})
print(x)                        # {2, 3}

x.symmetric_difference_update({3, 5})
print(x)                        # {2, 5}

# 3.11 Copy and clear
copied = a.copy()
print(copied)

copied.clear()
print(copied)                   # set()

# 3.12 Loop through a set
for item in a:
    print(item)

# Do not rely on a particular iteration order.

# 3.13 Set comprehension
squares = {n ** 2 for n in range(6)}
print(squares)

evens = {n for n in range(10) if n % 2 == 0}
print(evens)

# 3.14 Remove duplicates from a list
names = ["Aline", "Eric", "Aline", "Diane"]
unique_names = set(names)

print(unique_names)

# Convert back to a list if needed
unique_names_list = list(unique_names)
print(unique_names_list)



# ============================================================
# 4. DICTIONARY
# ============================================================

# 4.1 Create a dictionary
student = {
    "name": "Aline",
    "age": 21,
    "course": "Python"
}

empty_dict = {}

print(student)
print(empty_dict)

# Create a dictionary from pairs
from_pairs = dict([("a", 1), ("b", 2)])
print(from_pairs)

# 4.2 Access values using keys
print(student["name"])        # Aline
print(student["age"])         # 21

# get() avoids KeyError for a missing key
print(student.get("name"))
print(student.get("phone"))             # None
print(student.get("phone", "Unknown"))  # Default value

# 4.3 Add a new key-value pair
student["city"] = "Kigali"
student["phone"] = "0780000000"

print(student)

# 4.4 Update an existing value
student["age"] = 22

# Update one or more key-value pairs
student.update({
    "course": "Data Analytics",
    "country": "Rwanda"
})

print(student)

# 4.5 Remove items
phone = student.pop("phone")
print("Removed phone:", phone)

last_pair = student.popitem()
print("Removed last inserted pair:", last_pair)

print(student)

# Delete a particular key
del student["city"]
print(student)

# 4.6 Check whether keys exist
print("name" in student)          # True
print("phone" in student)         # False
print("phone" not in student)     # True

# Important: 'in' checks keys, not values.
print("Aline" in student)         # False

# 4.7 Get the dictionary's length
print(len(student))

# 4.8 Get keys, values, and key-value pairs
print(student.keys())
print(student.values())
print(student.items())

# Convert dictionary views to lists
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

# 4.9 Loop through keys
for key in student:
    print(key)

# 4.10 Loop through values
for value in student.values():
    print(value)

# 4.11 Loop through keys and values
for key, value in student.items():
    print(key, ":", value)

# 4.12 Copy a dictionary
copied = student.copy()
print(copied)

# 4.13 Merge dictionaries
a = {"name": "Aline", "age": 21}
b = {"city": "Kigali", "age": 22}

# update() modifies the first dictionary
a.update(b)
print(a)                  # age becomes 22

# | creates a new merged dictionary (Python 3.9+)
x = {"a": 1, "b": 2}
y = {"b": 99, "c": 3}

merged = x | y
print(merged)             # {'a': 1, 'b': 99, 'c': 3}
print(x)                  # Original x is unchanged

# 4.14 setdefault()
data = {"name": "Aline"}

data.setdefault("status", "active")
print(data)               # Adds status

data.setdefault("name", "Eric")
print(data)               # Existing name remains Aline

# 4.15 Create a dictionary from keys
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, None)

print(new_dict)

# 4.16 Dictionary comprehension
squares = {n: n ** 2 for n in range(5)}
print(squares)

# Filter a dictionary using comprehension
scores = {"Aline": 85, "Eric": 45, "Diane": 92}

passed = {
    name: score
    for name, score in scores.items()
    if score >= 50
}

print(passed)

# 4.17 Clear all items
temporary = {"a": 1, "b": 2}
temporary.clear()

print(temporary)          # {}

# 4.18 Safely check for a missing key
if "email" in student:
    print(student["email"])
else:
    print("Email not found")