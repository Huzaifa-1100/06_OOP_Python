class Employee:
     def __init__(self, name, salary, ssn):
        self.name = name         # Public
        self._salary = salary    # Protected
        self.__ssn = ssn         # Private
        
# Example Usage
emp = Employee("John", 50000, "123-45-6789")
print(emp.name)        # Public: Accessible
print(emp._salary)     # Protected: Accessible but not recommended
try:
    print(emp.__ssn)   # Private: Not accessible directly
except AttributeError:
    print("Private variable __ssn cannot be accessed directly.")