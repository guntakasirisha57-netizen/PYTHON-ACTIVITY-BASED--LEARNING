#1. Problem Statement
Develop a Python program to calculate hospital bills using consultation, diagnostic, and treatment charges. Apply discounts based on patient conditions, validate billing details, and classify patients according to the payment policy.

#2. Assumptions
1. Consultation fee = ₹500.
2. Diagnostic charges = ₹1,000.
3. Treatment charges = ₹2,000.
4. Senior citizens get a 10% discount.
5. Total bill must be greater than zero.
6. Payment classification:
   - Below ₹1,000 – Low
   - ₹1,000 to ₹3,000 – Medium
   - Above ₹3,000 – High

#3. Algorithm
1. Start.
2. Input patient name and age.
3. Input consultation, diagnostic, and treatment charges.
4. Calculate total bill.
5. Check patient age.
6. Apply discount if age is 60 or above.
7. Calculate final bill.
8. Classify patient payment.
9. Display the bill details.
10. Stop.

 ```mermaid

flowchart TD
    A([Start]) --> B[/Enter patient details/]
    B --> C[/Enter hospital charges/]
    C --> D[Calculate total bill]
    D --> E{Age >= 60?}
    E -->|Yes| F[Apply 10% discount]
    E -->|No| G[No discount]
    F --> H[Calculate final bill]
    G --> H
    H --> I{Classify payment}
    I --> J[/Display bill and category/]
    J --> K([Stop])
```
 #5.pseudo code

 START

INPUT name, age
INPUT consultation, diagnostic, treatment

total = consultation + diagnostic + treatment

IF total <= 0 OR age < 0
    PRINT "Invalid Details"

ELSE
    IF age >= 60
        discount = total * 10 / 100
    ELSE
        discount = 0

    final_bill = total - discount

    IF final_bill < 1000
        category = "Low"
    ELSE IF final_bill <= 3000
        category = "Medium"
    ELSE
        category = "High"

    DISPLAY total
    DISPLAY discount
    DISPLAY final_bill
    DISPLAY category

#6.python source code


# Hospital Billing System

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validation
if age < 0 or min(consultation, diagnostic, treatment) < 0:
    print("Invalid Details")

else:
    # Calculate total
    total = consultation + diagnostic + treatment

    # Apply discount
    if age >= 60:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    # Patient classification
    if final_bill < 1000:
        category = "Low"
    elif final_bill <= 3000:
        category = "Medium"
    else:
        category = "High"

    # Display bill
    print("\n--- HOSPITAL BILL ---")
    print("Patient Name:", name)
    print("Total Charges:", total)
    print("Discount:", discount)
    print("Final Bill:", final_bill)
    print("Payment Category:", category)

#7.sample output

Enter patient name: Siri
Enter patient age: 65
Enter consultation charges: 500
Enter diagnostic charges: 1000
Enter treatment charges: 2000

--- HOSPITAL BILL ---
Patient Name: Siri
Total Charges: 3500.0
Discount: 350.0
Final Bill: 3150.0
Payment Category: High

#8.conclusion

The program calculates hospital charges, applies senior citizen discounts, validates billing details, and classifies patients based on their final bill amount.







  
   


