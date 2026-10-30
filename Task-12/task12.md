#1. Problem Statement
To calculate a student's current attendance percentage and find the minimum number of consecutive classes they must attend to reach the required eligibility percentage (75%).

#2. Assumptions
1. Total classes conducted and attended are entered by the user.
2. Minimum required attendance is 75%.
3. Future classes are attended continuously.
4. Attendance cannot be greater than total classes.
5. Invalid inputs are not accepted.

#3. Algorithm
1. Start.
2. Read total classes and attended classes.
3. Calculate current attendance percentage.
4. Check whether attendance is 75% or above.
5. If not, calculate minimum classes required.
6. Display attendance percentage and required classes.
7. Stop.

 ```mermaid

flowchart TD
    A([Start]) --> B[/Input total and attended classes/]
    B --> C{Valid input?}
    C -- No --> D[/Display Invalid Input/]
    D --> H([Stop])
    C -- Yes --> E[Calculate attendance percentage]
    E --> F{Attendance >= 75?}
    F -- Yes --> G[/Display Eligible/]
    F -- No --> I[Calculate required classes]
    I --> J[/Display classes needed/]
    G --> H
    J --> H
```

#5.pseudo code

START
INPUT total, attended

IF total <= 0 OR attended < 0 OR attended > total
    PRINT "Invalid Input"
ELSE
    percentage = attended / total * 100
    PRINT percentage

    IF percentage >= 75
        PRINT "Eligible"
    ELSE
        required = (3 * total - 4 * attended)
                   / 1
        required = CEILING(required / 1)
        PRINT required
    END IF
END IF

#6.python source code


total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid Input")

else:
    percentage = (attended / total) * 100

    print("Attendance:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Eligible for exam")
        print("No extra classes required")

    else:
        required = 0

        while ((attended + required) /
               (total + required)) * 100 < 75:
            required += 1

        print("Not Eligible currently")
        print("Classes required:", required)
#7.sample output
Enter total classes: 100
Enter attended classes: 60

Attendance: 60.0 %
Not Eligible currently
Classes required: 60

#8.conclusion
This program calculates current attendance and determines the minimum number of consecutive classes a student must attend to reach 75% eligibility.
  
  
