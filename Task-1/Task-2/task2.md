#1.Problem Statement
To develop a Python program to calculate household electricity bills using different consumption slabs, fixed charges, surcharges, and rebates. The program also compares electricity bills for several months and identifies unusual increases in the bill amount.

#2. Assumptions
1. The user enters electricity units consumed for three months.
2. First 100 units cost ₹2 per unit.
3. Next 100 units cost ₹3 per unit.
4. Units above 200 cost ₹5 per unit.
5. Fixed charge is ₹50 per month.
6. Surcharge is 5% of the energy charge.
7. Rebate is ₹20 per month.
8. If the bill increases by more than 20% compared with the previous month, it is considered an unusual increase.
9. All units consumed must be non-negative.
These are sample rates for the assignment, not official electricity tariffs.

. Algorithm
1. Start.
2. Input electricity units for three months.
3. Check whether the units are valid.
4. Calculate energy charges using the consumption slabs.
5. Add the fixed charge and surcharge.
6. Subtract the rebate to get the final bill.
7. Compare each month's bill with the previous month's bill.
8. If the bill increases by more than 20%, display an unusual increase message.
9. Display the monthly bills.
10. Stop.
 ```mermaid   
4. Flowchart
flowchart td


    A([Start]) --> B[/Enter units for 3 months/]
    B --> C{Units valid?}
    C -- No --> D[/Print Invalid Input/]
    D --> J([Stop])
    C -- Yes --> E[Calculate slab charges]
    E --> F[Add fixed charge and surcharge]
    F --> G[Subtract rebate]
    G --> H[Display monthly bills]
    H --> I[Compare consecutive bills]
    I --> K{Increase above 20%?}
    K -- Yes --> L[/Print Unusual Increase/]
    K -- No --> M[/Print Normal Increase/]
    L --> N([Stop])
    M --> N
    ```
  #5. pseudocode
  
INPUT units for 3 months

IF any units < 0
    PRINT "Invalid Input"
ELSE
    FOR each month
        IF units <= 100
            energy = units * 2
        ELSE IF units <= 200
            energy = 200 + (units - 100) * 3
        ELSE
            energy = 500 + (units - 200) * 5
        END IF

        surcharge = energy * 0.05
        bill = energy + 50 + surcharge - 20
        STORE bill
    END FOR

    DISPLAY all bills

    FOR each month after the first
        increase = (current bill - previous bill)
                   / previous bill * 100

        IF increase > 20
            PRINT "Unusual Increase"
        ELSE
            PRINT "Normal Increase"
        END IF
    END FOR
END IF

STOP
#6.python source code

units = []
bills = []

for i in range(3):
    u = int(input("Enter units for month: "))
    units.append(u)

if any(u < 0 for u in units):
    print("Invalid units")
else:
    for u in units:
        if u <= 100:
            energy = u * 2
        elif u <= 200:
            energy = 200 + (u - 100) * 3
        else:
            energy = 500 + (u - 200) * 5

        surcharge = energy * 0.05
        bill = energy + 50 + surcharge - 20
        bills.append(bill)

    for i in range(3):
        print("Month", i + 1, "Bill: Rs.", bills[i])

    for i in range(1, 3):
        if bills[i - 1] > 0:
            increase = ((bills[i] - bills[i - 1])
                        / bills[i - 1]) * 100

            if increase > 20:
                print("Month", i + 1, ": Unusual Increase")
            else:
                print("Month", i + 1, ": Normal Increase")

#7.sample output
Enter units for month: 80
Enter units for month: 120
Enter units for month: 250

Month 1 Bill: Rs. 198.0
Month 2 Bill: Rs. 303.0
Month 3 Bill: Rs. 817.5

Month 2 : Unusual Increase
Month 3 : Unusual Increase

#8. Conclusion
The Python program calculates electricity bills using progressive slabs, fixed charges, surcharges, and rebates. It compares bills across three months and identifies unusual increases using conditional statements and loops.
                


    

