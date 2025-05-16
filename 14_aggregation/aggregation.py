class Employee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Aggregation

    def add_employee(self, employee):
        self.employees.append(employee)


# Example Usage
emp = Employee("Alice")
dept = Department("Engineering")
dept.add_employee(emp)
print(f"Department: {dept.name}, Employees: {[e.name for e in dept.employees]}")