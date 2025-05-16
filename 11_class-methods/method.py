class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


# Example Usage
b1 = Book("Python Basics")
b2 = Book("Advanced Python")
print(f"Total Books: {Book.total_books}")