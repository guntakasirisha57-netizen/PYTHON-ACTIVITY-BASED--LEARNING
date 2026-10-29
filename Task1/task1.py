
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

