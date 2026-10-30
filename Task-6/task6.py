#python source code

n = int(input("Enter number of passengers: "))
distance = float(input("Enter distance in km: "))

if n <= 0 or distance <= 0:
    print("Invalid Input")

else:
    travel_class = input("Enter class (Sleeper/AC): ").lower()

    if travel_class == "sleeper":
        rate = 2
    elif travel_class == "ac":
        rate = 4
    else:
        rate = 0

    if rate == 0:
        print("Invalid travel class")

    else:
        total = 0

        for i in range(n):
            age = int(input("Enter passenger age: "))

            if age < 0:
                print("Invalid age")
                break

            if age < 5:
                fare = 0
            else:
                fare = distance * rate

                if distance < 100:
                    fare = max(fare, 100)

                if age >= 60:
                    fare = fare * 0.80

                fare += 30

            print("Passenger", i + 1, "Fare:", fare)
            total += fare

        else:
            print("Total Fare:", total)

            cancel = input("Cancel ticket? (yes/no): ").lower()

            if cancel == "yes":
                total = max(0, total - (50 * n))

            print("Final Amount:", total)

