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

        # Convert times into minutes
        entry_minutes = entry.hour * 60 + entry.minute
        exit_minutes = exit.hour * 60 + exit.minute

        if exit_minutes == entry_minutes:
            print("\nError: Entry and exit times cannot be identical.")

        else:
            # Calculate parking duration
            overnight = exit_minutes < entry_minutes

            if overnight:
                duration_minutes = (
                    24 * 60 - entry_minutes + exit_minutes
                )
            else:
                duration_minutes = exit_minutes - entry_minutes

            duration_hours = duration_minutes / 60

            # Charge for each started hour
            charged_hours = (duration_minutes + 59) // 60

            # Calculate complete days and remaining hours
            days = duration_minutes // 1440
            remaining_minutes = duration_minutes % 1440

            # Calculate base fee using daily limits
            full_day_fee = daily_limits[vehicle]
            hourly_rate = rates[vehicle]

            remaining_hours = (remaining_minutes + 59) // 60

            base_fee = (
                days * full_day_fee
                + min(remaining_hours * hourly_rate, full_day_fee)
            )

            # Apply overnight charge
            overnight_fee = (
                OVERNIGHT_CHARGE if overnight else 0
            )

            # Apply penalty for parking beyond 24 hours
            penalty = 0

            if duration_minutes > 1440:
                extra_periods = (
                    (duration_minutes - 1440 + 1439) // 1440
                )
                penalty = extra_periods * PENALTY_CHARGE

            # Calculate final fee
            total_fee = base_fee + overnight_fee + penalty

            # Display parking bill
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
        print("\nError: Invalid time format.")
        print("Enter valid times in HH:MM format, such as 09:30 or 18:45.")
