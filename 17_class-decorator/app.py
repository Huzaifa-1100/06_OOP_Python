# Define the class decorator `add_greeting`
def add_greeting(cls):
    """
    This is a class decorator that modifies a class by adding a new method `greet()`.
    The `greet()` method returns the string "Hello from Decorator!".
    """
    # Define the new `greet` method
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the `greet` method to the class
    cls.greet = greet
    
    # Return the modified class
    return cls


# Apply the `add_greeting` decorator to the `Person` class
@add_greeting
class Person:
    """
    The `Person` class is decorated with `add_greeting`, which adds the `greet()` method.
    Without the decorator, this class would not have the `greet()` method.
    """
    pass


# Example Usage
if __name__ == "__main__":
    # Create an instance of the `Person` class
    person = Person()
    
    # Call the `greet()` method added by the decorator
    print(person.greet())  # Output: Hello from Decorator!