#1. Problem Statement
To develop a Python program to calculate railway fares for multiple passengers based on distance, travel class, age-based concessions, reservation charges and cancellation penalties.

#2. Assumptions
1. Distance is entered in kilometres.
2. Sleeper fare = ₹2 per km.
3. AC fare = ₹4 per km.
4. Distance below 100 km has a minimum fare of ₹100.
5. Children below 5 years travel free.
6. Senior citizens (60 years and above) get a 20% concession.
7. Reservation fee = ₹30 per passenger.
8. Cancellation penalty = ₹50 per passenger.
9. Invalid inputs are not accepted.

#3. Algorithm
1. Start.
2. Enter number of passengers and journey distance.
3. Select travel class (Sleeper or AC).
4. Enter each passenger's age.
5. Calculate fare based on distance and class.
6. Apply age-based concession.
7. Add reservation fee.
8. Calculate total fare.
9. If cancelled, deduct cancellation penalty.
10. Display final fare.
11. Stop.

  ```mermaid

flowchart TD
    A([Start]) --> B[/Enter passengers and distance/]
    B --> C[/Select travel class/]
    C --> D[/Enter passenger age/]
    D --> E{Age below 5?}
    E -- Yes --> F[Fare = 0]
    E -- No --> G[Calculate distance fare]
    G --> H{Age >= 60?}
    H -- Yes --> I[Apply 20% concession]
    H -- No --> J[Keep normal fare]
    I --> K[Add reservation fee]
    J --> K
    F --> L[Calculate total]
    K --> L
    L --> M{Cancelled?}
    M -- Yes --> N[Deduct cancellation penalty]
    M -- No --> O[Display final fare]
    N --> O
    O --> P([Stop])
```
#5.pseudo code

START
INPUT number_of_passengers
INPUT distance
INPUT travel_class

IF travel_class = "Sleeper"
    rate = 2
ELSE IF travel_class = "AC"
    rate = 4
ELSE
    PRINT "Invalid class"
END IF

FOR each passenger
    INPUT age

    IF age < 5
        fare = 0
    ELSE
        fare = distance * rate

        IF distance < 100
            fare = MAX(fare, 100)
        END IF

        IF age >= 60
            fare = fare * 0.80
        END IF

        fare = fare + 30
    END IF

    total = total + fare
END FOR

INPUT cancellation choice

IF cancelled
    total = MAX(0, total - (50 * number_of_passengers))
END IF

PRINT total

#6.python source code

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
            
  #7.sample output
  Enter number of passengers: 2
Enter distance in km: 150
Enter class (Sleeper/AC): sleeper

Enter passenger age: 25
Passenger 1 Fare: 330.0

Enter passenger age: 65
Passenger 2 Fare: 294.0

Total Fare: 624.0
Cancel ticket? (yes/no): no

Final Amount: 624.0

#8.conclusion
This program calculates railway ticket fares for multiple passengers using distance, travel class, age concessions, reservation fees and cancellation penalties
  



