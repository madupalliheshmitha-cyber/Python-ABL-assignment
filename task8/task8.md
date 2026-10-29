1. Problem Statement
The Nested Loop Calendar Generator generates a formatted monthly calendar using the supplied month name, starting weekday, and number of days in the month. The program validates the input values, ensures that the number of days is valid, and uses nested loops to arrange dates into correctly aligned weeks. It displays the calendar in a clear tabular format, placing each date under the appropriate weekday.
2. Algorithm
1. Start the program.
2. Input the month name, starting weekday, and number of days in the month.
3. Store the weekday names from Sunday to Saturday.
4. Validate the starting weekday and the number of days.
5. If the inputs are invalid, display an error message and stop.
6. Print the calendar heading and weekday names.
7. Use spaces to align the first date under the correct weekday.
8. Use an outer loop to process each week.
9. Use an inner loop to print the dates under the seven weekdays.
10. Print a new line after each week.
11. Continue until all dates have been displayed.
12. Stop the program.
13. flowchart
14. ```mermaid
flowchart TD
    A([Start]) --> B[Input month name starting weekday and number of days]
    B --> C[Validate input values]
    C --> D{Are inputs valid?}
    D -- No --> E[Display error message]
    E --> Z([Stop])
    D -- Yes --> F[Display calendar heading and weekdays]
    F --> G[Align first date using blank spaces]
    G --> H[Initialize date counter]
    H --> I{Are all dates printed?}
    I -- No --> J[Print date in correct column]
    J --> K[Move to next weekday]
    K --> L{End of week?}
    L -- Yes --> M[Print new line]
    L -- No --> N[Continue current row]
    M --> O[Increment date counter]
    N --> O
    O --> I
    I -- Yes --> P[Display completed calendar]
    P --> Z
```
code
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
output:
===================================
      MONTHLY CALENDAR GENERATOR
===================================

===================================
            October
===================================
  Sun  Mon  Tue  Wed  Thu  Fri  Sat
-----------------------------------
                        1    2    3
    4    5    6    7    8    9   10
   11   12   13   14   15   16   17
   18   19   20   21   22   23   24
   25   26   27   28   29   30   31
===================================
Calendar generated successfully.
