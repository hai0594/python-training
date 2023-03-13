employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
employees_with_salary = []
for employee in employees:
    name,hour,rate = employee
    salary = hour * rate 
    employees_with_salary.append((name,hour,rate,salary))

amount = len(employees_with_salary)

total_salary = 0
for employee in employees_with_salary:
    total_salary += employee[3]
    ave_salary = total_salary/amount

for employee in employees_with_salary:
    if employee[3] > ave_salary:
        print(employee[0])