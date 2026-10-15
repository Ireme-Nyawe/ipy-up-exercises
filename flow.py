data = [0, "hello", "", None, 42, [], "py", False, 7]

clean = []
for item in data:
    if item:
        clean.append(item)

dropped = len(data) - len(clean)
print(clean)
print("Dropped:", dropped)