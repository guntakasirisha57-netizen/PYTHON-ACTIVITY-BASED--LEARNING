
units = []
bills = []

for i in range(3):
    u = int(input("Enter units for month: "))
    units.append(u)

if any(u < 0 for u in units):
    print("Invalid units")
else:
    for u in units:
        if u <= 100:
            energy = u * 2
        elif u <= 200:
            energy = 200 + (u - 100) * 3
        else:
            energy = 500 + (u - 200) * 5

        surcharge = energy * 0.05
        bill = energy + 50 + surcharge - 20
        bills.append(bill)

    for i in range(3):
        print("Month", i + 1, "Bill: Rs.", bills[i])

    for i in range(1, 3):
        if bills[i - 1] > 0:
            increase = ((bills[i] - bills[i - 1])
                        / bills[i - 1]) * 100

            if increase > 20:
                print("Month", i + 1, ": Unusual Increase")
            else:
                print("Month", i + 1, ": Normal Increase")

