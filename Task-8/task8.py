#python source code


material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
machine = float(input("Enter machine cost: "))

waste = float(input("Enter wastage percentage: "))
selling = float(input("Enter selling price: "))
target = float(input("Enter profit target: "))

wastage = material * waste / 100

total = material + labour + machine + wastage
profit = selling - total

print("Wastage Cost:", wastage)
print("Total Manufacturing Cost:", total)
print("Profit:", profit)

if profit >= target:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")

