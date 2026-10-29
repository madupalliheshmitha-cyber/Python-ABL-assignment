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
