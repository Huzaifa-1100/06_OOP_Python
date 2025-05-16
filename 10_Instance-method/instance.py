class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} ({self.breed}) says woof!")
        
# Example Usage
dog = Dog("Buddy", "Goldent Retriever")

dog.bark()