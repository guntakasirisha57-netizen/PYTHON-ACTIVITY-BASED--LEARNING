#python source code

basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime: "))
incentives = float(input("Enter incentives: "))

gross = basic + allowances + overtime + incentives

if gross <= 10000:
    deduction = gross * 0.05

elif gross <= 20000:
    deduction = 500 + (gross - 10000) * 0.10

else:
    deduction = 1500 + (gross - 20000) * 0.15

net = gross - deduction

print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)
