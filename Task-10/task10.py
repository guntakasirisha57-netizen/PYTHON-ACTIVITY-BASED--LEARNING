#python source code


import math

# Input
n = int(input("Enter participants: "))

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per person: "))
transport = float(input("Enter transport cost per person: "))
certificate = float(input("Enter certificate cost per person: "))

fee = float(input("Enter registration fee per person: "))
sponsor = float(input("Enter sponsorship amount: "))

# Calculations
fixed = venue + equipment

variable = catering + transport + certificate

total_cost = fixed + variable * n

registration = n * fee

income = registration + sponsor

shortfall = max(0, total_cost - income)

# Break-even calculation
if fee > variable:
    break_even = math.ceil((fixed - sponsor) / (fee - variable))
    break_even = max(0, break_even)
else:
    break_even = "Not possible"

# Output
print("\n--- CAMPUS EVENT REPORT ---")
print("Total Expenses:", total_cost)
print("Registration Income:", registration)
print("Sponsorship:", sponsor)
print("Total Income:", income)
print("Sponsorship Shortfall:", shortfall)
print("Break-even Participants:", break_even)

