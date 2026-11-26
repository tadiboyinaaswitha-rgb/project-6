# PROJECT 6 – TRAFFIC VIOLATION PENALTY CALCULATOR

## About the Project
The Traffic Violation Penalty Calculator project is designed to record and evaluate traffic offences committed by a driver using vehicle category, violation type, and repeat-offence status. It calculates cumulative fines and demerit points and checks whether the driver's license should be suspended.

## Technologies Used
- **Python** – Used to build the e-challan penalty and demerit tracking system.
- **Lists & Tuples** – Used to store violation records for summary output.
- **Loops** – Used to process multiple traffic violations per driver.
- **Conditional Statements** – Used to assign fines/points, apply multipliers, and check license status.
- **String Methods** – Used to standardize vehicle category, offence name, and repeat input.

## Main Features
- Accepts driver name, vehicle category (`TWO-WHEELER`, `CAR`, `HEAVY`), and number of violations.
- Assigns base fines and demerit points for offences (`HELMET`, `SIGNAL`, `SPEEDING`, `DRUNK`).
- Applies a `1.5x` multiplier for heavy vehicles and doubles fines (`2x`) with `+2` demerit points for repeat offences.
- Flags license disqualification when cumulative demerit points reach `10` or more.

## Algorithm
1. Start the program.
2. Read driver name, vehicle category, and number of violations.
3. Set vehicle multiplier (`1.5` for `HEAVY`, else `1.0`) and initialize fine, points, and records list.
4. Loop through each violation to read offence type and repeat status.
5. Determine base fine and demerit points, apply multipliers, and update totals.
6. Save each violation record in the list.
7. Print the e-challan summary with total penalty and demerit points.
8. Display license status (`DISQUALIFIED / SUSPENDED` if points `>= 10`, else `ACTIVE`).
9. Stop the program.

## Sample Output
Enter driver name: Vikram
Enter vehicle category (TWO-WHEELER / CAR / HEAVY): CAR
Enter number of violations: 2

Violation 1:
  Offence (HELMET / SIGNAL / SPEEDING / DRUNK): SPEEDING
  Repeat offence? (YES / NO): YES

Violation 2:
  Offence (HELMET / SIGNAL / SPEEDING / DRUNK): SIGNAL
  Repeat offence? (YES / NO): NO

----- E-CHALLAN VIOLATION SUMMARY -----
Driver Name       : Vikram
Vehicle Category  : CAR
  - SPEEDING (Repeat: YES) -> Fine: Rs. 3000.00 | Points: 6
  - SIGNAL (Repeat: NO) -> Fine: Rs. 1000.00 | Points: 3
---------------------------------------
Total Penalty     : Rs. 4000.00
Total Demerit Pts : 9
License Status    : ACTIVE (Warning Issued)

## Conclusion
This project helps compute traffic challan penalties and track demerit points across repeated violations. It demonstrates Python concepts such as lists, tuples, loops, conditional statements, and string methods.
