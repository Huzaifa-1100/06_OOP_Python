# Define the Logger class
class Logger:
    # Constructor (__init__) is called when an object is created
    def __init__(self):
        """
        The constructor method (__init__) is automatically called when a new object is created.
        It initializes the object and prints a message indicating that the object has been created.
        """
        print("Logger created.")  # Message printed when the object is created

    # Destructor (__del__) is called when an object is destroyed (garbage collected)
    def __del__(self):
        """
        The destructor method (__del__) is automatically called when an object is about to be destroyed.
        This typically happens when there are no more references to the object, or when the program ends.
        """
        print("Logger destroyed.")  # Message printed when the object is destroyed


# Example Usage
if __name__ == "__main__":
    # Step 1: Create an instance of the Logger class
    logger = Logger()  # Constructor is called here, printing "Logger created."

    # Step 2: Perform some operations (simulating the object's lifecycle)
    print("Performing some operations...")

    # Step 3: Delete the object explicitly (optional)
    del logger  # Destructor is called here, printing "Logger destroyed."

    # If `del logger` is not used, the destructor will still be called automatically
    # when the program ends and the object goes out of scope.