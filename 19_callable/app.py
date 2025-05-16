class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return self.factor * x
    
    
# Example usage

m = Multiplier(3)
print(m(5)) # output 15
print(callable(m)) # output: true