#python source code

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

