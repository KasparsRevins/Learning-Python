
"""
If you put a list of numbers into sorted order, the median number is the number at the halfway point. 
Outliers can cause the statistical average to be much higher or smaller than the majority of numbers, so that the median number may give you a better idea of the characteristics of the numbers in the list. 
This, the previous, and the next exercise challenge you to make Python solve these statistics calculations.

Exercise Description

Write a median() function that has a numbers parameter. This function returns the statistical median of the numbers list. 
The median of an odd-length list is the number in the middlemost number when the list is in sorted order. 
If the list has an even length, the median is the average of the two middlemost numbers when the list is in sorted order. Feel free to use Python’s built-in sort() method to sort the numbers list.
"""

def median(numbers):
    numbers.sort()
    x = len(numbers)
    if not numbers:
        return None
    result = 0
    for number in numbers:
        result += number
    if x % 2 == 0:
        average = result / x
    else:
        average = result / x
        return round(average)
    return average
    



assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random

random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6