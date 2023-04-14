
"""
Area, perimeter, volume, and surface area are straightforward calculations. This exercise is similar to Exercise #2, “Temperature Conversion” and Exercise #3, “Odd & Even.” Each function in this exercise is a simple calculation and return statement.
However, area and volume are slightly more complicated because they involve multiple parameters. This exercise continues to challenge you to translate mathematical formulas into Python code.

Exercise Description

You will write four functions for this exercise. The functions area() and perimeter() have length and width parameters and the functions volume() and surfaceArea() have length, width, and height parameters.
These functions return the area, perimeter, volume, and surface area, respectively.
"""

def area(Length, Width):
    return Length * Width

def perimeter(Length, Width):
    return Length + Width + Length + Width

def volume(Length, Width, Height):
    return Length * Width * Height

def surfaceArea(Length, Width, Height):
    return (Length * Width * 2) + (Length * Height * 2) + (Width * Height * 2)

assert area(10, 10) == 100

assert area(0, 9999) == 0

assert area(5, 8) == 40

assert perimeter(10, 10) == 40

assert perimeter(0, 9999) == 19998

assert perimeter(5, 8) == 26

assert volume(10, 10, 10) == 1000

assert volume(9999, 0, 9999) == 0

assert volume(5, 8, 10) == 400

assert surfaceArea(10, 10, 10) == 600

assert surfaceArea(9999, 0, 9999) == 199960002

assert surfaceArea(5, 8, 10) == 340