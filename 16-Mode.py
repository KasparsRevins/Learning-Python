
"""
Mode is the third statistical calculation exercise in this book. 
The mode is the number that appears most frequently in a list of numbers. Together with the median and average, you can get a descriptive summary of a list of numbers. 
This exercise tests your ability to use a dictionary to keep a count of the numbers in a list to find the most frequent number.

Exercise Description

Write a mode() function that has a numbers parameter. 
This function returns the mode, or most frequently appearing number, of the list of integer and floating-point numbers passed to the function.
"""

def mode(numbers):
    if not numbers:
        return None
    counter = 0
    num = numbers[0]

    for i in numbers:
        frequency = numbers.count(i)
        if (frequency > counter):
            counter = frequency
            num = i
    return num

assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)

testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4