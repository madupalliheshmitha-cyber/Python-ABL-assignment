# Nested Loop Calendar Generator

weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

print("=" * 35)
print("      MONTHLY CALENDAR GENERATOR")
print("=" * 35)

month = input("Enter month name: ").strip()

try:
    start_day = int(input(
        "Enter starting weekday (0=Sun, 1=Mon, ..., 6=Sat): "
    ))

    days = int(input("Enter number of days in the month: "))

    # Validate inputs
    if not month:
        print("Error: Month name cannot be empty.")

    elif start_day < 0 or start_day > 6:
        print("Error: Starting weekday must be between 0 and 6.")

    elif days not in [28, 29, 30, 31]:
        print("Error: A month must have 28, 29, 30, or 31 days.")

    else:
        print("\n" + "=" * 35)
        print(" " * 12 + month.title())
        print("=" * 35)

        # Print weekday headings
        for day in weekdays:
            print(f"{day:>5}", end="")
        print()

        print("-" * 35)

        # Align the first date
        for space in range(start_day):
            print(" " * 5, end="")

        current_day = 1
        weekday_position = start_day

        # Outer loop processes weeks
        while current_day <= days:

            # Inner loop processes weekdays
            while weekday_position < 7 and current_day <= days:
                print(f"{current_day:>5}", end="")
                current_day += 1
                weekday_position += 1

            print()
            weekday_position = 0

        print("=" * 35)
        print("Calendar generated successfully.")

except ValueError:
    print("Error: Please enter valid numeric values.")
