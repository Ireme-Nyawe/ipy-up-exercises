# ADVANCED PYTHON SALES ANALYSIS

# Sales data
sales = [
    {"product": "Laptop", "quantity": 2, "price": 500000},
    {"product": "Phone", "quantity": 5, "price": 300000},
    {"product": "Tablet", "quantity": 3, "price": 400000},
    {"product": "Monitor", "quantity": 4, "price": 250000},
    {"product": "Keyboard", "quantity": 10, "price": 50000}
]


# 1. List comprehension

revenues = [
    sale["quantity"] * sale["price"]
    for sale in sales
]

print("Revenues:", revenues)

# 2. List comprehension with condition

high_value_sales = [
    sale
    for sale in sales
    if sale["quantity"] * sale["price"] > 1000000
]

print("\nHigh-value sales:")
print(high_value_sales)


# 3. Extract product names

product_names = [
    sale["product"]
    for sale in sales
]

print("\nProducts:", product_names)


# 4. sum() with generator expression

total_revenue = sum(
    sale["quantity"] * sale["price"]
    for sale in sales
)

print("\nTotal revenue:", total_revenue)


# 5. min() and max()

highest_sale = max(
    sales,
    key=lambda sale: sale["quantity"] * sale["price"]
)

lowest_sale = min(
    sales,
    key=lambda sale: sale["quantity"] * sale["price"]
)

print("\nHighest sale:", highest_sale)
print("Lowest sale:", lowest_sale)


# 6. sorted() + lambda

sorted_sales = sorted(
    sales,
    key=lambda sale: sale["price"],
    reverse=True
)

print("\nSorted by price:")

for sale in sorted_sales:
    print(sale)


# 7. map()

prices = list(
    map(
        lambda sale: sale["price"],
        sales
    )
)

print("\nPrices:", prices)


# 8. filter()

large_sales = list(
    filter(
        lambda sale: sale["quantity"] >= 5,
        sales
    )
)

print("\nSales with quantity >= 5:")
print(large_sales)


# 9. Dictionary comprehension

revenue_by_product = {
    sale["product"]: sale["quantity"] * sale["price"]
    for sale in sales
}

print("\nRevenue by product:")
print(revenue_by_product)


# 10. Conditional expression

statuses = [
    "High" if sale["quantity"] * sale["price"] >= 1000000
    else "Normal"
    for sale in sales
]

print("\nSale statuses:")
print(statuses)


# 11. Function with comprehension

def calculate_revenues(sales):
    return [
        sale["quantity"] * sale["price"]
        for sale in sales
    ]


revenues = calculate_revenues(sales)

print("\nFunction result:")
print(revenues)


# ==========================================
# 12. Function returning multiple values
# ==========================================

def sales_summary(sales):

    revenues = [
        sale["quantity"] * sale["price"]
        for sale in sales
    ]

    total = sum(revenues)
    highest = max(revenues)
    lowest = min(revenues)
    average = total / len(revenues)

    return total, highest, lowest, average


total, highest, lowest, average = sales_summary(sales)

print("\n===== SALES SUMMARY =====")
print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)

# 13. *args

def calculate_total(*numbers):
    return sum(numbers)


result = calculate_total(
    100000,
    200000,
    300000,
    400000
)

print("\nTotal using *args:", result)

# 14. **kwargs

def show_customer(**customer):

    for key, value in customer.items():
        print(key, ":", value)


print("\nCustomer information:")

show_customer(
    name="John",
    age=25,
    city="Kigali",
    country="Rwanda"
)