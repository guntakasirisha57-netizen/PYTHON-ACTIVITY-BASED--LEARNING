#1.Problem Statement:

Develop a Python program to calculate the total campus event expenses, including venue, equipment, catering, transport, and certificates. Calculate participant contributions, sponsorship amount, sponsorship shortfall, and minimum registrations required to break even.

#2.Assumptions
1. Venue cost is fixed.
2. Equipment cost is fixed.
3. Catering cost depends on the number of participants.
4. Transport and certificate costs are calculated per participant.
5. Sponsorship amount is fixed.
6. Each participant pays a fixed registration fee

#3.Algorithm
1. Start.
2. Read the number of participants.
3. Read venue, equipment, catering, transport, and certificate costs.
4. Calculate total event expenses.
5. Calculate participant registration income.
6. Add sponsorship amount.
7. Calculate total income and sponsorship shortfall.
8. Calculate minimum registrations required to break even.
9. Display all results.
10. Stop.

 ```mermaid

flowchart TD
    A([Start]) --> B[/Enter participants and costs/]
    B --> C[Calculate total expenses]
    C --> D[Calculate registration income]
    D --> E[Add sponsorship]
    E --> F[Calculate shortfall]
    F --> G[Calculate break-even registrations]
    G --> H[/Display results/]
    H --> I([Stop])
```
#5.pseudo code

START
INPUT participants
INPUT venue, equipment
INPUT catering, transport, certificate
INPUT registration_fee, sponsorship

fixed_cost = venue + equipment

variable_cost = catering + transport + certificate

total_cost = fixed_cost + (variable_cost * participants)

registration_income = participants * registration_fee

total_income = registration_income + sponsorship

shortfall = MAX(0, total_cost - total_income)

break_even = CEILING(
 fixed_cost / (registration_fee - variable_cost)
)

DISPLAY total_cost
DISPLAY registration_income
DISPLAY total_income
DISPLAY shortfall
DISPLAY break_even

#6.python source code


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

#7.sample output

Enter participants: 100
Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost per person: 100
Enter transport cost per person: 50
Enter certificate cost per person: 20
Enter registration fee: 300
Enter sponsorship amount: 10000

--- CAMPUS EVENT REPORT ---
Total Expenses: 32000.0
Registration Income: 30000.0
Sponsorship: 10000.0
Total Income: 40000.0
Sponsorship Shortfall: 0
Break-even Participants: 0

#8.conclusion
The program calculates total campus event expenses, registration income, sponsorship, and break-even participants. It helps organizers plan the event budget and manage expenses efficiently.






    

   


