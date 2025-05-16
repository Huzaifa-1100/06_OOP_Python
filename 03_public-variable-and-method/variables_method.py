class Car:
    def __init__(self, brand):
        self.brand = brand #Public variable
    
    def start(self):  # Public method
        print(f"{self.brand} car started")

# Example usage
car = Car("Honda")
print(car.brand)
car.start()