#python source code

import math

# Input
total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))
threshold = float(input("Enter eligibility percentage: "))

# Validation
if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")

else:
    current = (attended / total) * 100

    print("Current Attendance:", round(current, 2), "%")

    if current >= threshold:
        print("Already Eligible")

    else:
        # Scenario 1: Attend all future classes
        required = math.ceil(
            (threshold * total / 100 - attended) /
            (1 - threshold / 100)
        )

        print("If all future classes are attended:")
        print("Required classes:", max(0, required))

        # Scenario 2: Attend 4 out of every 5 classes
        future_attended = 4
        future_total = 5

        found = False

        for i in range(1, 10001):
            new_attended = attended + (i // future_total) * future_attended
            new_total = total + i

            # Account for remaining classes in the 4-out-of-5 pattern
            new_attended = attended + (i // 5) * 4 + min(i % 5, 4)

            percentage = (new_attended / new_total) * 100

            if percentage >= threshold:
                print("If attending 4 out of every 5 classes:")
                print("Required classes:", i)
                found = True
                break

        if not found:
            print("Eligibility not reached in search range")

