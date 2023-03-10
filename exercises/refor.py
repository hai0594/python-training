employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
employees_with_sal = []
for employee in employees:
    name,hour,rate = employee
    salary = hour * rate
    employees_with_sal.append((name,hour,rate,salary))
print(employees_with_sal)

total = 0
for employee in employees_with_sal:
    total += employee[3]
    ave = total/len(employees_with_sal)
print(ave)
for employee in employees_with_sal:
    if employee[3] > ave:
        print(employee[0])