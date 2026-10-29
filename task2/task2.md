1. Problem Statement
The Employee Payroll and Deduction Analysis system calculates employees' salaries based on basic pay, allowances, overtime, and incentives. It determines the gross salary by adding all earnings and calculates deductions using progressive deduction rates. Finally, the program calculates the net salary after deducting the applicable amounts and generates a formatted salary statement for each employee.
2. Algorithm
1. Start the program.
2. Initialize employee details, including employee ID, name, and basic salary.
3. Calculate allowances based on the basic salary.
4. Calculate overtime pay and incentives.
5. Calculate gross salary by adding basic salary, allowances, overtime pay, and incentives.
6. Calculate deductions using progressive deduction slabs.
7. Calculate net salary by subtracting total deductions from gross salary.
8. Display the employee's salary statement, including earnings, deductions, and net salary.
9. Repeat the process for all employees.
10. Stop the program.
3. Flowchart Using Mermaid
```mermaid
flowchart TD
    A([Start]) --> B[Enter employee details]
    B --> C[Calculate allowances]
    C --> D[Calculate overtime and incentives]
    D --> E[Calculate gross salary]
    E --> F[Calculate progressive deductions]
    F --> G[Calculate net salary]
    G --> H[Generate salary statement]
    H --> I{More employees?}
    I -- Yes --> B
    I -- No --> J([Stop])
```

4. Python Program Code
# Employee Payroll and Deduction Analysis

# Employee details stored as tuples inside a list
employees = [
    (101, "Ravi", 30000, 5000, 2000, 3000),
    (102, "Sita", 45000, 7000, 3000, 5000),
    (103, "Kiran", 20000, 3000, 1000, 1500)
]

# Progressive deduction slabs
def calculate_deduction(gross_salary):
    deduction = 0
    if gross_salary <= 20000:
        deduction = gross_salary * 0.05

    elif gross_salary <= 40000:
        deduction = (20000 * 0.05) + (
            (gross_salary - 20000) * 0.10
        )
    else:
        deduction = (
            (20000 * 0.05)
            + (20000 * 0.10)
            + ((gross_salary - 40000) * 0.15)
        )
    return deduction
# Process employee payroll
for employee in employees:

    emp_id, name, basic, allowances, overtime, incentives = employee

    # Calculate gross salary
    gross_salary = basic + allowances + overtime + incentives

    # Calculate deductions
    deduction = calculate_deduction(gross_salary)

    # Calculate net salary
    net_salary = gross_salary - deduction

    # Display salary statement
    print("\n====================================")
    print("       EMPLOYEE SALARY STATEMENT")
    print("====================================")
    print("Employee ID       :", emp_id)
    print("Employee Name     :", name)
    print("Basic Salary      : Rs.", basic)
    print("Allowances        : Rs.", allowances)
    print("Overtime Pay      : Rs.", overtime)
    print("Incentives        : Rs.", incentives)
    print("------------------------------------")
    print("Gross Salary      : Rs.", gross_salary)
    print("Total Deductions  : Rs.", round(deduction, 2))
    print("Net Salary        : Rs.", round(net_salary, 2))
    print("====================================")
output:
    ====================================
       EMPLOYEE SALARY STATEMENT
====================================
Employee ID       : 101
Employee Name     : Ravi
Basic Salary      : Rs. 30000
Allowances        : Rs. 5000
Overtime Pay      : Rs. 2000
Incentives        : Rs. 3000
------------------------------------
Gross Salary      : Rs. 40000
Total Deductions  : Rs. 3000.0
Net Salary        : Rs. 37000.0
====================================

====================================
       EMPLOYEE SALARY STATEMENT
====================================
Employee ID       : 102
Employee Name     : Sita
Basic Salary      : Rs. 45000
Allowances        : Rs. 7000
Overtime Pay      : Rs. 3000
Incentives        : Rs. 5000
------------------------------------
Gross Salary      : Rs. 60000
Total Deductions  : Rs. 6000.0
Net Salary        : Rs. 54000.0
====================================

====================================
       EMPLOYEE SALARY STATEMENT
====================================
Employee ID       : 103
Employee Name     : Kiran
Basic Salary      : Rs. 20000
Allowances        : Rs. 3000
Overtime Pay      : Rs. 1000
Incentives        : Rs. 1500
------------------------------------
Gross Salary      : Rs. 25500
Total Deductions  : Rs. 750.0
Net Salary        : Rs. 24750.0
====================================
