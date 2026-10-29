```python
# Examination Result and Grace-Mark Validation

MAX_MARKS = 100
PASS_MARKS = 35
MAX_GRACE = 5

# Student records: ID, Name, Subject Marks
students = [
    (101, "Anu", [78, 82, 90]),
    (102, "Ravi", [65, 58, 72]),
    (103, "Kiran", [32, 70, 68]),
    (104, "Sita", [25, 40, 60])
]

# Process each student's result
for student in students:
    student_id, name, original_marks = student
    marks = original_marks.copy()
    grace_awarded = 0

    # Validate marks
    invalid = any(
        not isinstance(mark, (int, float))
        or isinstance(mark, bool)
        or mark < 0
        or mark > MAX_MARKS
        for mark in marks
    )

    if invalid:
        print("\nInvalid marks for:", name)
        continue

    # Identify failed subjects
    failed = [
        i for i, mark in enumerate(marks)
        if mark < PASS_MARKS
    ]

    # Apply grace marks if exactly one subject has a small shortfall
    if len(failed) == 1:
        i = failed[0]
        shortfall = PASS_MARKS - marks[i]

        if 0 < shortfall <= MAX_GRACE:
            grace_awarded = shortfall
            marks[i] += grace_awarded

    # Recheck subject-wise pass criteria
    passed = all(mark >= PASS_MARKS for mark in marks)

    # Calculate total and percentage
    total = sum(marks)
    percentage = total / (len(marks) * MAX_MARKS) * 100

    # Determine final classification
    if not passed:
        classification = "Fail"
    elif percentage >= 75:
        classification = "Distinction"
    elif percentage >= 60:
        classification = "First Class"
    elif percentage >= 50:
        classification = "Second Class"
    else:
        classification = "Pass"

    # Display formatted result statement
    print("\n========================================")
    print("       EXAMINATION RESULT STATEMENT")
    print("========================================")
    print("Student ID       :", student_id)
    print("Student Name     :", name)
    print("Original Marks   :", original_marks)
    print("Final Marks      :", marks)
    print("Grace Marks      :", grace_awarded)
    print("----------------------------------------")
    print("Total Marks      :", total, "/", len(marks) * MAX_MARKS)
    print("Percentage       :", round(percentage, 2), "%")
    print("Final Result     :", classification)
    print("========================================")
```
