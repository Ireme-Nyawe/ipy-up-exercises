# follows lambda arguments: expression
add = lambda a, b: a + b

print(add(5, 3))

# Create a lambda function to calculate the square of a number
square = lambda x: x * x

# Call the function
print(square(5))
print(square(10))
print(square(7))



# Create a lambda function to check if a number is even or odd
check_number = lambda x: "Even" if x % 2 == 0 else "Odd"

# Test the function
print(check_number(10))
print(check_number(7))
print(check_number(24))
print(check_number(15))