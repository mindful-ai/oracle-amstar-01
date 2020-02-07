class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)
    
'''
The last line of the code, makes a property object temperature.
Simply put, property attaches some code (get_temperature and set_temperature)
to the member attribute accesses (temperature).
Any code that retrieves the value of temperature will automatically
call get_temperature() instead of a dictionary (__dict__) look-up.
Similarly, any code that assigns a value to temperature will automatically
call set_temperature(). This is one cool feature in Python.
'''

class Celsius2:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
