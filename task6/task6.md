1. Problem Statement
The Smart Parking Fee Management System calculates parking charges based on vehicle category, entry time, and exit time. It considers overnight parking, daily parking limits, and penalty conditions. The program validates time inputs, checks whether the entry and exit times are valid, calculates the total parking duration, applies the appropriate vehicle-based rates and penalties, and displays a detailed parking bill.
2. Algorithm
1. Start the program.
2. Define the hourly parking rates for different vehicle categories.
3. Define the daily parking limit and penalty charges.
4. Input the vehicle category, entry time, and exit time.
5. Validate the vehicle category and time inputs.
6. If the inputs are invalid, display an error message and stop.
7. Calculate the total parking duration, including overnight parking.
8. Calculate the parking fee based on the vehicle category and duration.
9. Apply the daily parking limit where applicable.
10. Check for overnight parking and apply the appropriate additional charges.
11. Check for penalty conditions and add penalty charges if required.
12. Calculate the final parking fee.
13. Display the vehicle category, parking duration, basic fee, penalties, and total amount.
14. Stop the program.
15. flowchart
16. ```mermaid
flowchart TD
    A([Start]) --> B[Define vehicle rates and parking limits]
    B --> C[Input vehicle category]
    C --> D[Input entry and exit times]
    D --> E{Are inputs valid?}
    E -- No --> F[Display error message]
    F --> Z([Stop])
    E -- Yes --> G[Calculate parking duration]
    G --> H{Is parking overnight?}
    H -- Yes --> I[Calculate overnight duration]
    H -- No --> J[Calculate regular duration]
    I --> K[Calculate base parking fee]
    J --> K
    K --> L[Apply daily parking limit]
    L --> M{Is there a penalty?}
    M -- Yes --> N[Add penalty charge]
    M -- No --> O[Calculate final fee]
    N --> O
    O --> P[Display detailed parking bill]
    P --> Z
```
code
from datetime import datetime

# Vehicle parking rates per hour
rates = {
    "two-wheeler": 20,
    "car": 40,
    "heavy vehicle": 60
}

# Maximum daily parking charges
daily_limits = {
    "two-wheeler": 200,
    "car": 400,
    "heavy vehicle": 600
}

OVERNIGHT_CHARGE = 50
PENALTY_CHARGE = 100

print("=" * 50)
print("       SMART PARKING FEE MANAGEMENT")
print("=" * 50)

# Input details
vehicle = input(
    "Enter vehicle category (two-wheeler/car/heavy vehicle): "
).strip().lower()

entry_time = input("Enter entry time (HH:MM): ").strip()
exit_time = input("Enter exit time (HH:MM): ").strip()

# Validate vehicle category
if vehicle not in rates:
    print("\nError: Invalid vehicle category.")

else:
    try:
        # Validate time format
        entry = datetime.strptime(entry_time, "%H:%M")
        exit = datetime.strptime(exit_time, "%H:%M")

        # Calculate duration
        entry_minutes = entry.hour * 60 + entry.minute
        exit_minutes = exit.hour * 60 + exit.minute

        if exit_minutes == entry_minutes:
            print("\nError: Entry and exit times cannot be identical.")

        else:
            # Handle overnight parking
            overnight = exit_minutes < entry_minutes

            if overnight:
                duration_minutes = (
                    24 * 60 - entry_minutes + exit_minutes
                )
            else:
                duration_minutes = exit_minutes - entry_minutes

            duration_hours = duration_minutes / 60

            # Charge for every started hour
            charged_hours = (duration_minutes + 59) // 60

            # Calculate complete 24-hour periods
            days = duration_minutes // (24 * 60)
            remaining_minutes = duration_minutes % (24 * 60)

            # Calculate base fee with daily limits
            full_day_fee = daily_limits[vehicle]
            hourly_rate = rates[vehicle]

            base_fee = (
                days * full_day_fee
                + min(
                    ((remaining_minutes + 59) // 60) * hourly_rate,
                    full_day_fee
                )
            )

            # Overnight charge
            overnight_fee = (
                OVERNIGHT_CHARGE if overnight else 0
            )

            # Penalty for parking beyond 24 hours
            penalty = 0

            if duration_minutes > 24 * 60:
                extra_periods = (
                    (duration_minutes - 24 * 60 + 1439) // 1440
                )
                penalty = extra_periods * PENALTY_CHARGE

            # Final bill
            total_fee = base_fee + overnight_fee + penalty

            print("\n" + "=" * 50)
            print("             PARKING BILL")
            print("=" * 50)

            print("Vehicle Category :", vehicle.title())
            print("Entry Time       :", entry_time)
            print("Exit Time        :", exit_time)
            print("Parking Duration :", round(duration_hours, 2), "hours")
            print("Charged Hours    :", charged_hours)
            print("Base Parking Fee : Rs.", base_fee)
            print("Overnight Charge : Rs.", overnight_fee)
            print("Penalty          : Rs.", penalty)

            print("-" * 50)
            print("TOTAL PARKING FEE: Rs.", total_fee)
            print("=" * 50)

    except ValueError:
        print(
            "\nError: Invalid time format. "
            "Enter valid times in HH:MM format."
        )
        print("Example: 09:30 or 18:45")
output:
==================================================
       SMART PARKING FEE MANAGEMENT
==================================================

==================================================
             PARKING BILL
==================================================
Vehicle Category : Car
Entry Time       : 18:30
Exit Time        : 22:15
Parking Duration : 3.75 hours
Charged Hours    : 4
Base Parking Fee : Rs. 160
Overnight Charge : Rs. 0
Penalty          : Rs. 0
--------------------------------------------------
TOTAL PARKING FEE: Rs. 160
==================================================
