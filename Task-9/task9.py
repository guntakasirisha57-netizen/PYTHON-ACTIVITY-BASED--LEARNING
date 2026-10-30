#python source code


food = float(input("Enter food expense: "))
travel = float(input("Enter travel expense: "))
shopping = float(input("Enter shopping expense: "))

rate = float(input("Enter exchange rate: "))
fee = float(input("Enter conversion fee percentage: "))
budget = float(input("Enter budget in INR: "))

f = food * rate
t = travel * rate
s = shopping * rate

subtotal = f + t + s
charges = subtotal * fee / 100
total = subtotal + charges

print("Food Cost:", f)
print("Travel Cost:", t)
print("Shopping Cost:", s)
print("Conversion Fee:", charges)
print("Total Expense:", total)

if total <= budget:
    print("Within Budget")
else:
    print("Over Budget")

if f >= t and f >= s:
    print("Largest Expense: Food")
elif t >= f and t >= s:
    print("Largest Expense: Travel")
else:
    print("Largest Expense: Shopping")

