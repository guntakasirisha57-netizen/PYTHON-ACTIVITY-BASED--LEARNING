#python source code


n = int(input("Enter number of passengers: "))

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter distance: "))

    print("1. General  2. Sleeper  3. AC")
    choice = int(input("Select class: "))

    if choice == 1:
        rate = 1
    elif choice == 2:
        rate = 2
    elif choice == 3:
        rate = 4
    else:
        print("Invalid class")
        continue

    fare = distance * rate

    if age < 5:
        fare = 0
    elif age >= 60:
        fare = fare * 0.80

    total = fare + 50

    cancel = input("Cancel ticket? (yes/no): ")

    if cancel.lower() == "yes":
        total = max(0, total - 100)

    print("\n--- Railway Bill ---")
    print("Name:", name)
    print("Final Fare: Rs.", total)

print("\nCalculation Completed")

