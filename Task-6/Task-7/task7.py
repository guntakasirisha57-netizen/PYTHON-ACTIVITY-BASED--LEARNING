#python source code


n = int(input("Enter number of products: "))

subtotal = 0
tax_total = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    category = input("Enter category (food/electronics/other): ").lower()

    amount = price * qty
    subtotal += amount

    if category == "food":
        tax = 5
    elif category == "electronics":
        tax = 18
    else:
        tax = 12

    tax_amount = amount * tax / 100
    tax_total += tax_amount

    print(name, "Amount:", amount)

if subtotal > 5000:
    discount = min(subtotal * 0.10, 1000)
else:
    discount = 0

total = subtotal + tax_total - discount

print("\n--- RETAIL INVOICE ---")
print("Subtotal: Rs.", subtotal)
print("Tax: Rs.", tax_total)
print("Discount: Rs.", discount)
print("Final Bill: Rs.", total)

