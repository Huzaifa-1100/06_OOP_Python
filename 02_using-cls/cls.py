class Counter:
    count = 0 # class variable
    def __init__(self):
        Counter.count += 1 # Increment count when a new object is created
        
    @classmethod
    def get_count(cls):
        return cls.count

# Example Usage

c1 = Counter() 
c2 = Counter()
c3 = Counter()
print(F"Total objects created: {Counter.get_count()}")