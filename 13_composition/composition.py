class Engine:
    def start(self):
        return "Engine Started."
    
class Car:
    def __init__(self, engine):
        self.engine = engine # Composition
        
    def start(self):
        return self.engine.start()
    

# Example Usage
engine = Engine()
car = Car(engine)
print(car.start())