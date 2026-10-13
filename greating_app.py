#first_name = input("Enter Your First Name:")
#last_name = input("Enter Your Last Name:")
#print(f"Hello {first_name} {last_name}, Have a nice day ahead!")

#Python program to demonstrate the use of input() function
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
hypotenuse = (side1 ** 2 + side2 ** 2) ** 0.5

print(f"The hypotenuse of the right triangle is: {round(hypotenuse, 2)}")
