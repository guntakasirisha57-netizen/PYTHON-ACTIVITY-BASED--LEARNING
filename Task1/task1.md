#1. Problem Statement
To develop a Python program that selects eligible students for scholarships based on aggregate marks, subject-wise minimum marks, attendance, and family income. Eligible students are ranked by aggregate marks, and ties are resolved using attendance.

#2. Assumptions
1. Aggregate marks must be at least 75%.
2. Each subject mark must be at least 60%.
3. Attendance must be at least 75%.
4. Annual family income must not exceed ₹2,50,000.
5. Students with higher aggregate marks get higher ranks.
6. If aggregate marks are equal, the student with higher attendance gets the higher rank.

#3.Algorithm
1. Start.
2. Input student details and marks.
3. Check subject marks, aggregate, attendance, and income.
4. If all conditions are satisfied, declare the student eligible.
5. Rank eligible students by aggregate marks.
6. Resolve ties using attendance.
7. Display eligibility and rank.
8. Stop.

 ```mermaid

flowchart TD
    A([Start]) --> B[/Input student details/]
    B --> C[Calculate aggregate marks]
    C --> D{All eligibility conditions satisfied?}
    D -- No --> E[Reject student]
    D -- Yes --> F[Add to eligible list]
    E --> G{More students?}
    F --> G
    G -- Yes --> B
    G -- No --> H[Sort by aggregate and attendance]
    H --> I[Display rank and results]
    I --> J([Stop])
```
#5.pseudo code
START
INPUT details of students

FOR each student
    Calculate aggregate marks

    IF aggregate >= 75 AND all subjects >= 60
       AND attendance >= 75 AND income <= 250000
        Add student to eligible list
    END IF
END FOR

Sort eligible students by aggregate and attendance
Display students with ranks
STOP

#6.python source code

students = []

for i in range(3):
    print("\nEnter student details")
    name = input("Name: ")
    m1 = float(input("Subject 1 marks: "))
    m2 = float(input("Subject 2 marks: "))
    m3 = float(input("Subject 3 marks: "))
    attendance = float(input("Attendance: "))
    income = float(input("Family income: "))

  avg = (m1 + m2 + m3) / 3

    if (avg >= 75 and min(m1, m2, m3) >= 60
            and attendance >= 75 and income <= 250000):
        students.append([name, avg, attendance])

students.sort(key=lambda s: (s[1], s[2]), reverse=True)

print("\n--- Scholarship Results ---")
if not students:
    print("No eligible students")
else:
    for rank, s in enumerate(students, 1):
        print(rank, s[0], "Aggregate:", round(s[1], 2),
              "Attendance:", s[2], "%")

 #7.sample output
--- Scholarship Results ---
1 Ravi Aggregate: 90.0 Attendance: 90.0 %
2 Sita Aggregate: 80.0 Attendance: 85.0 %

#8.conclusion
The program checks scholarship eligibility, ranks eligible students based on aggregate marks, and resolves ties using attendance. It uses simple Python conditions, lists, and sorting.
              


