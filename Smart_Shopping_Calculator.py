# 1. Product Information
products = ["Laptop", "Mouse", "Keyboard", "Headphones", "USB Cable"]
prices = [55000, 500, 1500, 2500, 300]
categories = ("Electronics", "Accessories", "Accessories", "Electronics", "Accessories")

# 2. Customer Information
customer_name = "Ali Ahmed"
delivery_required = True

# 3. Shopping Calculation
subtotal = sum(prices)

# 4. Discount Conditions
if subtotal < 10000:
    discount = subtotal * 0.05
elif subtotal <= 25000:
    discount = subtotal * 0.10
else:
    discount = subtotal * 0.15

# 5. Delivery Conditions
if subtotal >= 10000:
    delivery_charges = 0
else:
    delivery_charges = 250

final_total = subtotal - discount + delivery_charges

# 6. Final Receipt
print("=" * 45)
print("        SHOPPING RECEIPT")
print("=" * 45)
print(f"Customer : {customer_name}")
print("-" * 45)

# 7. Display Results
for i in range(len(products)):
    print(f"{products[i]:<20} ({categories[i]:<12}) PKR {prices[i]:>8.2f}")

print("-" * 45)
print(f"Subtotal{' ' * 29}PKR {subtotal:>8.2f}")
print(f"Discount{' ' * 29}PKR {discount:>8.2f}")

if delivery_required:
    print(f"Delivery{' ' * 29}PKR {delivery_charges:>8.2f}")
    if delivery_charges == 0:
        print("   * Free delivery applied!")
else:
    print("Delivery : Not required (pickup)")

print("=" * 45)
print(f"FINAL TOTAL{' ' * 26}PKR {final_total:>8.2f}")
print("=" * 45)
print("      Thank you for shopping with us!")