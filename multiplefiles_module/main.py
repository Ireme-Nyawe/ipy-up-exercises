from support import *
import  matplotlib.pyplot as plt
math_ops = MathOperations()
result = math_ops.multiply(5, 3)
print("Multiplication Result:", result)

division_result = math_ops.divide(10, 2)
print("Division Result:", division_result)

sum_result = add_numbers(5, 3)
print("Addition Result:", sum_result)

x=[x for x in range(1,11)]
y=[x**2 for x in range(1,11)]

plt.plot(x,y)
plt.title("Square Numbers")
plt.xlabel("Number")
plt.ylabel("Square of Number")
plt.show()