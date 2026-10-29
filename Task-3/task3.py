#python source code


name = input("Enter patient name: ")
age = int(input("Enter age: "))
c = float(input("Consultation charge: "))
d = float(input("Diagnostic charge: "))
t = float(input("Treatment charge: "))

if age < 0 or c < 0 or d < 0 or t < 0:
    print("Invalid Input")
else:
    total = c + d + t

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
    print("Patient:", name)
    print("Total Charges:", total)
    print("Concession:", discount)
    print("Final Bill:", final)
    print("Category:", category)

