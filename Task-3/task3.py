#python source code

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

