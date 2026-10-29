```python
# Integrated Student Record Consistency Checker

# Valid course names
valid_courses = ("CSE", "ECE", "EEE", "IT")

# Student records stored as tuples inside a list
students = [
    (101, "Ravi", 85, 92, "CSE"),
    (102, "Sita", 90, 88, "ECE"),
    (101, "Kiran", 75, 95, "CSE"),
    (103, "", 105, 70, "IT"),
    (104, "Anu", 80, 110, ""),
    (None, "Rahul", 65, 85, "EEE")
]

# List to store validation errors
errors = []

# Check each student record
for student in students:
    student_id, name, marks, attendance, course = student
    student_errors = []

    # Check missing student ID
    if student_id is None or student_id == "":
        student_errors.append("Missing student ID")

    # Check duplicate student ID
    elif sum(1 for s in students if s[0] == student_id) > 1:
        student_errors.append("Duplicate student ID")

    # Check student name
    if name is None or name == "":
        student_errors.append("Missing student name")

    # Check marks
    if marks is None or marks == "":
        student_errors.append("Missing marks")
    elif not isinstance(marks, (int, float)) or not 0 <= marks <= 100:
        student_errors.append("Invalid marks")

    # Check attendance
    if attendance is None or attendance == "":
        student_errors.append("Missing attendance")
    elif (
        not isinstance(attendance, (int, float))
        or not 0 <= attendance <= 100
    ):
        student_errors.append("Invalid attendance")

    # Check course
    if course is None or course == "":
        student_errors.append("Missing course")
    elif course not in valid_courses:
        student_errors.append("Invalid course")

    # Store errors if found
    if student_errors:
        errors.append((student_id, student_errors))

# Display validation results
print("STUDENT RECORD VALIDATION REPORT")
print("--------------------------------")

if len(errors) == 0:
    print("All student records are consistent.")
else:
    for record in errors:
        print("\nStudent ID:", record[0])

        for error in record[1]:
            print("-", error)

# Display summary
print("\nTotal student records:", len(students))
print("Records with errors:", len(errors))
print("Records without errors:", len(students) - len(errors))
```
