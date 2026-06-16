# 1. Get Inputs
item_name = input("Enter item name: ")
price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))

# 2. Calculations
subtotal = price * qty
tax = subtotal * 0.05
total = subtotal + tax

# 3. Print Output
print("-" * 20)
print(f"Item: {item_name}")
print(f"Subtotal: ${subtotal}")
print(f"Tax (5%): ${tax}")
print("-" * 20)
print(f"TOTAL: ${total}")