inventory = [
    ["Strawberry", "Fruit", 3.50, 40, 10],
    ["Broccoli", "Vegetable", 2.20, 25, 8],
    ["Cheddar", "Dairy", 5.00, 18, 4],
    ["Baguette", "Bakery", 2.80, 35, 2],
    ["Blueberry", "Fruit", 4.00, 22, 6],
    ["Spinach", "Vegetable", 1.80, 30, 12],
    ["Yogurt", "Dairy", 1.20, 50, 15],
    ["Croissant", "Bakery", 3.00, 28, 3]
]

total_revenue = sum(item[2] * item[3] for item in inventory)
print(total_revenue)

low_stock = [item[0] for item in inventory if item[4] < 5]
print(low_stock)


fruit = 0
vegetable = 0
dairy = 0
bakery = 0

for item in inventory:
    if item[1] == "Fruit":
        fruit = fruit + (item[2] * item[3])
    elif item[1] == "Vegetable":
        vegetable = vegetable + (item[2] * item[3])
    elif item[1] == "Dairy":
        dairy = dairy + (item[2] * item[3])
    elif item[1] == "Bakery":
        bakery = bakery + (item[2] * item[3])

print("Category-wise Revenue:")
print("Fruit:", fruit)
print("Vegetable:", vegetable)
print("Dairy:", dairy)
print("Bakery:", bakery)