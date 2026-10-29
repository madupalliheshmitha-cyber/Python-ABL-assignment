# Multi-Stage Examination Eligibility System

print("=" * 55)
print("    MULTI-STAGE EXAMINATION ELIGIBILITY SYSTEM")
print("=" * 55)

# Input student details
student_name = input("Enter student name: ").strip()

try:
    attendance = float(input("Enter attendance percentage: "))
    lab_completed = input(
        "Are all laboratory activities completed? (yes/no): "
    ).strip().lower()

    internal_marks = float(input("Enter internal assessment marks (out of 100): "))

    fees_cleared = input(
        "Are all fees cleared? (yes/no): "
    ).strip().lower()

    # Validate inputs
    if not student_name:
        print("Error: Student name cannot be empty.")

    elif not 0 <= attendance <= 100:
        print("Error: Attendance must be between 0 and 100.")

    elif lab_completed not in ("yes", "no"):
        print("Error: Enter yes or no for laboratory completion.")

    elif not 0 <= internal_marks <= 100:
        print("Error: Internal marks must be between 0 and 100.")

    elif fees_cleared not in ("yes", "no"):
        print("Error: Enter yes or no for fee clearance.")

    else:
        unmet_requirements = []

        # Check attendance
        if attendance < 75:
            unmet_requirements.append(
                "Attendance is below 75%."
            )

        # Check laboratory completion
        if lab_completed == "no":
            unmet_requirements.append(
                "Laboratory activities are incomplete."
            )

        # Check internal assessment marks
        if internal_marks < 40:
            unmet_requirements.append(
                "Internal assessment marks are below 40."
            )

        # Check fee clearance
        if fees_cleared == "no":
            unmet_requirements.append(
                "Examination fees are not fully cleared."
            )

        # Display eligibility report
        print("\n" + "=" * 55)
        print("             ELIGIBILITY REPORT")
        print("=" * 55)

        print("Student Name       :", student_name)
        print("Attendance         :", attendance, "%")
        print("Laboratory Status  :", lab_completed.title())
        print("Internal Marks     :", internal_marks, "/ 100")
        print("Fee Clearance      :", fees_cleared.title())

        print("-" * 55)

        if len(unmet_requirements) == 0:
            print("Final Status: ELIGIBLE")
            print("All eligibility requirements are satisfied.")

        else:
            print("Final Status: NOT ELIGIBLE")
            print("\nUnmet Requirements:")

            for number, requirement in enumerate(
                unmet_requirements, start=1
            ):
                print(f"{number}. {requirement}")

        print("=" * 55)

except ValueError:
    print("Error: Please enter valid numeric values for attendance and marks.")
