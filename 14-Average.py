
"""
Averages are an essential statistical tool, and computers make it easy to calculate the average of millions or billions of numbers. 
The average is the sum of a set of the numbers divided by the amount of numbers. 
For example, the average of 12, 1, and 5 is 6, because 12 + 1 + 5 is 18 and 18 / 3 is 6. This and the following two exercises challenge you to make Python solve these statistics calculations.

Exercise Description

Write an average() function that has a numbers parameter. This function returns the statistical average of the list of integer and floating-point numbers passed to the function. 
While Python’s built-in sum() function can help you solve this exercise, try writing the solution without using it.
"""

def average(numbers):
    if not numbers:
        return None
    
    x = len(numbers)

    result = 0
    for number in numbers:
        result += number
    average = result // x
    return average

assert average([1, 2, 3]) == 2

assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2

assert average([12, 20, 37]) == 23

assert average([0, 0, 0, 0, 0]) == 0

import random

random.seed(42)

testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]

for i in range(1000):

    random.shuffle(testData)

    assert average(testData) == 2