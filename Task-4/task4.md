#1. Problem Statement
To develop a Python program to calculate an employee's gross salary using basic pay, allowances, overtime, and incentives. Apply progressive deductions and display the final net salary in a formatted salary statement.

#2. Assumptions
1. Basic salary must be greater than zero.
2. Allowances, overtime, and incentives are non-negative.
3. Gross salary = Basic + Allowances + Overtime + Incentives.
4. Deduction is calculated using these slabs:
   - Up to ₹10,000 → 5%
   - ₹10,001 to ₹20,000 → 10%
   - Above ₹20,000 → 15%
5. Net salary = Gross salary − Deduction.

 #3. Algorithm
1. Start.
2. Read basic salary, allowances, overtime, and incentives.
3. Calculate gross salary.
4. Calculate deduction using progressive slabs.
5. Calculate net salary.
6. Display salary statement.
7. Stop.

 ```mermaid

flowchart TD
    A([Start]) --> B[/Read Basic, Allowances, Overtime, Incentives/]
    B --> C[Calculate Gross Salary]
    C --> D{Gross <= 10000?}
    D -- Yes --> E[Deduction = Gross * 5%]
    D -- No --> F{Gross <= 20000?}
    F -- Yes --> G[Deduction = 500 + (Gross-10000)*10%]
    F -- No --> H[Deduction = 1500 + (Gross-20000)*15%]
    E --> I[Net = Gross - Deduction]
    G --> I
    H --> I
    I --> J[/Display Salary Statement/]
    J --> K([Stop])
```

#5.pseudo code
START
INPUT basic, allowances, overtime, incentives

gross = basic + allowances + overtime + incentives

IF gross <= 10000
    deduction = gross * 0.05
ELSE IF gross <= 20000
    deduction = 500 + (gross-10000) * 0.10
ELSE
    deduction = 1500 + (gross-20000) * 0.15
END IF

net = gross - deduction

PRINT gross, deduction, net

#6.python source code


basic = float(input("Enter basic salary: "))
allow = float(input("Enter allowances: "))
overtime = float(input("Enter overtime: "))
incentive = float(input("Enter incentives: "))

if basic <= 0 or allow < 0 or overtime < 0 or incentive < 0:
    print("Invalid salary details")
else:
    gross = basic + allow + overtime + incentive

    if gross <= 10000:
        deduction = gross * 0.05
    elif gross <= 20000:
        deduction = 500 + (gross - 10000) * 0.10
    else:
        deduction = 1500 + (gross - 20000) * 0.15

    net = gross - deduction

    print("\n--- SALARY STATEMENT ---")
    print("Gross Salary:", gross)
    print("Deduction:", deduction)
    print("Net Salary:", net)

#7.sample output

Enter basic salary: 15000
Enter allowances: 3000
Enter overtime: 1000
Enter incentives: 1000

--- SALARY STATEMENT ---
Gross Salary: 20000.0
Deduction: 1500.0
Net Salary: 18500.0

#8.conclusion

Thus, the Python program successfully calculates gross salary, applies progressive deductions, and displays the employee's final net salary


    


   
