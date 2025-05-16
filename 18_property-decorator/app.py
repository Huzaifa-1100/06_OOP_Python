class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        del self._price


# Example Usage
p = Product(100)
print(f"Price: {p.price}")
p.price = 200
print(f"Updated Price: {p.price}")
del p.price