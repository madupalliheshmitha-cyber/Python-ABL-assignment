import math

# Attendance Details
total_classes = 60
attended_classes = 42
eligibility_threshold = 75

# Validate Inputs
if (total_classes <= 0 or attended_classes < 0
        or attended_classes > total_classes
        or not 0 < eligibility_threshold <= 100):

    print("Invalid attendance details.")

else:
    # Calculate Current Attendance
    current_percentage = (attended_classes / total_classes) * 100

    print("=" * 50)
    print("       ATTENDANCE RECOVERY REPORT")
    print("=" * 50)

    print("Total Classes Conducted :", total_classes)
    print("Classes Attended        :", attended_classes)
    print("Current Attendance      :", round(current_percentage, 2), "%")
    print("Eligibility Threshold   :", eligibility_threshold, "%")

    # Calculate Required Classes
    if current_percentage >= eligibility_threshold:
        required_classes = 0

        print("\nStatus: Already eligible.")
        print("Additional Classes Required:", required_classes)

    elif eligibility_threshold == 100:
        required_classes = total_classes - attended_classes

        print("\nStatus: Below eligibility threshold.")
        print("Attend all remaining classes to reach 100%.")

    else:
        required_classes = math.ceil(
            (eligibility_threshold * total_classes
             - 100 * attended_classes)
            / (100 - eligibility_threshold)
        )

        print("\nStatus: Below eligibility threshold.")
        print("Minimum Consecutive Classes Required:", required_classes)

    # Future Attendance Scenarios
    scenarios = [
        ("Attend all next 10 classes", 10, 10),
        ("Attend 8 of next 10 classes", 10, 8),
        ("Attend 5 of next 10 classes", 10, 5)
    ]

    print("\nFUTURE ATTENDANCE SCENARIOS")
    print("-" * 50)

    for description, future_classes, future_attended in scenarios:
        projected_total = total_classes + future_classes
        projected_attended = attended_classes + future_attended

        projected_percentage = (
            projected_attended / projected_total
        ) * 100

        print(description)
        print("Projected Attendance:", round(projected_percentage, 2), "%")

        if projected_percentage >= eligibility_threshold:
            print("Eligibility: Eligible")
        else:
            print("Eligibility: Not yet eligible")

        print("-" * 50)

    print("Report generated successfully.")
