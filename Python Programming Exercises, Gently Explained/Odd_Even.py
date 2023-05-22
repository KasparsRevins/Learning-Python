
"""
Determining if a number is even or odd is a common calculation that uses the modulo operator.
Like Exercise #2, “Temperature Conversion,” the functions for this exercise’s solution functions can be as little as one line long.

This exercise covers the % modulo operator, and the technique of using modulo-2 arithmetic to determine if a number is even or odd.

Exercise Description

Write two functions, isOdd() and isEven(), with a single numeric parameter named number. The isOdd() function returns True if number is odd and False if number is even. The isEven() function returns the True if number is even and False if number is odd.
Both functions return False for numbers with fractional parts, such as 3.14 or -4.5. Zero is considered an even number.
"""


def isOdd(number):
    if number % 2 == 0:
        return False
    elif type(number) == float:
        return False
    else:
        return True
    
def isEven(number):
    if number % 2 == 0:
        return True
    elif type(number) == float:
        return False
    else:
        return False
    
print(isOdd(42))
print(isOdd(9999))
print(isOdd(-10))
print(isOdd(-11))
print(isOdd(3.1415))