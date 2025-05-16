class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


# Example Usage
f = TemperatureConverter.celsius_to_fahrenheit(25)
print(f"25°C in Fahrenheit: {f}")