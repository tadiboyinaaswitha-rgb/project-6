driver = input("Enter driver name: ")
vehicle_cat = input("Enter vehicle category (TWO-WHEELER / CAR / HEAVY): ").upper()
n = int(input("Enter number of violations: "))

veh_mult = 1.5 if vehicle_cat == "HEAVY" else 1.0
total_fine = 0.0
total_points = 0
records = []

for i in range(n):
    print(f"\nViolation {i + 1}:")
    offence = input("  Offence (HELMET / SIGNAL / SPEEDING / DRUNK): ").upper()
    repeat = input("  Repeat offence? (YES / NO): ").upper()

    if offence == "HELMET":
        base, pts = 500, 2
    elif offence == "SIGNAL":
        base, pts = 1000, 3
    elif offence == "SPEEDING":
        base, pts = 1500, 4
    elif offence == "DRUNK":
        base, pts = 5000, 8
    else:
        base, pts = 500, 1

    fine = base * veh_mult
    if repeat == "YES":
        fine *= 2
        pts += 2

    total_fine += fine
    total_points += pts
    records.append((offence, repeat, fine, pts))

print("\n----- E-CHALLAN VIOLATION SUMMARY -----")
print("Driver Name       :", driver)
print("Vehicle Category  :", vehicle_cat)
for r in records:
    print(f"  - {r[0]} (Repeat: {r[1]}) -> Fine: Rs. {r[2]:.2f} | Points: {r[3]}")
print("---------------------------------------")
print(f"Total Penalty     : Rs. {total_fine:.2f}")
print(f"Total Demerit Pts : {total_points}")
if total_points >= 10:
    print("License Status    : DISQUALIFIED / SUSPENDED")
else:
    print("License Status    : ACTIVE (Warning Issued)")
