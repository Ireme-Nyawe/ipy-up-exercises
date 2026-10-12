print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)


x = 10
y = 3
x=x + y
x=+3
print(bool("false"))

age = 24
if 18<=age<65:
    print("Eligible")
successful = False
for number in range(3):
    print("Attempt", number+1)
    if(successful):
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
    count = 0
for number in range(2,10,2):
    print(number)
    count += 1
else:
    print(f"we have {count} even numbers")

def greet_user(first_name, last_name):
    return f"Hi {first_name} {last_name}!"


greeting= greet_user("John", "Doe")
print(greeting)
file=open("text.txt", "w")
file.write(greeting)
file.close()    
