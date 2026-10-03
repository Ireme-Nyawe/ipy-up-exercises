
# 1. Variables
product_name = "Laptop"
price = 500000
quantity = 3

# 2. Arithmetic expressions
subtotal = price * quantity
tax = subtotal * 0.18
total = subtotal + tax

print("Product:", product_name)
print("Price:", price)
print("Quantity:", quantity)
print("Subtotal:", subtotal)
print("Tax:", tax)
print("Total:", total)


# 3. User input

customer = input("Enter customer name: ")
discount = float(input("Enter discount percentage: "))

discount_amount = total * (discount / 100)
final_price = total - discount_amount

print("\nCustomer:", customer)
print("Discount:", discount_amount)
print("Final price:", final_price)


# 4. IF / ELSE

if final_price >= 1000000:
    print("Large purchase")
elif final_price >= 500000:
    print("Medium purchase")
else:
    print("Small purchase")

# 5. Comparison operators


if quantity > 0:
    print("Product is available")

if quantity == 3:
    print("Customer bought exactly 3 items")

if price != 0:
    print("Price exists")

# 6. Logical operators

if quantity > 0 and price > 0:
    print("Valid sale")

if quantity > 10 or total > 5000000:
    print("High-volume or high-value sale")


# 7. LIST

sales = [500000, 300000, 700000, 200000, 900000]

print("\nSales:", sales)
print("First sale:", sales[0])
print("Last sale:", sales[-1])

# Add a sale
sales.append(600000)

# Remove a sale
sales.remove(200000)

print("Updated sales:", sales)


# 8. FOR LOOP

print("\nAll sales:")

for sale in sales:
    print(sale)


# 9. Calculate total sales

total_sales = 0

for sale in sales:
    total_sales = total_sales + sale

print("Total sales:", total_sales)


# 10. Find sales above 500,000

print("\nSales above 500,000:")

for sale in sales:
    if sale > 500000:
        print(sale)

# 11. DICTIONARY

product = {
    "name": "Laptop",
    "price": 500000,
    "quantity": 3,
    "category": "Electronics"
}

print("\nProduct information:")
print(product["name"])
print(product["price"])
print(product["quantity"])
print(product["category"])


# Add new information
product["supplier"] = "ABC Company"

print(product)


# 12. FUNCTION

def calculate_total(price, quantity):
    return price * quantity


result = calculate_total(100000, 5)

print("\nFunction result:", result)


# Another function
def calculate_profit(revenue, cost):
    return revenue - cost


profit = calculate_profit(1000000, 700000)

print("Profit:", profit)

# 13. WHILE LOOP

counter = 1

print("\nCounting:")

while counter <= 5:
    print(counter)
    counter += 1


# 14. Final calculation

revenue = 5000000
cost = 3500000

profit = revenue - cost
profit_margin = (profit / revenue) * 100

print("\n===== BUSINESS SUMMARY =====")
print("Revenue:", revenue)
print("Cost:", cost)
print("Profit:", profit)
print("Profit margin:", profit_margin, "%")