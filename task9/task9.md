1. Problem Statement
The Multi-Stage Examination Eligibility System determines whether a student is eligible to appear for the final examination based on attendance percentage, laboratory completion, internal assessment marks, and fee-clearance status. The program validates the student's input details and checks each eligibility requirement independently. If any condition is not satisfied, it reports every unmet requirement instead of stopping after finding the first failure. Finally, it displays the student's eligibility status and a list of pending requirements.
2. Algorithm
1. Start the program.
2. Input the student's name and attendance percentage.
3. Input laboratory completion status, internal assessment marks, and fee-clearance status.
4. Validate all input values.
5. Set the eligibility requirements:
   - Attendance must be at least 75%.
   - All required laboratory work must be completed.
   - Internal assessment marks must be at least 40 out of 100.
   - All examination fees must be cleared.
6. Create an empty list to store unmet requirements.
7. Check the attendance percentage.
8. If attendance is below 75%, add an attendance warning to the list.
9. Check laboratory completion. If incomplete, add a laboratory warning.
10. Check internal assessment marks. If below 40, add an assessment warning.
11. Check fee clearance. If fees are pending, add a fee warning.
12. If the list is empty, declare the student eligible.
13. Otherwise, declare the student not eligible and display every unmet requirement.
14. Display the final eligibility report.
15. Stop the program.
16. flowchart:
17. ```mermaid
flowchart TD
    A([Start]) --> B[Input student details]
    B --> C[Validate input values]
    C --> D{Are inputs valid?}
    D -- No --> E[Display input error]
    E --> Z([Stop])
    D -- Yes --> F[Create empty unmet requirements list]
    F --> G{Attendance at least 75 percent?}
    G -- No --> H[Add attendance requirement]
    G -- Yes --> I{Laboratory completed?}
    H --> I
    I -- No --> J[Add laboratory requirement]
    I -- Yes --> K{Internal marks at least 40?}
    J --> K
    K -- No --> L[Add assessment requirement]
    K -- Yes --> M{Fees cleared?}
    L --> M
    M -- No --> N[Add fee clearance requirement]
    M -- Yes --> O{Any unmet requirements?}
    N --> O
    O -- Yes --> P[Display not eligible and all unmet requirements]
    O -- No --> Q[Display eligible status]
    P --> R[Display final report]
    Q --> R
    R --> Z
```
code:
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
output:
=======================================================
    MULTI-STAGE EXAMINATION ELIGIBILITY SYSTEM
=======================================================

=======================================================
             ELIGIBILITY REPORT
=======================================================
Student Name       : Heshmitha
Attendance         : 68.0 %
Laboratory Status  : No
Internal Marks     : 32.0 / 100
Fee Clearance      : No
-------------------------------------------------------
Final Status: NOT ELIGIBLE

Unmet Requirements:
1. Attendance is below 75%.
2. Laboratory activities are incomplete.
3. Internal assessment marks are below 40.
4. Examination fees are not fully cleared.
=======================================================
