#python source code

usage = float(input("Enter data usage (GB): "))
days = int(input("Enter required validity: "))
budget = float(input("Enter budget: "))

plans = [
    ["Basic", 199, 2, 28],
    ["Standard", 299, 3, 56],
    ["Premium", 399, 5, 84]
]

best = None

for p in plans:
    extra = max(0, usage - p[2]) * 10
    total = p[1] + extra

    if p[3] >= days and total <= budget:
        if best is None or total < best[0]:
            best = (total, p[0], extra)

if best:
    print("\nBest Plan:", best[1])
    print("Extra Charges: Rs.", best[2])
    print("Total Cost: Rs.", best[0])
else:
    print("No suitable plan available")

