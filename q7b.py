

class Employee:
    def __init__(self, name,  employee_id, department, salary):
        self.Name = name
        self.Employee_id = employee_id
        self.Department = department
        self.Salary = salary

    def update_salary(self, department, salary):
        if self.Department == department:
            self.Salary = salary

employees = [
    Employee("John", 101, "HR", 5000),
    Employee("Alice", 102, "Finance", 6000),
    Employee("Bob", 103, "HR", 4500),
    Employee("Eva", 104, "Sales", 5500)
]

department = input("Enter the department name: ")
new_salary = float(input("Enter the new salary: "))

for employee in employees:
    employee.update_salary(department, new_salary)

print("Updated salaries for employees in the", department, "department:")
for employee in employees:
    if employee.Department == department:
        print("Employee:", employee.Name, "ID:", employee.Employee_id, "Salary:", employee.Salary)