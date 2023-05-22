"""
Converting between Celsius and Fahrenheit involves a basic calculation and provides a good exercise for writing functions that take in a numeric input and return a numeric output.
 This exercise tests your ability to use Python’s math operators and translate math equations into Python code.

Exercise Description

Write a convertToFahrenheit() function with a degreesCelsius parameter.
 This function returns the number of this temperature in degrees Fahrenheit.
   Then write a function named convertToCelsius() with a degreesFahrenheit parameter and returns a number of this temperature in degrees Celsius.
"""
def convertToFahrenheit(Celsius):
    return Celsius * (9 / 5) + 32

def convertToCelsius(Fahrenheit):
    return (Fahrenheit - 32) * (5 / 9)

print(convertToCelsius(0))

print(convertToCelsius(180))

print(convertToFahrenheit(0))

print(convertToFahrenheit(100))

print(convertToCelsius(convertToFahrenheit(15)))

print(convertToCelsius(convertToFahrenheit(42)))