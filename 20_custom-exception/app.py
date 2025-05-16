# Define the custom exception `InvalidAgeError`
class InvalidAgeError(Exception):
    """
    This is a custom exception class that inherits from Python's built-in `Exception` class.
    It is used to raise an error when an invalid age (e.g., less than 18) is encountered.
    """
    def __init__(self, message="Invalid age. Age must be 18 or above."):
        """
        The constructor initializes the exception with a default error message.
        You can also provide a custom message when raising the exception.
        """
        self.message = message
        super().__init__(self.message)


# Define the function `check_age` that raises the custom exception
def check_age(age):
    """
    This function checks if the provided age is valid (i.e., 18 or above).
    If the age is less than 18, it raises the `InvalidAgeError` exception.
    Otherwise, it returns a success message.
    """
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")  # Raise the custom exception
    return "Age is valid."


# Example Usage
if __name__ == "__main__":
    try:
        # Test the `check_age` function with different ages
        age = int(input("Enter your age: "))  # Get user input
        result = check_age(age)  # Call the function
        print(result)  # Print the result if no exception is raised
    except InvalidAgeError as e:
        # Handle the custom exception and print the error message
        print(f"Error: {e}")
    except ValueError:
        # Handle cases where the user enters a non-integer value
        print("Error: Please enter a valid integer for age.")