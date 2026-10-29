#source code
if age < 5:
    discount = total * 0.20
elif age >= 60:
    discount = total * 0.10
else:
    discount = 0

final = total - discount

if final <= 1000:
    category = "Low Payment"
elif final <= 5000:
    category = "Medium Payment"
else:
    category = "High Payment"

print("\n--- Hospital Bill ---")
print("Patient Name:", name)
print("Total Charges:", total)
print("Concession:", discount)
print("Final Bill:", final)
print("Patient Category:", category)
