class Person:
    def __init__(self, name):
        self.name = name
        
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name) #call base class constructor
        self.subject = subject
        
# Example Usage
teacher1 = Teacher("Ameen", "AI")

print(f"Teacher Name: {teacher1.name}, Subject: {teacher1.subject}")